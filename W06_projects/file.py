with open("books.txt") as books_file:
    for book in books_file:
        print(book.strip())
