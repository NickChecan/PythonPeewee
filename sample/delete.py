from model.Book import Book

def delete():

    book = Book.get(Book.title == "Clean Code")
    book.delete_instance()
    
    print("Delete: OK")