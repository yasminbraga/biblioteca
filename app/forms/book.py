from flask_wtf import FlaskForm
from wtforms import fields, validators


class BookForm(FlaskForm):
    name = fields.StringField('Name', validators=[validators.DataRequired()])
    author = fields.StringField('Author', validators=[validators.DataRequired()])
    genre = fields.StringField('Genre', validators=[validators.DataRequired()])
    status = fields.BooleanField('Status', default="checked")