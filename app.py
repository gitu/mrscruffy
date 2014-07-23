import re
import subprocess

from flask import Flask
from flask import request
from flask import render_template

import scruffy

from forms import IndexForm
from config import config
import StringIO

app = Flask(__name__)
app.config.update(config)


@app.route('/', methods=['GET'])
def index():
    form = IndexForm(request.form)
    return render_template('index.html', form=form)


@app.route('/', methods=['POST'])
def parse():
    form = IndexForm(request.form)
    options = dict(font=None, shadow=None, png=None)
    if form.validate():
        fout = StringIO.StringIO()
        fin = form.data['source']
        svg = subprocess.Popen(['dot', '-Tsvg'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(input=fin)[0]
        scruffy.transform(svg, fout, options)
        return fout.getvalue()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
