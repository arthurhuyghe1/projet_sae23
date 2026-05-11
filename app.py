import os
import time
import pymysql
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'une_cle_secrete_tres_complexe'

# Configuration de la base de données via variables d'environnement (définies dans docker-compose)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'iut_lab')

def get_db_connection():
    # Retry mechanism pour s'assurer que la db a démarré
    max_retries = 5
    for i in range(max_retries):
        try:
            connection = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except pymysql.err.OperationalError as e:
            if i < max_retries - 1:
                time.sleep(2)
            else:
                raise e

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        if role == 'student':
            session['role'] = 'student'
            return redirect(url_for('inventory'))
        elif role == 'admin':
            password = request.form.get('password')
            if password == 'admin':
                session['role'] = 'admin'
                return redirect(url_for('inventory'))
            else:
                flash('Mot de passe administrateur incorrect.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/inventory')
def inventory():
    if 'role' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products ORDER BY id DESC")
            products = cursor.fetchall()
    finally:
        conn.close()
        
    return render_template('inventory.html', products=products, role=session['role'])

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if session.get('role') != 'admin':
        return redirect(url_for('inventory'))
        
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        description = request.form['description']
        
        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (name, quantity, description) VALUES (%s, %s, %s)",
                    (name, quantity, description)
                )
            conn.commit()
            flash('Produit ajouté avec succès.', 'success')
            return redirect(url_for('inventory'))
        finally:
            conn.close()
            
    return render_template('add_edit.html', action='Ajouter')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    if session.get('role') != 'admin':
        return redirect(url_for('inventory'))
        
    conn = get_db_connection()
    try:
        if request.method == 'POST':
            name = request.form['name']
            quantity = request.form['quantity']
            description = request.form['description']
            
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE products SET name=%s, quantity=%s, description=%s WHERE id=%s",
                    (name, quantity, description, id)
                )
            conn.commit()
            flash('Produit modifié avec succès.', 'success')
            return redirect(url_for('inventory'))
        else:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
                product = cursor.fetchone()
                if not product:
                    flash('Produit introuvable.', 'error')
                    return redirect(url_for('inventory'))
            return render_template('add_edit.html', action='Modifier', product=product)
    finally:
        conn.close()

@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    if session.get('role') != 'admin':
        return redirect(url_for('inventory'))
        
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        conn.commit()
        flash('Produit supprimé avec succès.', 'success')
    finally:
        conn.close()
        
    return redirect(url_for('inventory'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
