from flask import render_template, request, redirect
from models import db, Book

# ADD BOOK
def add_book():
    if request.method == "POST":
        book = Book(
            title=request.form['title'],
            author=request.form['author'],
            price=request.form['price']
        
        )
        db.session.add(book)
        db.session.commit()
        return redirect("/")
    return render_template("add_book.html")



# VIEW BOOKS
def view_books():
    books = Book.query.all()
    return render_template("view_books.html", books=books)

# DELETE BOOK
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

# EDIT BOOK
def edit_book(id):
    book = Book.query.get(id)

    if request.method == "POST":
        book.title = request.form['title']
        book.author = request.form['author']
        book.price = request.form['price']

        db.session.commit()
        return redirect("/")

    return render_template("edit_book.html", book=book)
