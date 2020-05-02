# TRIP SORTER (API)
Compiles an ordered route list based on boarding passes.

## Getting Started
Used Python version 3.7.5

1. Clone Project
        ```
        git clone https://github.com/Aleksand-S/trip_sorter.git
        ```
2. Install Python requirments: 
        ```
        pip install requirements.txt
        ```

To run the application use: 
        ```
        python3 app.py
        ```
(default port is 5000).
 
## Tests running
Tests are in **test_app.py**

To use tests you need to install pytest: 
    ```
    pip install pytest
    ```
    
To run tests use command: 
    ```
    pytest
    ```
## How to use
**Request requirements:**
- there must be one unique point 'FROM', one unique point 'TO' and all other points must have a pair
- a point cannot be repeated (e.g. Boston > ~~**NY**~~ > LA > ~~**NY**~~ > Detroit )
- fields "type", "from", "to", "number" and 'gate/platform' are required.
- request and response format (in case of code 200) is JSON


**Request example:**
```
{"cards": [
{"type":"airplane", "from":"NY", "to":"LA", "number":"flynum", "gate/platform":"gate1", "seat":"C5", "baggage_info":"baggage"},
{"type":"bus", "from":"Jersey", "to":"NY", "number":"city bus", "gate/platform":"123", "seat":"23"},
{"type":"train", "from":"LA", "to":"Village", "number":"TR123", "gate/platform":"B03", "seat":"16"},
{"type":"bus", "from":"Boston", "to":"Jersey", "number":"1234", "gate/platform":"B03", "seat":"16"}
]}
```
**Response example:**
```
{"route_list": [
    "1. Take bus number '1234' from Boston to Jersey. Platform B03, seat 16.", 
    "2. Take bus number 'city bus' from Jersey to NY. Platform 123, seat 23.", 
    "3. Take airplane number 'flynum' from NY to LA. Gate gate1, seat C5.Baggage info: baggage.", 
    "4. Take train number 'TR123' from LA to Village. Platform B03, seat 16."
]}
```