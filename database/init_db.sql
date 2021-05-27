CREATE DATABASE IF NOT EXISTS agiledb;

use agiledb;

drop table if exists Users;
drop table if exists Educations;
drop table if exists Projects;
drop table if exists Teammates;
drop table if exists Class;

CREATE TABLE IF NOT EXISTS Users (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    first_name  VARCHAR(30) NOT NULL,
    last_name   VARCHAR(30) NOT NULL,
    email       VARCHAR(50) NOT NULL,
    comment     VARCHAR(50) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Educations (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    school      varchar(50) NOT NULL,
    degree      varchar(30) NOT NULL,
    major       varchar(30) NOT NULL,
    date        varchar(30) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Projects (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    title       varchar(30) NOT NULL,
    description varchar(100) NOT NULL,
    link        varchar(50) NOT NULL,
    Image_src   varchar(50) NOT NULL,
    teamID      integer NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Teammates (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    url         varchar(60) NOT NULL,
    teamID      integer NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE Table IF NOT EXISTS Class (
    id          integer  AUTO_INCREMENT PRIMARY KEY,
    url         varchar(60) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into Users (first_name, last_name, email, comment) values ("Stephen", "Kim", "sskim@ucsd.edu", "This is my comment");

insert into Educations (school, degree, major, date) values ("University of California, San Diego", "Bachelor", "Electrical Engineering", "March 2022");

insert into Projects (title, description, link, Image_src, teamID) values ("ServiceUp", "Community Posting Board for services", "tbd", "tbd/static/images/ServiceUp.png", 0);

insert into Teammates (url, teamID) values ("http://143.198.73.78/",  0), ("http://165.232.153.255/",  0), ("tbd",  0);

insert into Class (url) values ("http://kimsternator.games/"), ("http://143.198.73.78/"), ("http://165.232.153.255/");