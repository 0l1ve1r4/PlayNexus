-- PlayNexus application database structure definition script.
-- WARNING: Running this will erase and rebuild the database!
-- Requires a MySQL database server to run.

DROP DATABASE IF EXISTS PlayNexus;

CREATE DATABASE PlayNexus;

USE PlayNexus;

-- Creates the table that will store user's account information:
CREATE TABLE Account (
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    type ENUM('Gamer', 'Publisher') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (email)
);

-- Creates the table that will store the gamer's information:
CREATE TABLE Gamer (
    account VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    country VARCHAR(50) NOT NULL,
    bio VARCHAR(255),
    PRIMARY KEY (account),
    FOREIGN KEY (account) REFERENCES Account(email) ON DELETE CASCADE
);

-- Creates the table that will store the publisher's information:
CREATE TABLE Publisher (
    account VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (account),
    FOREIGN KEY (account) REFERENCES Account(email) ON DELETE CASCADE
);

-- Creates the table that will store the game's information:
CREATE TABLE Game (
    title VARCHAR(50) NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    developer VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
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
    gamer VARCHAR(50) NOT NULL,
    game VARCHAR(50) NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (gamer, title, publisher),
    FOREIGN KEY (gamer) REFERENCES Gamer(account) ON DELETE CASCADE,
    FOREIGN KEY (game, publisher) REFERENCES Game(title, publisher) ON DELETE CASCADE
);
