from app import app, db
from flask import render_template, request, redirect, url_for
from app.models.models import Film
from app.forms.film import FilmForm


@app.route('/films')
def index_films():
    films = Film.query.all()
    return render_template('films/index.html', films=films)


@app.route('/films/new', methods=['GET', 'POST'])
def new_film():
    form = FilmForm(request.form)
    if request.method == 'POST':
        film = Film(form)
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('index_films'))
    return render_template('films/new.html', form=form)


@app.route('/films/edit/<int:id>', methods=['GET', 'POST'])
def edit_films(id):
    film = Film.query.get(id)
    form = FilmForm(request.form, obj=film)
    if request.method == 'POST':
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('index_films'))
    return render_template('films/edit.html', form=form)


@app.route('/films/delete/<int:id>')
def delete_films(id):
    film = Film.query.get(id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('index_films'))
