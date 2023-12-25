import os

import psycopg2
import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DB_URI", "sqlite:///movies-collection.db"
)
app.config["SECRET_KEY"] = os.getenv("FLASK_KEY")
Bootstrap5(app)
# initialize the app with the extension
db.init_app(app)


# inherits from db.Model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    # Retrieve the book ID from the query parameters (book is defined a loop element and id=book.id to get the arg)
    movie_id = request.args.get("id")
    # Get the corresponding book from the database or return a 404 error if not found
    movie_to_delete = db.get_or_404(Movie, movie_id)
    # Delete the book from the database
    db.session.delete(movie_to_delete)
    # Commit the changes to the database
    db.session.commit()
    # Redirect the user to the home page after deleting the book
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()

    if form.validate_on_submit():
        movie_title = form.title.data
        movie_title = movie_title.replace(" ", "%20")
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NTQ2MDBjZTI1MzEwNGJlMzYzOWZhZTg0OGE5NzMyOCIsInN1YiI6IjY1Nzc0NDU4NTY0ZWM3MDExYjIwMjJkZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zrqz9yDrIXqORNoUjdDc48GMq7z34bUsY6FQJz39c4g",
        }
        response = requests.get(url, headers=headers)
        titles = response.json()["results"]

        return render_template("select.html", titles=titles)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_api_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NTQ2MDBjZTI1MzEwNGJlMzYzOWZhZTg0OGE5NzMyOCIsInN1YiI6IjY1Nzc0NDU4NTY0ZWM3MDExYjIwMjJkZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zrqz9yDrIXqORNoUjdDc48GMq7z34bUsY6FQJz39c4g",
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=int(data["release_date"][:4]),
            img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
            description=data["overview"],
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=False)
