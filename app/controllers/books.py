from app import app, db
from flask import render_template, request, redirect, url_for
from app.models.models import Book
from app.forms.book import BookForm


@app.route('/books')
def index_books():
    books = Book.query.all()
    return render_template('books/index.html', books=books)


@app.route('/books/new', methods=['GET','POST'])
def new_book():
    form = BookForm(request.form)
    if request.method == 'POST':
        book = Book(form)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index_books'))
    return render_template('books/new.html', form=form)


@app.route('/books/edit/<int:id>', methods=['GET','POST'])
def edit_books(id):
    book = Book.query.get(id)
    form = BookForm(request.form, obj=book)
    if request.method == 'POST':
        form.populate_obj(book)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index_books'))
    return render_template('books/edit.html', form=form)


@app.route('/books/delete/<int:id>')
def delete_books(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index_books'))