import requests
from flask import Blueprint, render_template
# from algorithm.image import image_data

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets')

@app_starter.route('/event', methods=['GET', 'POST'])
def event():
    # use this url to test and make modifications on your own machine
    url = "http://127.0.0.1:5555/api/event"

    # url = "https://csp.nighthawkcodingsociety.com/api/event"
    response = requests.request("GET", url)
    return render_template("starter/event.html", event=response.json())


@app_starter.route('/events', methods=['GET', 'POST'])
def events():
    # use this url to test and make modifications on your own machine
    url = "http://127.0.0.1:5555/api/events"

    # url = "https://csp.nighthawkcodingsociety.com/api/events"

    response = requests.request("GET", url)
    return render_template("starter/events.html", events=response.json())
