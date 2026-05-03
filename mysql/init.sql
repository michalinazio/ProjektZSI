SET NAMES 'utf8mb4';

CREATE TABLE lizards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    votes INT DEFAULT 0
)CHARACTER SET utf8mb4;

INSERT INTO lizards (name) VALUES ('Jaszczurka Zwinka'), ('Jaszczurka Zielona'), ('Jaszczurka Żyworodna');