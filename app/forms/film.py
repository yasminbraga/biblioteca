from flask_wtf import FlaskForm
from wtforms import fields, validators


class FilmForm(FlaskForm):
    name = fields.StringField('Name', validators=[validators.DataRequired()])
    year = fields.IntegerField('Year', validators=[validators.DataRequired()])
    genre = fields.StringField('Genre', validators=[validators.DataRequired()])
    status = fields.BooleanField('Status', default="checked")