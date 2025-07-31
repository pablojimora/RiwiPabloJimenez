Cuestionario de Investigación: Fundamentos de Bases de Datos
1. ¿Qué es un dato?

    ¿Cómo se define un dato en informática?
    Un dato en informática es una representación simbólica (numérica, alfabética, etc.) de un hecho, valor o entidad. Carece de significado por sí solo hasta que se procesa o interpreta en un contexto. Es la unidad básica de información.

    ¿Qué tipos de datos existen?
    Los tipos de datos más comunes incluyen:

        Numéricos: Enteros (int), decimales (float, double).

        Texto: Cadenas de caracteres (string, char).

        Booleanos: Verdadero o falso (true/false).

        Fechas y horas: Para almacenar fechas, horas o marcas temporales (date, timestamp).

        Binarios: Archivos o datos en formato binario (blob).

        Estructurados: Arreglos, objetos o estructuras complejas (JSON, XML).

    ¿Puedes dar un ejemplo de dato en una aplicación web?
    En una aplicación web de comercio electrónico, un dato puede ser el nombre de un producto, como “Camiseta Azul”, almacenado como una cadena de texto (string).

2. ¿Qué es una base de datos?

    ¿Para qué se utiliza una base de datos?
    Una base de datos es una colección organizada de datos, diseñada para almacenar, gestionar y recuperar información de manera eficiente. Se utiliza para organizar datos, facilitar consultas, garantizar la integridad y soportar aplicaciones.

    ¿Cuál es la diferencia entre almacenar datos en archivos y en una base de datos?

        Archivos: Los datos se guardan en formatos como texto, CSV o Excel, sin una estructura rígida. La búsqueda y gestión son manuales, menos eficientes y propensas a errores.

        Base de datos: Los datos se organizan en estructuras (tablas, documentos, etc.), permitiendo consultas rápidas, escalabilidad, integridad y concurrencia.

        Diferencias clave: Las bases de datos ofrecen mejor organización, seguridad, escalabilidad y soporte para múltiples usuarios.

    Menciona un ejemplo de uso en la vida real.
    Una base de datos en un hospital que almacena registros de pacientes, incluyendo nombres, fechas de nacimiento, diagnósticos y tratamientos, para facilitar la gestión médica.

3. ¿Qué es un motor de base de datos?

    ¿Qué papel cumple el motor en una base de datos?
    El motor de base de datos es el software que gestiona el almacenamiento, recuperación, actualización y administración de los datos. Procesa las consultas, asegura la integridad y controla el acceso.

    ¿En qué se diferencia de una base de datos como tal?

        Base de datos: Es la colección de datos organizada.

        Motor de base de datos: Es el sistema que administra la base de datos, ejecuta operaciones y garantiza su funcionamiento.

    ¿Cuáles son algunos motores de base de datos conocidos?

        Relacionales: MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.

        NoSQL: MongoDB, Cassandra, Redis, Couchbase.

4. Bases de Datos Relacionales (SQL)

    ¿Qué significa que una base de datos sea “relacional”?
    Organiza los datos en tablas con filas y columnas, donde las tablas están relacionadas mediante claves (primarias y foráneas). Utiliza el modelo relacional para establecer conexiones lógicas entre los datos.

    ¿Qué ventajas ofrece el uso de SQL?

        Estandarización: Es un lenguaje estructurado y ampliamente aceptado.

        Integridad: Garantiza la consistencia de los datos mediante restricciones.

        Consultas complejas: Permite operaciones avanzadas como las uniones (JOIN).

        Seguridad: Ofrece un control robusto de acceso y permisos.

    ¿Cuáles son algunos motores de bases de datos relacionales populares?
    MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server y SQLite.

5. Bases de Datos NoSQL

    ¿Qué significa NoSQL y en qué se diferencia de SQL?
    NoSQL significa “Not Only SQL” y se refiere a bases de datos no relacionales que no usan tablas ni esquemas fijos. A diferencia de SQL, NoSQL maneja datos no estructurados o semiestructurados y está diseñada para una alta escalabilidad horizontal.

    ¿Qué tipos de bases de datos NoSQL existen?

        Clave-valor: Redis, DynamoDB.

        Documentales: MongoDB, CouchDB.

        Columnares: Cassandra, HBase.

        Gráficas: Neo4j, ArangoDB.

    ¿Cuáles son ejemplos de motores NoSQL?
    MongoDB, Cassandra, Redis, Couchbase y Neo4j.

6. SQL vs. NoSQL: ¿Cuándo usar cada una?

    Escenario de uso ideal para SQL:
    Un sistema bancario que requiere transacciones consistentes (ACID) y relaciones complejas entre cuentas, clientes y transacciones. SQL garantiza la integridad y soporta estas consultas relacionales de forma nativa.

    Escenario de uso ideal para NoSQL:
    Una red social que maneja grandes volúmenes de datos no estructurados, como publicaciones, "me gusta" y comentarios. NoSQL permite una escalabilidad horizontal masiva y una mayor flexibilidad en el esquema de datos.

Comparativa: SQL vs. NoSQL

    Estructura de Datos

        SQL (Relacional): Tablas con esquema fijo y predefinido.

        NoSQL (No Relacional): Documentos, grafos, clave-valor, etc., con esquema dinámico.

    Lenguaje de Consulta

        SQL (Relacional): SQL (Lenguaje de Consulta Estructurado).

        NoSQL (No Relacional): Varía según el motor (sin un estándar único).

    Escalabilidad

        SQL (Relacional): Vertical, aumentando la potencia de un solo servidor (CPU, RAM).

        NoSQL (No Relacional): Horizontal, distribuyendo la carga entre múltiples servidores.

    Manejo de Relaciones

        SQL (Relacional): Mediante claves primarias y foráneas (JOINs).

        NoSQL (No Relacional): Anidando datos (documentos) o mediante referencias en la aplicación.

    Consistencia

        SQL (Relacional): Fuerte consistencia (modelo ACID).

        NoSQL (No Relacional): Consistencia eventual (modelo BASE), prioriza la disponibilidad.

    Casos de Uso

        SQL (Relacional): Sistemas transaccionales, ERP, finanzas, data warehousing.

        NoSQL (No Relacional): Big Data, redes sociales, IoT, catálogos de productos.