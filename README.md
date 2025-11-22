# CST 1510 Coursework 2 - CST1510 — Multi-Domain Intelligence Platform
Week 8: Data Pipeline & CRUD (SQL)

Student Name: Madiyar
Student ID: M01033592

The project Intelligence Platform.
The project creates databases, loads csv and txt data, then demonstrates analysis results.

## Project Structure
 
app/
    data/
        db.py
        schema.py
        users.py
        incidents.py
        datasets.py
        tickets.py
    services/
        user_services.py
        __init__.py
DATA/
    cyber_incidents.csv
    datasets_metadata.csv
    intelligence_platform.db
    it_tickets.csv
    users.txt

main.py
README.md
requirements.txt

## What the project does

Creates the database file "intelligence_platform.db".
Creates three tables: users, cyber_incidents, and it_tickets.
Loads all data from CSV and TXT files into the database.
Imports users from the file users.txt
Test registration and login
Reads data from the tables

## How to run the project

1. Run main.py

## What it will do after running 

Create the database 
Create tables 
Load CSV data
Import users 
Test login






