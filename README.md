# Flask Movies Collection

## Overview

This Flask web application allows users to manage a collection of movies. Users can add, edit, rate, and delete movies within their collection.

## Prerequisites

1. Python 3.x
2. Install required Python packages using:

    ```bash
    python -m pip install -r requirements.txt
    ```

    On MacOS, use `pip3` instead of `pip`.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-movies-collection.git
    ```

2. Navigate to the project folder:

    ```bash
    cd flask-movies-collection
    ```

3. Install dependencies:

    ```bash
    python -m pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

    The application will start, and you can access it at [http://localhost:5000](http://localhost:5000).

## Live Deployment

The live version of this application is accessible at [https://my-movies-website.onrender.com/](https://my-movies-website.onrender.com/).

## Features

- View a list of movies with ratings and reviews.
- Edit the rating and review of each movie.
- Delete movies from the collection.
- Add new movies by searching The Movie Database (TMDb) API.

## Project Structure

1. `main.py`: The main application file.
2. `templates/`: HTML templates for rendering pages.
3. `static/`: Static files such as stylesheets and images.
4. `requirements.txt`: List of Python packages required for the project.
5. `.env`: Environment variables configuration file (create this file).

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Follow the [GitHub flow](https://guides.github.com/introduction/flow/) when contributing.


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)
