-- PlayNexus application database structure definition script.
-- WARNING: Running this will erase and rebuild the database!
-- Requires a MySQL database server to run.

DROP DATABASE IF EXISTS PlayNexus;

CREATE DATABASE PlayNexus;

USE PlayNexus;

-- Creates the table that will store user's account information:
CREATE TABLE Account (
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    type ENUM('Gamer', 'Publisher') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (email)
);

-- Creates the table that will store the gamer's information:
CREATE TABLE Gamer (
    account VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    country VARCHAR(255) NOT NULL,
    bio VARCHAR(255),
    PRIMARY KEY (account),
    FOREIGN KEY (account) REFERENCES Account(email) ON DELETE CASCADE
);

-- Creates the table that will store the publisher's information:
CREATE TABLE Publisher (
    account VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (account),
    FOREIGN KEY (account) REFERENCES Account(email) ON DELETE CASCADE
);

-- Creates the table that will store the game's information:
CREATE TABLE Game (
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    developer VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    publication_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255) NOT NULL,
    cover BLOB,
    installer LONGBLOB,
    price DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (title, publisher),
    FOREIGN KEY (publisher) REFERENCES Publisher(account) ON DELETE CASCADE
);

-- Creates the table that will store the purchase's information:
CREATE TABLE Purchase (
    gamer VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (gamer, title, publisher),
    FOREIGN KEY (gamer) REFERENCES Gamer(account) ON DELETE CASCADE,
    FOREIGN KEY (title, publisher) REFERENCES Game(title, publisher) ON DELETE CASCADE
);
