-- create table
CREATE TABLE IF NOT EXISTS users (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    );