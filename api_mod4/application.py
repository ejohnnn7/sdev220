from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} ({self.publisher})"

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify({
        "books": [
            {
                "id": b.id,
                "book_name": b.book_name,
                "author": b.author,
                "publisher": b.publisher
            } for b in books
        ]
    })

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        "id": book.id,
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    })

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    new_book = Book(
        book_name=data["book_name"],
        author=data["author"],
        publisher=data["publisher"]
    )
    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book created", "id": new_book.id}), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.book_name = data["book_name"]
    book.author = data["author"]
    book.publisher = data["publisher"]

    db.session.commit()
    return jsonify({"message": "Book updated"}), 200

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
