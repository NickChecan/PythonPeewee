from model.Author import Author
from model.Book import Book

def create():

    author_1 = Author.create(name = 'Robert Cecil Martin')
    author_2 = Author.create(name = 'Gary Gygax')
    author_3 = Author.create(name = 'Nicholas Checan')

    book_1 = {
        'title': 'Clean Architecture',
        'author_id': author_1,
    }

    book_2 = {
        'title': 'Clean Code',
        'author_id': author_1,
    }

    book_3 = {
        'title': 'Advanced Dungeons and Dragons',
        'author_id': author_2,
    }

    # Set an array of books and insert it into the database
    books = [book_1, book_2, book_3]
    Book.insert_many(books).execute()

    print("Create: OK")