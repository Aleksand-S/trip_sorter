from flask import Flask, request, jsonify


# Init app
app = Flask(__name__)


def cards_sorter(cards):
    ordered = [cards[0]]
    cards.remove(cards[0])

    while len(cards) != 0:
        for card in cards:
            point_from = card['from']
            point_to = card['to']

            if ordered[-1]['to'] == point_from:
                ordered.append(card)
                cards.remove(card)
            elif ordered[0]['from'] == point_to:
                ordered.insert(0, card)
                cards.remove(card)

    return ordered


def request_check(cards):
    """
    the function checks for:
    1. There must be one unique point 'from', one unique point 'to', all other points must have a pair
    2. A point cannot be repeated
    3. Fields "type", "from", "to" and "number" are required.
    :param cards: list of dicts with data about boarding card
    :return: 'Correct' or error message
    """
    point_from = []
    point_to = []
    for card in cards:
        point_from.append(card['from'])
        point_to.append(card['to'])
        try:
            if card['type'] == '' or card['from'] == '' or card['to'] == '' or\
               card['number'] == '' or card['gate/platform'] == '':
                return 'Error: fields "type", "from", "to", "number", "gate/platform" are required'
        except KeyError:
            return 'Error: fields "type", "from", "to" and "number" are required'
    if len(point_from) != len(set(point_from)):
        return "Error: duplicate point FROM"
    if len(point_to) != len(set(point_to)):
        return "Error: duplicate point TO"
    uniq_from = len(set(point_from) - set(point_to))
    if uniq_from != 1:
        return "Error: the number of unique points FROM: {}. Should be 1".format(uniq_from)
    uniq_to = len(set(point_to) - set(point_from))
    if uniq_to != 1:
        return "Error: the number of unique points TO: {}. Should be 1".format(uniq_from)
    return 'Correct'


def list_creator(ordered_cards):
    route_list = []
    for num, card in enumerate(ordered_cards):
        info = "{}. Take {} number '{}' from {} to {}.".format(num+1, card['type'], card['number'], card['from'], card['to'])
        dep_place = 'Platform'
        if card["type"] == 'airplane':
            dep_place = 'Gate'
        seat_num = 'no assignment'
        try:
            if card['seat'] != '':
                seat_num = card['seat']
        except KeyError:
            pass
        info += " {} {}, seat {}.".format(dep_place, card['gate/platform'], seat_num)
        try:
            if card['baggage_info'] != '':
                info += "Baggage info: {}.".format(card['baggage_info'])
        except KeyError:
            pass
        route_list.append(info)
    return route_list


@app.route('/', methods=['POST'])
def route_creation():
    cards = request.json['cards']
    cards_check = request_check(cards)
    if cards_check == 'Correct':
        ordered_cards = cards_sorter(cards)
        return jsonify({'route_list': list_creator(ordered_cards)})
    else:
        return cards_check, 400


# Run Server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
