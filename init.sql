CREATE DATABASE IF NOT EXISTS iut_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE iut_lab;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    description TEXT
);

INSERT INTO products (name, quantity, description) VALUES
('Microscopes Binoculaires', 12, 'Microscopes optiques pour TP de biologie.'),
('Pipettes Pasteur (boîte)', 5, 'Boîtes de 100 pipettes en verre.'),
('Béchers 250ml', 45, 'Béchers en verre Pyrex.'),
('Oscilloscopes Numériques', 8, 'Oscilloscopes 2 voies 50MHz.'),
('Générateurs Basses Fréquences', 10, 'GBF avec formes d''onde sinus/carré/triangle.');
