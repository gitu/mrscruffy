import re

from wtforms import Form, TextAreaField, TextField, SelectField
from wtforms import validators as v
from wtforms import ValidationError


class IndexForm(Form):
    type = SelectField('Type', choices=[('png','PNG'),('svg','SVG')]);
    source = TextAreaField('Source', [v.Required()])