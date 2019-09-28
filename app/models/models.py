from app import db


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, default=False, server_default="false")

    def __init__(self,form):
        self.name = form.name.data
        self.author = form.author.data
        self.genre = form.genre.data
        self.status = form.status.data


class Film(db.Model):
    __tablename__ = 'film'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String)
    status = db.Column(db.Boolean)

    def __init__(self, form):
        self.name = form.name.data
        self.year = form.year.data
        self.genre = form.genre.data
        self.status = form.status.data


class Series(db.Model):
    __tablename__ = 'series'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String)
    seasons = db.Column(db.Integer)
    status = db.Column(db.Boolean)

    def __init__(self, form):
        self.name = form.name.data
        self.year = form.year.data
        self.genre = form.genre.data
        self.seasons = form.seasons.data
        self.status = form.status.data
