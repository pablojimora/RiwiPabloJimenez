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


INSERT INTO estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) VALUES 
('Pablo Jimenez Mora', 'pablo@email.com', 'masculino','111111', 'ingenieria biomedica', '2001-4-15', '2026-3-12'),
('Carolina Serna Gomez', 'caro@email.com', 'femenino', '222222', 'arquitectura', '2002-10-18', '2025-6-12'),
('Felipe Londoño', 'pipe@email.com', 'masculino', '333333', 'ingeniero agronomo', '2002-01-30', '2026-6-5'),
('Laura Cristina Gomez Gomez', 'laura@email.com', 'femenino', '444444', 'medico', '2001-08-24','2025-08-06'),
('Alejandro Madrigal Montoya', 'alejandro@email.com', 'masculino', '555555', 'medico', '2001-10-1', '2025-4-15');

INSERT INTO docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) VALUES
('David Henao', 'davidhenao@riwi.io','Desarrollo',12), 
('Andrea Taborda', 'andrea@riwi.io','Fisiopatologia',10), 
('Mateo Hurtado', 'mateo@riwi.io', 'taller arquitectonico', 15);

INSERT INTO cursos (nombre, codigo, creditos, semestre, id_docente) VALUES
('Algoritmia', '01', 4, 5, 1),
('Fisiopatologia II', '02', 6, 8, 2),
('Taller 9', '03', 8, 9, 3),
('Java', '04', 6, 7, 1);

INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) 
VALUES (1, 1, '2027-01-20', 100),
(1, 4, '2027-01-20', 90),
(2, 3, '2027-02-02', 100),
(3, 4, '2027-01-20', 71),
(3, 1, '2027-01-20', 80),
(4, 2, '2027-01-15', 70),
(5, 2, '2027-01-15', 100),
(5, 1, '2027-01-20', 100),
(4, 1, '2027-01-20', 77);

-- Obtener el listado de todos los estudiantes junto con sus inscripciones y cursos (JOIN)

SELECT e.nombre_completo AS Estudiante, c.nombre AS Curso FROM estudiantes e
LEFT JOIN inscripciones m ON e.id_estudiante = m.id_estudiante
LEFT JOIN cursos c ON m.id_curso = c.id_curso;

-- Listar los cursos dictados por docentes con más de 5 años de experiencia.
SELECT cursos.nombre, docentes.nombre_completo FROM cursos
JOIN docentes ON cursos.id_docente = docentes.id_docente WHERE anios_experiencia > 5;

-- Obtener el promedio de calificaciones por curso (GROUP BY + AVG).

SELECT nombre , AVG(calificacion_final) AS promedio FROM cursos
JOIN inscripciones ON cursos.id_curso = inscripciones.id_curso GROUP BY cursos.id_curso;

-- Mostrar los estudiantes que están inscritos en más de un curso (HAVING COUNT(*) > 1)

SELECT e.nombre_completo, COUNT(i.id_estudiante) AS numero_inscripciones FROM estudiantes e 
JOIN inscripciones i ON i.id_estudiante = e.id_estudiante GROUP BY e.id_estudiante HAVING COUNT(i.id_curso )>1;

-- Agregar una nueva columna estado_academico a la tabla estudiantes (ALTER TABLE).

ALTER TABLE estudiantes ADD estado_academico VARCHAR(100);
SELECT * FROM estudiantes;

-- Eliminar un docente y observar el efecto en la tabla cursos (uso de ON DELETE en FK).

DELETE FROM docentes WHERE id_docente=3;

-- SQL Error [1451] [23000]: Cannot delete or update a parent row: a foreign key constraint fails 
-- (`gestion_academica_universidad`.`cursos`, CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `docentes` (`id_docente`))
-- Este error aparece ya que se intenta eliminar o actualizar un registro en la tabla docentes, pero ese registro todavía
-- está siendo referenciado en la tabla cursos mediante la clave foránea id_docente. Para poder eliminarlo habría que eliminar primero la calve foránea 
-- de la tabla cursos o cambiar el profesor para que el que se vaya a eliminar no dependa ningun curso



-- Consultar los cursos en los que se han inscrito más de 2 estudiantes (GROUP BY + COUNT + HAVING).

SELECT c.nombre, COUNT(i.id_estudiante) FROM cursos c 
JOIN inscripciones i ON i.id_curso = c.id_curso GROUP BY c.id_curso HAVING COUNT(i.id_curso )>2;

-- Obtener los estudiantes cuya calificación promedio es superior al promedio general (AVG() + subconsulta).

SELECT e.nombre_completo , AVG(calificacion_final) AS promedio FROM estudiantes e
JOIN inscripciones i ON i.id_estudiante  = e.id_estudiante GROUP BY e.id_estudiante HAVING AVG(calificacion_final > (SELECT AVG(calificacion_final) FROM inscripciones)
);

-- Mostrar los nombres de las carreras con estudiantes inscritos en cursos del semestre 2 o posterior (IN o EXISTS).

SELECT e.carrera, c.semestre FROM estudiantes e
JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
JOIN cursos c ON c.id_curso = i.id_curso WHERE c.semestre > 3;


-- Vista
CREATE VIEW vista_historial_academico AS
SELECT e.nombre_completo AS estudiante, c.nombre AS curso, d.nombre_completo AS docente, c.semestre, i.calificacion_final FROM estudiantes e
JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
JOIN cursos c ON c.id_curso = i.id_curso
JOIN docentes d ON d.id_docente = c.id_docente;



-- Creaciones de usuarios
CREATE ROLE revisor_academico;

GRANT SELECT ON vista_historial_academico TO revisor_academico;

-- Revoque de los permisos de revisor_academico en inscripciones

REVOKE INSERT, UPDATE , DELETE ON inscripciones FROM revisor_academico;

-- SQL Error [1147] [42000]: There is no such grant defined for user 'revisor_academico' on host '%' on table 'inscripciones'
-- Este error se genera ya que al momento de crear un rol, este se genera sin permisos, por ende no hay necesidad de quitarlos




-- Simulacion y operaciones de actualización de calificaciones 

BEGIN;

UPDATE inscripciones SET calificacion_final= 100 WHERE id_estudiante = 3 AND id_curso = 4;

SAVEPOINT cambio_nota_felipe;

UPDATE inscripciones SET calificacion_final = 50 WHERE id_estudiante = 2 AND id_curso = 3;

SAVEPOINT cambio_nota_carolina;

ROLLBACK TO cambio_nota_felipe;

COMMIT;


SELECT * FROM vista_historial_academico;

















