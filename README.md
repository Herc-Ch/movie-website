# Flask Movies Collection

## 🎬 Overview

This Flask web application allows users to manage a collection of movies. Users can add, edit, rate, and delete movies within their collection.

## 🚀 Prerequisites

1. Python 3.x
2. Install required Python packages using:

    ```bash
    python -m pip install -r requirements.txt
    ```

    On MacOS, use `pip3` instead of `pip`.
   
## 🌐 Data Scraping via APIs

Flask Movies Collection utilizes data scraping through The Movie Database (TMDb) API to provide detailed information about movies. This integration allows users to seamlessly add new movies to their collection by searching and fetching data from TMDb.

### 🔑 Key Points:

- **The Movie Database (TMDb):** The project leverages the TMDb API to retrieve information such as movie titles, release years, descriptions, and poster images.

### 🚨 Important Note:

Ensure compliance with [The Movie Database (TMDb) API terms of service](https://www.themoviedb.org/documentation/api/terms-of-use) while using this feature.

## 🛠️ Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Herc-Ch/movie-website.git
    ```

2. Navigate to the project folder:

    ```bash
    cd movie-website
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

## 🌐 Live Deployment

The live version of this application is accessible at [https://my-movies-website.onrender.com/](https://my-movies-website.onrender.com/).

## 🎥 Features

- View a list of movies with ratings and reviews.
- Edit the rating and review of each movie.
- Delete movies from the collection.
- Add new movies by searching The Movie Database (TMDb) API.

## 📂 Project Structure

1. `main.py`: The main application file.
2. `templates/`: HTML templates for rendering pages.
3. `static/`: Static files such as stylesheets and images.
4. `requirements.txt`: List of Python packages required for the project.
5. `.env`: Environment variables configuration file (create this file).

## 🤝 Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Follow the [GitHub flow](https://guides.github.com/introduction/flow/) when contributing.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)
