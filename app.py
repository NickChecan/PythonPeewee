# -*- coding: utf-8 -*-
import peewee
from model.Author import Author
from model.Book import Book

# Samples - Test purpose
from sample.create import create
from sample.read import read
from sample.update import update
from sample.delete import delete

if __name__ == '__main__':
    
    try:
        Author.create_table()
        print("'Author' table successfully created!")
    except peewee.OperationalError:
        print("'Author' already exist!")

    try:
        Book.create_table()
        print("'Book' table successfully created!")
    except peewee.OperationalError:
        print("'Book' already exist!")

    create() # Example: Books and authors data creation
    
    read() # Example: Read books and authors

    update() # Example: Update a book register

    delete() # Example: Delete a book register