# import "packages" from flask
from algorithms.image import image_data
from flask import Flask, render_template, request
from pathlib import Path
import requests
from newsapi.newsapi_client import NewsApiClient
from api.webapi import api_bp
from starter.starter import app_starter
import firebase_admin
from firebase_admin import credentials

# cred = credentials.Certificate("static/assets/the-forum-82bd6-firebase-adminsdk-4y6ls-6662d615ea.json")
# firebase_admin.initialize_app(cred)

# create a Flask instance
app = Flask(__name__)

thisList = []
# connects default URL to render index.html

yourAPIKEY = '8169dc4f99474483ab5999bc2c761381'  # write your API key here

newsapi = NewsApiClient(api_key=yourAPIKEY)


@app.route('/')
def index():
    # news =head_lines
    return render_template('index.html', news='')


@app.route('/results/', methods=['POST'])
def get_results():
    keyword = request.form['keyword']  # getting input from user

    news = newsapi.get_top_headlines(q=keyword,
                                     # sources='bbc-news,the-verge',#optional and you can change
                                     # category='business', #optional and you can change also
                                     language='en',  # optional and you can change also
                                     country='in')
    # print(news['articles'])
    return render_template('index.html', news=news['articles'])


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")


@app.route('/error/')
def error():
    return render_template("error.html")


@app.route('/national_events/')
def national_events():
    return render_template("pages/national_events.html")


# @app.route('/north_east/')
# def east_coast():
#     return render_template("pages/north_east.html")


# @app.route('/west/')
# def west_coast():
#     return render_template("pages/west.html")
#
#
# @app.route('/mid_west/')
# def mid_west():
#     return render_template("pages/mid_west.html")


@app.route('/international_events/')
def international_events():
    # news = {}
    news["NorthAmerica"] = newsapi.get_top_headlines(q="America")['articles']
    news["SouthAmerica"] = newsapi.get_top_headlines(q="South America")['articles']
    news["Asia"] = newsapi.get_top_headlines(q="China")['articles']
    news["Europe"]= newsapi.get_top_headlines(q="Europe")['articles']
    news["Africa"]= newsapi.get_top_headlines(q="Africa")['articles']
    news["Australia"] = newsapi.get_top_headlines(q="Zealand")['articles']
    news["Antarctica"] = newsapi.get_top_headlines(q="Antarctica")['articles']
    print(news['NorthAmerica'])
    return render_template("pages/international_events.html", news=news)


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.form:
        thought = request.form.get("thought")
        thisList.append(thought)
        if len(thought) != 0:
            return render_template("pages/international_events.html", nickname=thisList)
    return render_template("pages/international_events.html")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if len(thisList) > 0:
        thisList.pop(len(thisList) - 1)
    return render_template("pages/international_events.html", nickname=thisList)


@app.route('/science_news/')
def science_news():
    news = {}
    news["Health"] = newsapi.get_top_headlines(q="Health")['articles']
    news["Science"] = newsapi.get_top_headlines(q="Science")['articles']
    return render_template("pages/science_news.html", news=news)


@app.route('/west/')
def west():
    return render_template("pages/west.html")

@app.route('/mid_west/')
def mid_west():
    return render_template("pages/mid_west.html")

@app.route('/south_west/')
def south_west():
    return render_template("pages/south_west.html")

@app.route('/north_east/')
def north_east():
    return render_template("pages/north_east.html")

@app.route('/south_east/')
def south_east():
    return render_template("pages/south_east.html")

@app.route('/sports_news/')
def sports_news():
    return render_template("pages/sports_news.html")


@app.route('/most_popular/')
def most_popular():
    return render_template("pages/most_popular.html")


@app.route('/video_journal_0/')
def video_journal_0():
    return render_template("video_journal_0.html")


@app.route('/raiden/', methods=['GET', 'POST'])
def raiden():
    return render_template("profiles/raiden.html")


@app.route('/brian', methods=['GET', 'POST'])
def brian():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("profiles/brian.html", nickname=name)
    # starting and empty input default
    return render_template("profiles/brian.html", nickname="World")


@app.route('/Connor/', methods=['GET', 'POST'])
def connor():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("profiles/Connor.html", nickname=name)
    # starting and empty input default
    return render_template("profiles/Connor.html", nickname="World")


@app.route('/Jacob/', methods=['GET', 'Post'])
def Jacob():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("profiles/Jacob.html", nickname=name)
    # starting and empty input default
    return render_template("profiles/Jacob.html", nickname="World")


@app.route("/binary/", methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 7:  # input field has content
            return render_template("minilabs/binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("minilabs/binary.html", bits=8)


@app.route('/greet', methods=['GET', 'Post'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("minilabs/greet.html", name=name)
    # starting and empty input default
    return render_template("minilabs/greet.html", nickname="World")


@app.route('/rgb/', methods=['GET', 'POST'])
def rgb():
    path = Path(app.root_path) / "static" / "assets" / "images"
    return render_template('minilabs/rgb.html', images=image_data(path))


# runs the application on the development server

@app.route('/logicgates/')
def logicgates():
    return render_template('minilabs/logicgates.html')


@app.route("/morebinary/", methods=['GET', 'POST'])
def morebinary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 7:  # input field has content
            return render_template("minilabs/morebinary.html", bits=int(bits))
        # starting and empty input default
    return render_template("minilabs/morebinary.html", bits=8)


@app.route("/evenmorebinary/", methods=['GET', 'POST'])
def evenmorebinary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 7:  # input field has content
            return render_template("minilabs/evenmorebinary.html", bits=int(bits))
        # starting and empty input default
    return render_template("minilabs/evenmorebinary.html", bits=8)


@app.route("/colorcodes/", methods=['GET', 'POST'])
def colorcodes():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 7:  # input field has content
            return render_template("minilabs/colorcodes.html", bits=int(bits))
        # starting and empty input default
    return render_template("minilabs/colorcodes.html", bits=8)

app.register_blueprint(api_bp)
app.register_blueprint(app_starter)

if __name__ == "__main__":
    app.run(debug=True, port=5555)
