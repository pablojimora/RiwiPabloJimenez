CREATE TABLE users (
id_user INT AUTO_INCREMENT PRIMARY KEY,
userName VARCHAR(100),
role VARCHAR(100),
created_at DATETIME
);

CREATE TABLE posts (
id_post INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255),
status VARCHAR(255),
create_at DATETIME,
id_user INT, 
FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE followings (
id_followings INT AUTO_INCREMENT PRIMARY KEY,
id_follower INT,
id_followed INT, 
FOREIGN KEY (id_follower) REFERENCES users(id_user),
FOREIGN KEY (id_followed) REFERENCES users(id_user)
);

INSERT INTO users (userName, role, created_at) VALUES
('Carlos Pérez', 'admin', '2025-01-10 09:15:00'),
('María Gómez', 'user', '2025-01-12 10:30:00'),
('Juan Rodríguez', 'user', '2025-01-15 08:45:00'),
('Ana Torres', 'moderator', '2025-01-16 14:20:00'),
('Luis Martínez', 'user', '2025-01-17 12:00:00'),
('Laura Sánchez', 'user', '2025-01-18 09:10:00'),
('Pedro Castillo', 'admin', '2025-01-19 11:25:00'),
('Sofía Ramírez', 'user', '2025-01-20 16:40:00'),
('Diego Herrera', 'user', '2025-01-21 10:00:00'),
('Felipe Londoño', 'guest', '2025-01-10 09:15:00'),
('Valentina López', 'moderator', '2025-01-22 09:55:00');

INSERT INTO posts (title, status, create_at, id_user) VALUES
('Primer post de Carlos', 'publicado', '2025-02-01 10:00:00', 1),
('Receta de cocina fácil', 'publicado', '2025-02-02 12:10:00', 2),
('Mis vacaciones en la playa', 'borrador', '2025-02-03 08:30:00', 3),
('Reglas del foro', 'publicado', '2025-02-04 09:00:00', 4),
('Cómo aprender SQL rápido', 'publicado', '2025-02-05 15:40:00', 5),
('Noticias de tecnología', 'borrador', '2025-02-06 11:00:00', 1),
('Nueva funcionalidad en la app', 'publicado', '2025-02-06 14:25:00', 7),
('Reseña de película', 'publicado', '2025-02-07 18:10:00', 6),
('Tips para programar en Python', 'borrador', '2025-02-08 08:55:00', 8),
('Evento de la comunidad', 'publicado', '2025-02-09 17:20:00', 9),
('Tutorial de fotografía', 'publicado', '2025-02-10 13:45:00', 2),
('Primer post de Carlos', 'publicado', '2025-07-30 10:00:00', 1),
('Guía de ejercicios en casa', 'eliminado', '2025-02-11 19:00:00', 5);

INSERT INTO followings (id_follower, id_followed) VALUES
(2, 1),
(3, 1),
(4, 1),
(5, 2),
(6, 2),
(7, 3),
(8, 3),
(9, 4),
(10, 4),
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 9),
(7, 10),
(8, 1),
(9, 2);

-- 1. Listar todos los usuarios
SELECT * FROM users;

-- 2. Post publicados por el usuario con username sofia\_g
SELECT * FROM posts
JOIN users ON posts.id_user = users.id_user WHERE users.userName = 'Carlos Pérez';

-- 3. Mostrar todos los usuarios con rol admin
SELECT * FROM users WHERE role='Admin';

-- 4. Ver todos los posts con estado publicado
SELECT * FROM posts WHERE status= 'publicado';

-- 5. Mostrar los nombres de los usuarios que estan siendo seguidos
SELECT userName FROM users
JOIN followings ON users.id_user = followings.id_followed GROUP BY(id_user); 

-- 6. Consultar el numero total de usuarios
SELECT COUNT(*) AS numero_de_usuarios FROM users;

-- 7. Mostrar los titulos de los posts creados hoy
SELECT title FROM posts WHERE DATE (create_at)=CURDATE(); -- Hoy
SELECT title FROM posts WHERE DATE (create_at)="2025-02-01"; -- Otra fecha

-- 8. Obtener el nombre del autor y titulo de cada post
SELECT users.userName, posts.title FROM posts
JOIN users ON users.id_user = posts.id_user;

-- 9. Listar los usuarios junto con la cantidad de seguidores que tienen

SELECT userName, COUNT(*) AS numero_de_seguidores FROM users
JOIN followings ON users.id_user = followings.id_followed GROUP BY(id_user); 

-- 10. Mostrar los usuarios que no han publicado ningun post
SELECT users.*
FROM users
LEFT JOIN posts ON users.id_user = posts.id_user WHERE posts.title IS NULL;

-- 11. Mostrar los posts junto con el numero de palabras en el contenido (`body`)
SELECT title, LENGTH(title) - LENGTH(REPLACE(title, ' ', '')) + 1 AS Palabras from posts;

-- 12. Consultar cuantos usuarios hay por tipo de rol
SELECT role, COUNT(*) AS cantidad FROM users GROUP BY (role);


-- 13. Obtener la fecha y autor del post mas reciente
SELECT users.userName , posts.create_at FROM users 
JOIN posts ON users.id_user = posts.id_user ORDER BY DATE(create_at) DESC LIMIT 1; 

-- 14. Mostrar los usuarios que siguen a mas de 3 personas
SELECT users.userName, COUNT(*) AS seguidos FROM users
JOIN followings ON users.id_user = followings.id_follower GROUP BY id_user HAVING COUNT(*)  > 3; 




