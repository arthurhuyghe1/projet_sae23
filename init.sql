SET NAMES utf8mb4;
CREATE DATABASE IF NOT EXISTS iut_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE iut_lab;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    item_type ENUM('outil', 'consommable') NOT NULL DEFAULT 'outil',
    pictograms VARCHAR(255) DEFAULT '',
    qty_lab1 INT NOT NULL DEFAULT 0,
    qty_lab2 INT NOT NULL DEFAULT 0,
    qty_reserve INT NOT NULL DEFAULT 0,
    description TEXT
);

INSERT INTO products (name, item_type, pictograms, qty_lab1, qty_lab2, qty_reserve, description) VALUES
('Microscopes Binoculaires', 'outil', '', 5, 5, 2, 'Microscopes optiques pour TP de biologie.'),
('Pipettes Pasteur (boîte)', 'outil', '', 1, 2, 2, 'Boîtes de 100 pipettes en verre.'),
('Béchers 250ml', 'outil', '', 15, 15, 15, 'Béchers en verre Pyrex.'),
('Oscilloscopes Numériques', 'outil', '', 4, 4, 0, 'Oscilloscopes 2 voies 50MHz.'),
('Générateurs Basses Fréquences', 'outil', '', 5, 5, 0, 'GBF avec formes d''onde sinus/carré/triangle.'),
('Acide Chlorhydrique (1L)', 'consommable', 'corrosif,nocif', 0, 0, 10, 'Solution d''acide chlorhydrique concentrée. Stockage en réserve uniquement.'),
('Soude Caustique (1L)', 'consommable', 'corrosif', 2, 2, 5, 'Solution d''hydroxyde de sodium. Attention corrosif.'),
('Poudre de Fer (500g)', 'consommable', 'inflammable', 1, 0, 3, 'Limaille de fer pour expériences de magnétisme et chimie.');
