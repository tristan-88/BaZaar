from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError


class ShopForm(FlaskForm):
    name = StringField('name')
    address = StringField('address')
    description = StringField('description')
