import express, { json } from 'express'; 
import { createConnection } from 'mysql2';
import cors from 'cors';

const app = express(); //asignamos a la palabra app la instancia de express
app.use(cors());
app.use(json());

const db = createConnection({
  host: 'localhost',
  user: 'root',
  password: '', // tu contraseña si tienes
  database: 'pablo_db' // El nombre de tu DB
});

// Obtener usuarios
app.get('/usuarios', (req, res) => {
  db.query('SELECT * FROM usuarios', (err, results) => {
    if (err) return res.status(500).json(err);
    res.json(results);
  });
});

// Agregar usuario
app.post('/usuarios', (req, res) => {
  const { nombre, email } = req.body;
  db.query('INSERT INTO usuarios (nombre, email) VALUES (?, ?)', [nombre, email], (err) => {
    if (err) return res.status(500).json(err);
    res.json({ message: 'Usuario agregado' });
  });
});

//Actualizar usuario
app.put('/usuarios/:id', (req, res) => {
  const { id, nombre, email } = req.body;
  db.query('UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?', [nombre, email, id], (err) => {
    if (err) return res.status(500).json(err);
    res.json({ message: 'Usuario actualizado' });
  });
});

//Eliminar usuario
app.delete('/usuarios/:id', (req, res) => {
  const { id } = req.params;
  db.query('DELETE FROM usuarios WHERE id = ?', [id], (err) => {
    if (err) return res.status(500).json(err);
    res.json({ message: 'Usuario eliminado' });
  });
});


// Agrega los metodos put, y delete para el endpoint /users

app.listen(3000, () => console.log('Servidor corriendo en http://localhost:3000'));