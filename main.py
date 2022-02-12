import os

from flask import Flask, render_template, redirect, request, abort
from data.__all_models import *

from data import db_session


app = Flask(__name__)


@app.errorhandler(404)
def problem_404(e):
    return render_template("error404.html", title="Страница в разработке")


@app.route("/")
def main_page():
    # db_sess = db_session.create_session()
    # msls = db_sess.query(Category).all()
    return render_template("lending.html", title="ModernBMX: Главная")


@app.route("/exercises")
def exercises():
    return render_template("exercises.html", title="ModernBMX: Обучение")


if __name__ == '__main__':
    db_session.global_init("db/gym-bmx.db")
    db_sess = db_session.create_session()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
