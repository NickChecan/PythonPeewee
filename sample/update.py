from model.Author import Author
from model.Book import Book

def update():

    new_author = Author.get(Author.name == 'Nicholas Checan')
    book = Book.get(Book.title == "Clean Architecture")

    # Change the book author
    book.author = new_author
    book.save()
    
    print("Update: OK")