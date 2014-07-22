import re

from flask import Flask
from flask import request
from flask import render_template
from flask import flash

from forms import IndexForm
from config import config

app = Flask(__name__)
app.config.update(config)

@app.route('/', methods=['GET'])
def index():
    form = IndexForm(request.form)
    return render_template('index.html', form=form)
	
	
@app.route('/', methods=['POST'])
def parse():
    form = IndexForm(request.form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
