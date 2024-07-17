News Feed App
================

This is a Flask application that fetches real-time news feeds data from News API and displays it on a web page.

Setup
-----

1. Clone the repository && CD into the the Repo
2. Install the required packages: `pip install -r requirements.txt`
3. Create a `.env` file with your News API key: `NEWS_API_KEY=YOUR_NEWS_API_KEY`
4. Run the application: `python app/app.py`

Configuration
-------------

The application uses a `.env` file to store the News API key. You can add more configuration variables to this file as needed.

Code Structure
--------------

The code is organized into the following directories:

* `app/`: The main application code
* `models/`: Data models and API clients
* `templates/`: HTML templates for the web pages
* `static/`: Static assets (CSS, JS, images)
* `utils/`: Utility functions and configuration

License
-------

This application is licensed under the MIT License.