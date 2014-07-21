import re

from flask import Flask
from flask import request
from flask import render_template
from flask import flash

from forms import IndexForm

app = Flask(__name__)
app.config.update(config)

@app.route('/', methods=['POST', 'GET'])
def index():
    form = IndexForm(request.form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)