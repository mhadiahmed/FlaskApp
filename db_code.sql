-- users table

CREATE TABLE users (id INT(11) AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),username VARCHAR(100),email VARCHAR(100),password VARCHAR(100),date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,admin tinyint(1));

-- articales table 
CREATE TABLE articale (id INT(11) AUTO_INCREMENT PRIMARY KEY,title VARCHAR(100),content TEXT,created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,approve tinyint(1));