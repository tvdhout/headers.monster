import os
from flask import Flask, render_template


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SERVER_NAME'] = os.getenv('FQDN')


@app.route('/if')
@app.route('/')
def index():
    return render_template("homepage.html")
