import json
from flask import Flask, request
import pdb

app = Flask(__name__)

@app.route('/familia')
def home():
    pdb.set_trace()
    persons = [
        {
            "name": "Mirva", 'age': 54
        },
        {
            "name": "Yurac", 'age': 25
        }
    ]
    
    json_person = json.dumps(persons)
    return (json_person, 200, None)

@app.route('/mascotas')
def mascota():
    pdb.set_trace()
    person = {"name": "Oliver", 'age': 3}
    json_person = json.dumps(person)
    return (json_person, 200, None)

if __name__ == '__main__':
    app1.run()