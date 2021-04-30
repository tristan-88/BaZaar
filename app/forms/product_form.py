from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    store_id = IntegerField('storeId')
    price = StringField('price', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
