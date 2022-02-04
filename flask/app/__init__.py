import os
from flask import Flask

from app.website import website_blueprint


app = Flask(__name__)
app.config['SERVER_NAME'] = os.getenv('FQDN')

app.register_blueprint(website_blueprint, subdomain='www')
