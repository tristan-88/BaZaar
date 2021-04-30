from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class PhotoForm(FlaskForm):
    product_id = IntegerField('product_id')
    store_id = IntegerField('store_id')
