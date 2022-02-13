import os
import shutil

from flask import Flask, render_template, redirect, request, abort, url_for
from data.__all_models import *

from data import db_session


app = Flask(__name__)


@app.errorhandler(404)
def problem_404(e):
    return render_template("error404.html", title="ModernBMX|Страница в разработке")


@app.route("/")
def main_page():
    return render_template("lending.html", title="ModernBMX|Главная")


@app.route("/exercises")
def exercises():
    db_sess = db_session.create_session()
    articles = db_sess.query(Article).filter(Article.category_type == 1)
    res = []
    for article in articles:
        photo_flag = "0.png" in os.listdir(f"static/img/articles/{article.id}/")
        name_author = db_sess.query(User).filter(User.id == article.author).first().name
        tag = db_sess.query(Category).filter(Category.id == article.category_tag).first().name
        res.append([photo_flag, name_author, article, tag])
    return render_template("exercises.html", title="ModernBMX|Обучение", articles=res)


@app.route("/news")
def news():
    db_sess = db_session.create_session()
    articles = db_sess.query(Article).filter(Article.category_type == 2)
    res = []
    for article in articles:
        photo_flag = "0.png" in os.listdir(f"static/img/articles/{article.id}/")
        res.append([photo_flag, article])
    return render_template("news.html", title="ModernBMX|Новости", articles=res)


@app.route("/tips")
def tips():
    db_sess = db_session.create_session()
    articles = db_sess.query(Article).filter(Article.category_type == 3)
    res = []
    for article in articles:
        photo_flag = "0.png" in os.listdir(f"static/img/articles/{article.id}/")
        res.append([photo_flag, article])
    return render_template("tips.html", title="ModernBMX|Полезные статьи", articles=res)


@app.route("/article/<id_>")
def article(id_):
    db_sess = db_session.create_session()
    article = db_sess.query(Article).filter(Article.id == id_).first()
    author = db_sess.query(User).filter(User.id == article.author).first()
    photos = os.listdir(f"static/img/articles/{article.id}/")
    return render_template("article.html", title=article.name, article=article, author=author, photos=photos)


@app.route('/create', methods=['GET', 'POST'])
def article_create():
    db_sess = db_session.create_session()
    tags = db_sess.query(Category).all()
    types = db_sess.query(ArticleType).all()

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        text = request.form.get('text')
        category = request.form.get('category')
        type_ = request.form.get('type_')

        photos = request.files.getlist('photo')
        if len(photos) > 8:
            return render_template("make_article.html", title="ModernBMX|Создать статью",
                                   alert="Слишком много фото (максимум 8)", tags=tags, types=types)

        db_sess = db_session.create_session()
        article = Article(
            name=name,
            description=description,
            text=text,
            category_tag=category,
            category_type=type_,
            author=1
        )
        db_sess.add(article)
        db_sess.commit()
        os.mkdir(f"static/img/articles/{article.id}")
        if photos:
            photo_num = -1
            for photo in photos:
                photo_num += 1
                if photo.filename != '':
                    photo.save(f"static/img/articles/{article.id}/{photo_num}.png")
        return redirect(url_for('article_create'))

    return render_template("make_article.html", title="ModernBMX|Создать статью", alert="", tags=tags, types=types)


@app.route("/delete")
def article_delete():
    db_sess = db_session.create_session()
    articles = db_sess.query(Article).all()

    if request.method == 'POST':
        id_ = request.form.get('id_')
        art = db_sess.query(Article).filter(Article.id == id_).delete()
        shutil.rmtree(f"static/img/articles/{id_}")
        return redirect(url_for('article_delete'))

    return render_template("delete_article.html", title="ModernBMX|Удалить статью", alert="", articles=articles)


if __name__ == '__main__':
    db_session.global_init("db/gym-bmx.db")
    db_sess = db_session.create_session()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
