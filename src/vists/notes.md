Now we ware coonceting db to our application 
we do this by using Django models
Django Models
A Django model is like a blueprint for creating and managing data in a database. Instead of writing SQL queries, you define a Python class, and Django automatically creates a table for it in the database.
Key Points:
A model is just a Python class that represents a table in the database.
Each attribute in the class is a column in that table.
Django automatically handles database interactions, so you don’t need to write SQL.

Q1. What does Model mean in models.Model?
models.Model is a predefined Django class that gives your class database functionality.
When you write class Person(models.Model), you are telling Django that this class represents a database table.
It provides built-in functions to save, update, and delete data without writing SQL.
