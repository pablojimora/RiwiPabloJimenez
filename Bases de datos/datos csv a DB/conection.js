import fs from 'fs';
import csv from 'csv-parser';
import mysql from 'mysql2';

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Maria0295*',
    database: 'tienda'
});

db.connect((error) => {
    if (error) throw error;
    console.log('Conectado exitosamente a la db');
})

fs.createReadStream('products.csv')
    .pipe(csv())
    .on('data', (row) => {
            db.query('INSERT INTO product (product, price, amount, isActive) VALUES (?, ?, ?, ?)', [row.product, parseFloat(row.price), parseInt(row.amount), row.isActive === 'True'], (error, results) => {
            if (error) throw error;
            console.log(`Fila insertada: ${results.affectedRows}`);
        });
        console.log(row);
        console.log('--');
    })
    .on('end', () => {
        console.log('CSV único procesado.');
        db.end();
    });