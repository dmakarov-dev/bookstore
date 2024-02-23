# bookstore.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (you would typically use a real database like SQLite or MongoDB)
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    # Add more books as needed
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def view_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return render_template('book.html', book=book)
    return "Book not found"

if __name__ == '__main__':
    app.run(debug=True)
