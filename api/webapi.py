import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

events = []
event_list = [
    "Jen Psaki, White House press secretary to Joe Biden, tests positive for Covid ",
    "The stench of death: California city plagued by extraordinary odor for weeks",
    "The anchor-outs: San Francisco’s bohemian boat dwellers fight for their way of life",
    "FBI failed to act on tips of likely violence ahead of Capitol attack – report",
    "Killed in seconds: why did the FBI shoot Jonathan Cortez in an Oakland corner store?",
    "Joe Biden dismisses bad polling and says domestic agenda set to pass",
    "Al Franken rules out Senate run against Gillibrand, who led push to remove him",
    "Republican Adam Kinzinger: I will fight Trumpism ‘cancer’ outside Congress",
    "The battle over a vast New York park: is this climate resilience or capitalism?",
    "Blinken clashes with China over US support for Taiwan",
    "Man dressed as Joker arrested after injuring 17 in Tokyo train attack",
    "Macron accuses Australian PM of lying over submarine deal",
    "Best bird a bat: tiny flying mammal wins New Zealand bird of the year competition",
    "There could be snakes: planes mothballed by Covid prepare to fly again",
    "UK Covid infections are at record levels, but cases may have peaked",
    "Did Vikings and their stowaway mice beat Portugal to the Azores?",
    "Revealed: the towns Harlow is at risk from far-right extremism",
    "American Airlines cancels around 1,600 flights due to weather and staff shortage",
    "Brazilian police kill 25 suspects allegedly part of bank robbery gang",
    "Covid live news: UK weekly cases down 13%; US sending more vaccines to Taiwan"
]

def _find_next_id():
    return max(events["id"] for event in events) + 1


def _init_events():
    id = 1
    for event in event_list:
        events.append({"id": id, "event": event, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/event')
def get_event():
    if len(events) == 0:
        _init_events()
    return jsonify(random.choice(events))


@api_bp.route('/events')
def get_events():
    if len(events) == 0:
        _init_events()
    return jsonify(events)

if __name__ == "__main__":
    print(random.choice(event_list))