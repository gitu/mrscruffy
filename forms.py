import re

from wtforms import Form, TextAreaField, TextField, SelectField
from wtforms import validators as v
from wtforms import ValidationError
	
class IndexForm(Form):
    type = SelectField('Type', choices=[('dot','Dot File'),('tab','Table File')]);
    source = TextAreaField('Source', [v.Required()])