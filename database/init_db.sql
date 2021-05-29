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

insert into Educations (school, degree, major, date) values ("University of California, San Diego", "Bachelor's Degree", "Electrical Engineering", "March 2022");

insert into Projects (title, description, link, Image_src, teamID) values ("ServiceUp", "Community Posting Board for services", "tbd", "tbd/static/images/ServiceUp.png", 0);

insert into Teammates (url, teamID) values ("http://143.198.73.78/",  0), ("http://165.232.153.255/",  0), ("tbd",  0);

insert into Class (url) values ("http://kimsternator.games/"), ("http://143.198.73.78/"), ("http://165.232.153.255/"),
                                ("http://165.232.131.14:3000/"), ("http://144.126.210.32/"), ("http://143.198.136.37/"),
                                ("http://www.biandavid.com/"), ("http://143.198.128.150:6543/"), ("http://143.198.57.119/"),
                                ("http://144.126.215.62/"), ("http://143.198.59.27/"), ("http://143.198.76.115/"),
                                ("http://143.198.97.209/"), ("http://143.110.153.51/"), ("http://144.126.212.235/"),
                                ("http://www.cvwebring.com/"), ("http://anwarhsu.com/"), ("http://143.110.229.54/"),
                                ("http://eddieh00.com/"), ("http://161.35.229.252/"), ("http://64.227.107.46/"),
                                ("http://128.199.10.10/"), ("http://43.198.71.181/"), ("http://178.128.96.97/"),
                                ("http://165.232.131.189/"), ("http://143.198.136.173/"),
                                ("http://128.199.3.204/"), ("http://143.198.111.59/"), ("http://167.99.122.242/"),
                                ("http://35.185.251.8/"), ("http://164.90.144.97/"), ("http://161.35.228.30/"),
                                ("http://165.232.141.195/"), ("http://165.232.152.55/"), ("http://143.198.236.89/"),
                                ("http://143.110.234.12/"), ("http://128.199.15.251/"), ("http://161.35.239.252/"),
                                ("http://165.232.157.102/"), ("http://161.35.232.250/"), ("http://161.35.54.86/"),
                                ("http://143.198.59.67/"), ("http://143.198.232.38/"), ("http://165.232.143.129/"),
                                ("http://64.227.101.230/"), ("http://144.126.221.136/"), ("http://143.198.98.101/");



