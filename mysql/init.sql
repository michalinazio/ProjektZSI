CREATE TABLE lizards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    votes INT DEFAULT 0
);

INSERT INTO lizards (name) VALUES ('Jaszczurka1'), ('Jaszczurka2'), ('Jaszczurka3');