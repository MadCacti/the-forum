# import "packages" from flask
from flask import Flask, render_template, request
from algorithms.image import image_data

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/national_events/')
def national_events():
    return render_template("national_events.html")

@app.route('/international_events/')
def international_events():
    return render_template("international_events.html")

@app.route('/science_news/')
def science_news():
    return render_template("science_news.html")

@app.route('/sports_news/')
def sports_news():
    return render_template("sports_news.html")

@app.route('/most_popular/')
def most_popular():
    return render_template("most_popular.html")

@app.route('/video_journal_0/')
def video_journal_0():
    return render_template("video_journal_0.html")

@app.route('/raiden/', methods=['GET', 'POST'])
def raiden():
    # submit button has been pushed
    if request.form:
        namer = request.form.get("name")
        if len(namer) != 0:  # input field has content
            return render_template("raiden.html", funnyname=namer)
    # starting and empty input default
    return render_template("raiden.html", funnyname="World")


@app.route('/brian', methods=['GET', 'POST'])
def brian():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("brian.html", nickname=name)
    # starting and empty input default
    return render_template("brian.html", nickname="World")

@app.route('/Connor/', methods=['GET', 'POST'])
def connor():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Connor.html", nickname=name)
    # starting and empty input default
    return render_template("Connor.html", nickname="World")

@app.route('/Jacob/', methods=['GET', 'Post'])
def Jacob():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Jacob.html", nickname=name)
    # starting and empty input default
    return render_template("Jacob.html", nickname="World")

@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 7:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)

@app.route('/greet', methods=['GET', 'Post'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", nickname=name)
    # starting and empty input default
    return render_template("greet.html", nickname="World")

@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    rawList = image_data()
    colorList = []
    grayList = []
    for img in rawList:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])

    return render_template('rgb.html', images=rawList, colored=colorList, grayed=grayList)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
