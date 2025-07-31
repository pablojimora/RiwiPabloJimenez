CREATE DATABASE IF NOT EXISTS gestion_academica_universidad;

USE gestion_academica_universidad;

CREATE TABLE estudiantes (id_estudiante INT AUTO_INCREMENT PRIMARY KEY, 
nombre_completo VARCHAR(100) NOT NULL, 
correo_electronico VARCHAR(255) NOT NULL UNIQUE,  
genero ENUM ('Masculino','Femenino','Otro') NOT NULL, 
identificacion VARCHAR(20) NOT NULL UNIQUE, 
carrera VARCHAR(100) NOT NULL, 
fecha_nacimiento DATE NOT NULL, 
fecha_ingreso DATE NOT NULL );


CREATE TABLE docentes ( id_docente INT AUTO_INCREMENT PRIMARY KEY, 
nombre_completo VARCHAR(100) NOT NULL, 
correo_institucional VARCHAR(255) NOT NULL UNIQUE, 
departamento_academico VARCHAR(100) NOT NULL, 
anios_experiencia INT NOT NULL CHECK (anios_experiencia >=0));

CREATE TABLE cursos (
id_curso INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
codigo INT NOT NULL UNIQUE,
creditos INT NOT NULL CHECK(creditos>0),
semestre INT NOT NULL CHECK(semestre BETWEEN 1 AND 12),
id_docente INT NOT NULL, 
FOREIGN KEY (id_docente) REFERENCES docentes(id_docente));

CREATE TABLE inscripciones ( id_inscripcion INT AUTO_INCREMENT PRIMARY KEY, 
id_estudiante INT NOT NULL, 
id_curso INT NOT NULL, 
fecha_inscripcion DATE NOT NULL, 
calificacion_final INT CHECK(calificacion_final BETWEEN 0 AND 100), 
FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante), 
FOREIGN KEY (id_curso) REFERENCES cursos(id_curso), 
UNIQUE(id_estudiante, id_curso) );


INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) 
VALUES ('Pablo Jimenez Mora', 'pablo@email.com', 'masculino','111111', 'ingenieria biomedica', '2001-4-15', '2026-3-12');

INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) 
VALUES ('Carolina Serna Gomez', 'caro@email.com', 'femenino', '222222', 'arquitectura', '2002-10-18', '2025-6-12');

INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) 
VALUES ('Laura Cristina Gomez Gomez', 'laura@email.com', 'femenino', '444444', 'medico', '2001-08-24','2025-08-06'); 

INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) 
VALUES ('Alejandro Madrigal Montoya', 'alejandro@email.com', 'masculino', '555555', 'medico', '2001-10-1', '2025-4-15');


INSERT INTO docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) 
VALUES  ('David Henao', 'davidhenao@riwi.io','Desarrollo',12), 
('Andrea Taborda', 'andrea@riwi.io','Fisiopatologia',10), 
('Mateo Hurtado', 'mateo@riwi.io', 'taller arquitectonico', 15);

INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) 
VALUES ('Algoritmia', '01', 4, 5, 1),
('Fisiopatologia II', '02', 6, 8, 2),
('Taller 9', '03', 8, 9, 3),
('Java', '04', 6, 7, 1);

INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) 
VALUES (1, 1, '2027-01-20', 5),
(1, 4, '2027-01-20', 5),
(2, 3, '2027-02-02', 5),
(3, 4, '2027-01-20', 4),
(3, 1, '2027-01-20', 3.6),
(4, 2, '2027-01-15', 4),
(5, 2, '2027-01-15', 5),
(5, 1, '2027-01-20', 3),
(4, 1, '2027-01-20', 3.6);

-- Obtener el listado de todos los estudiantes junto con sus inscripciones y cursos (JOIN)

SELECT e.nombre_completo AS Estudiante, c.nombre AS Curso FROM estudiantes e
LEFT JOIN inscripciones m ON e.id_estudiante = m.id_estudiante
LEFT JOIN cursos c ON m.id_curso = c.id_curso;











