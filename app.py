from flask import Flask, request, jsonify, render_template
from flask_humanize import Humanize

from lib.requestHelper import requestHelper

app = Flask(__name__, template_folder="templates")
humanize = Humanize(app)


@humanize.localeselector
def get_locale():
    return 'id_ID'


@app.route("/")
def index():
    request_helper = requestHelper()
    data = request_helper.get_count()
    return render_template(
        "index.html",
        data_paslon=data["data_paslon"],
        data_chart=data["chart"],
        data_table=data["data"],
        data_last_updated=data["last_updated"],
        data_progres=data["progres"],

    )
