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
    classmate        varchar(40) NOT NULL,
    url         varchar(60) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into Users (first_name, last_name, email, comment) values ("Stephen", "Kim", "sskim@ucsd.edu", "This is my comment");

insert into Educations (school, degree, major, date) values ("University of California, San Diego", "Bachelor's Degree", "Electrical Engineering", "March 2022");

insert into Projects (title, description, link, Image_src, teamID) values ("ServiceUp", "Community Posting Board for services", "http://serviceup.tech/", "http://serviceup.tech/static/images/serviceUp.png", 0);

insert into Teammates (url, teamID) values ("http://143.198.73.78/",  0), ("http://165.232.153.255/",  0), ("tbd",  0);

    insert into Class (classmate, url) values ("Stephen Kim", "http://kimsternator.games/"), ("Vladimir Altov", "http://143.198.73.78/"),
                                    ("Manuel Sanchez","http://165.232.153.255/"), ("Joshua Ball", "tbd"),
                                    ("Sepehr Ardebilianfard", "http://165.232.131.14:3001"), ("Ankeen Arestakesyan", "http://144.126.210.32/"),
                                    ("Felipe Bailon", "http://143.198.136.37/"), ("Jiazheng Bian", "http://www.biandavid.com/"),
                                    ("Christian Bissett", "http://143.198.128.150:6543/"), ("James Chen", "http://143.198.57.119/"),
                                    ("Gourab Dastider", "http://144.126.215.62/"), ("Chaztine-Xiana Embucado", "http://143.198.59.27/"),
                                    ("Ashwin Ganesh", "tbd"), ("Tony Guan", "http://143.198.76.115/"),
                                    ("Jacinth Gudetti", "http://143.198.97.209/"), ("Bret Gustafson", "http://143.110.153.51/"),
                                    ("Aaron Hanna", "http://144.126.212.235/"), ("Andrew Hernandez", "http://www.cvwebring.com/"),
                                    ("Anwar Hsu", "http://anwarhsu.com/"), ("Myo Htoo", "http://143.110.229.54/"),
                                    ("Eddie Huang", "http://eddieh00.com/"), ("Hanjie Huang", "http://161.35.229.252/"),
                                    ("Isis Huang", "http://64.227.107.46/"), ("Tanvir Hussain", "http://128.199.10.10/"),
                                    ("Kimberly Johnson", "http://43.198.71.181/"), ("Jason Kaharudin", "http://178.128.96.97/"),
                                    ("Andrew Kahr", "http://165.232.131.189/"), ("Iris Kim", "http://143.198.136.173/"),
                                    ("Jake Kim", "http://128.199.3.204/"), ("Damon Koshmerl", "http://143.198.111.59/"),
                                    ("Mark Kragh", "http://167.99.122.242/"), ("Charles Lee", "http://35.185.251.8/"),
                                    ("Zhenwei Liu", "http://164.90.144.97/"), ("John Malgeri", "http://161.35.228.30/"),
                                    ("Christian Manalad", "http://165.232.141.195/"), ("Hector Montenegro", "http://165.232.152.55/"),
                                    ("Ariane Nazemi", "http://143.198.236.89/"), ("Emerson Noble", "http://143.110.234.12/"),
                                    ("Dong On", "http://128.199.15.251/"), ("Seok Park", "http:///"),
                                    ("Anjuman Raha", "http://161.35.239.252/"), ("Chonghao Tang", "http://165.232.157.102/"),
                                    ("Muhammad Taufek", "http://161.35.232.250/"), ("Hung Tong", "http://161.35.54.86/"),
                                    ("Carl Villegas", "http://143.198.59.67/"), ("Frederick Yang", "http://143.198.232.38/"),
                                    ("Aaron Yim", "http://165.232.143.129/"), ("Kasra Younessi", "http://64.227.101.230/"),
                                    ("Hang Zhang", "http://144.126.221.136/"), ("Siyuan Zhang", "http://143.198.98.101/");



