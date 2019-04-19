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

@app.route('/restaurants/<int:restaurant_id>/edit/')
def restaurantEdit(restaurant_id):
    message = ''


# Task1: Create route for newMenuItem
@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return 'Page to create a new menu item.  Task 1 completed'


# Task2: Create route for editMenuItem
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'Page to edit a new menu item.  Task 2 completed'

# Task3: Create a route for deleteMenuItem
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'Page to delete a menu item.  Task 3 completed'



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
