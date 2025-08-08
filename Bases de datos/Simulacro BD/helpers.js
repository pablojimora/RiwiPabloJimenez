import fs from 'fs';
import csv from 'csv-parser';
import pkg from 'pg';

const { Pool } = pkg;

export const uploadCSV = () => {

// Configuración de PostgreSQL con datos reales
const db = new Pool({
  host: 'aws-0-us-east-1.pooler.supabase.com',
  user: 'postgres.hjgskaepwigeecypxegl',
  password: 'Maria0295*', // remplaza con tu contraseña de Supabase
  database: 'postgres',
  port: 6543,
  ssl: { rejectUnauthorized: false } // Supabase requiere SSL
});


let inserts = [];

fs.createReadStream('products.csv')
  .pipe(csv())
  .on('data', (row) => {
    const insertPromise = db.query(
      'INSERT INTO product (product, price, amount, isActive) VALUES ($1, $2, $3, $4)',
      [row.product, parseFloat(row.price), parseInt(row.amount), row.isActive === 'True']
    );
    inserts.push(insertPromise);
  })
  .on('end', async () => {
    try {
      await Promise.all(inserts);
      console.log(`Insertadas ${inserts.length} filas correctamente.`);
    } catch (err) {
      console.error('Error insertando datos:', err);
    } finally {
      await db.end();
      console.log('Conexión cerrada.');
    }
  })
}
