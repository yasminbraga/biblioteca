from app import app, db
from flask import render_template, request, redirect, url_for
from app.models.models import Series
from app.forms.series import SeriesForm


@app.route('/series')
def index_series():
    series = Series.query.all()
    return render_template('series/index.html', series=series)


@app.route('/series/new', methods=["GET", "POST"])
def new_series():
    form = SeriesForm(request.form)
    if request.method == "POST":
        series = Series(form)
        db.session.add(series)
        db.session.commit()
        return redirect(url_for("index_series"))
    return render_template("series/new.html", form=form)



@app.route('/series/edit/<int:id>', methods=["GET", "POST"])
def edit_series(id):
    series = Series.query.get(id)
    form = SeriesForm(request.form, obj=series)
    if request.method == "POST":
        db.session.add(series)
        db.session.commit()
        return redirect(url_for('index_series'))
    return render_template('series/edit.html', form=form)


@app.route('/series/delete/<int:id>')
def delete_series(id):
    series = Series.query.get(id)
    db.session.delete(series)
    db.session.commit()
    return redirect(url_for('index_series'))
