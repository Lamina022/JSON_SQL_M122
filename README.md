JSON to mysql Project M122
==========================

Autor:          Lisa Wuethrich
Start Date:     14.08.2020
Project Name:   Py-Proj (JSON to mysql project M122)
Responsible:    Alexis Winiger
Languages:      Python 3, JSON and SQL



General Goal of the Project:
============================
Creating a Project in Python 3, which reads information from a JSON file, 
saves the path to that file in one database table using sqlite and saving the content of the file in a sub-table.


Steps:
======
- creating code, which reads JSON from a file and prints it 
- creating a database using mysql
- saving a files path to a database
- extending the code, so it reads a JSON file and separates the values from the datatypes
- writing the program, so it saves that data into the database 
- testing the program and bugfixing


Tables:
=======
------------------------------------------      ----------------------------------------------------
|               Filepath                 |      |                     Index                        |
|----------------------------------------|      |--------------------------------------------------|
|Path                        |   ID      |      |Value  |   NUM |   BOOL    |   STRING  |   NULL   |
|----------------------------|-----------|      |--------------------------------------------------|
|                            |           |      |       |       |           |           |          |
------------------------------------------      ----------------------------------------------------