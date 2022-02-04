from flask import Blueprint, render_template

website_blueprint = Blueprint('website', __name__, template_folder='templates', static_folder='static')


@website_blueprint.route('/')
def index():
    print("INDEX!!")
    return render_template("homepage.html")

print("LOADED ROUTES")