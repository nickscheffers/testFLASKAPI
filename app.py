from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #turn off flask tracker, while sqlalchemy has better tracker
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # creates path /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__': #zorgt ervoor dat dit alleen runt als je deze file direct runt
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

#401 unauth
#404 api error
#400 bad request
#200 succes
#201 succes get
#500 internal server error

#runnen:
#gewoon draaien python script

#venv
#ga naar folder, maak hierin folder met code, boven folder met code doe:
#virtualenv venv --python=python3.6
#source venv/bin/activate
