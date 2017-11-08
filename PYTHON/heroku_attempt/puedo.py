import os
from flask import Flask

puedo = Flask(__name__)

@puedo.route('/')
def logrando_heroku():
    return "Hell yeah EGON!!!!!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)