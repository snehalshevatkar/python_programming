from flask import Flask
from config import Config
from models import db

from controllers.book_controller import (add_book, view_books, delete_book, edit_book)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 

with app.app_context():
    db.create_all()

app.add_url_rule("/", "home", view_books)
app.add_url_rule("/add", "add", add_book, methods=["GET","POST"])
app.add_url_rule("/delete/<int:id>", "delete", delete_book)
app.add_url_rule("/edit/<int:id>", "edit", edit_book, methods=["GET","POST"])

app.run(debug=True)



