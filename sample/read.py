from model.Author import Author
from model.Book import Book

def read():
    
    book = Book.get(Book.title == 'Advanced Dungeons and Dragons')
    print(book.title)

    books = Book.select().join(Author).where(Author.name == 'Robert Cecil Martin')

    # Display the quantity of registers found in the search process
    print(books.count())

    for book in books:
        print(book.title)