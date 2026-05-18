from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

with app.app_context():
    db.create_all()

    # Add books
    new_book = Book(title="Harry Potter", author="J.K Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

    # Read all books
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    print(all_books)

    # Read one book
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)

    # Update book rating
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.rating = 9.5
    db.session.commit()

    # Delete a book
    book_id = 1
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()

    print("Done!")