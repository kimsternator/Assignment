# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv

load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Users;")
# will comment out after initially creating db

# Create a TStudents table (wrapping it in a try-except is good practice)
print("Creating Users table")
try:
  cursor.execute("""
    CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      comment     VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

print("Creating Educations table")
try:
  cursor.execute("""
      CREATE TABLE Educations (
        id          integer  AUTO_INCREMENT PRIMARY KEY,
        school      varchar(50) NOT NULL,
        degree      varchar(30) NOT NULL,
        major       varchar(30) NOT NULL,
        date        varchar(30) NOT NULL,
        created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    """)
except:
  print("Educations table already exists. Not recreating it.")

print("Creating Projects table")
try:
  cursor.execute("""
      CREATE TABLE Projects (
        id          integer  AUTO_INCREMENT PRIMARY KEY,
        title       varchar(30) NOT NULL,
        description varchar(100) NOT NULL,
        link        varchar(50) NOT NULL,
        Image_src   varchar(30) NOT NULL,
        teamID      integer NOT NULL,
        created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    """)
except:
  print("Projects table already exists. Not recreating it.")

print("Creating Teammates table")
try:
  cursor.execute("""
      CREATE TABLE Teammates (
        id          integer  AUTO_INCREMENT PRIMARY KEY,
        url         varchar(30) NOT NULL,
        teamID      integer NOT NULL,
        created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    """)
except:
  print("Teammates table already exists. Not recreating it.")

# Insert Records
print("inserting user")
query = "insert into Users (first_name, last_name, email, comment) values (%s, %s, %s, %s)"
values = [
  ('Stephen', 'Kim', 'sskim@ucsd.edu', 'This is my comment')
]
cursor.executemany(query, values)
db.commit()

print("inserting education")
query = "insert into Educations (school, degree, major, date) values (%s, %s, %s, %s)"
values = [
  ('University of California, San Diego', 'Bachelor', 'Electrical Engineering', 'March 2022')
]
cursor.executemany(query, values)
db.commit()

print("inserting Project")
query = "insert into Projects (title, description, link, Image_src, teamID) values (%s, %s, %s, %i)"
values = [
  ('ServiceUp', 'Community Posting Board for services', 'tbd', "/images/ServiceUp.png", 0)
]
cursor.executemany(query, values)
db.commit()

print("inserting teammates")
query = "insert into Teammates (url, teamID) values (%s, %i)"
values = [
  ('tbd',  0),
  ('tbd',  0),
  ('tbd',  0)
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Users;")
print('---------- DATABASE INITIALIZED ----------')
print("Users")
[print(x) for x in cursor]
db.commit()

cursor.execute("select * from Educations;")
print("Educations")
[print(x) for x in cursor]
db.commit()

cursor.execute("select * from Projects;")
print("Educations")
[print(x) for x in cursor]
db.commit()

cursor.execute("select * from Teammates;")
print("Educations")
[print(x) for x in cursor]
db.commit()

db.close()
