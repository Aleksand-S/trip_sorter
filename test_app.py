from app import app
from flask import json


def test_1():
    response = app.test_client().post(
        '/',
        data=json.dumps({
            "cards":
            [
            {"type": "airplane", "from": "NY", "to": "LA", "number": "flynum", "gate/platform": "gate1", "seat": "C5", "baggage_info": "baggage"},
            {"type": "bus", "from": "Jersey", "to": "NY", "number": "city bus", "gate/platform": "123", "seat": "23"},
            {"type": "train", "from": "LA", "to": "Village", "number": "TR123", "gate/platform": "B03", "seat": "16"},
            {"type": "bus", "from": "Boston", "to": "Jersey", "number": "1234", "gate/platform": "B03", "seat": "16"}
            ]
            }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['route_list'] == [
        "1. Take bus number '1234' from Boston to Jersey. Platform B03, seat 16.",
        "2. Take bus number 'city bus' from Jersey to NY. Platform 123, seat 23.",
        "3. Take airplane number 'flynum' from NY to LA. Gate gate1, seat C5.Baggage info: baggage.",
        "4. Take train number 'TR123' from LA to Village. Platform B03, seat 16."
    ]

def test_2():
    response = app.test_client().post(
        '/',
        data=json.dumps({
            "cards":
            [
            {"type":"airplane", "from":"NY", "to":"LA", "number":"flynum", "gate/platform":"gate1", "seat":"C5", "baggage_info":"baggage"},
            {"type":"bus", "from":"Jersey", "to":"NY", "number":"city bus", "gate/platform":"123", "seat":"23"},
            {"type":"train", "from":"LA", "to":"Village", "number":"TR123", "gate/platform":"B03", "seat":"16"},
            {"type":"bus", "from":"Boston", "to":"Jerse", "number":"1234", "gate/platform":"B03", "seat":"16"}
            ]
            }),
        content_type='application/json',
    )
    data = response.get_data(as_text=True)
    assert response.status_code == 400
    assert data == 'Error: the number of unique points FROM: 2. Should be 1'
