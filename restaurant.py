"""
Flask application with DB & Links
"""
from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    message = ''
    for i in items:
        message += i.name
        message += '<br/>'
        message += i.price
        message += '<br/>'
        message += i.description
        message += '<br/><br/>'
    return message


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
