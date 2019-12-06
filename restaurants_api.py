from flask import Flask, request
from restaurant_manager import RestaurantManager
from fast_food import FastFood
from fine_dining import FineDining
from datetime import datetime
import json

app = Flask(__name__)

restaurant_manager = RestaurantManager('restaurants.sqlite')

@app.route('/restaurantmanager/restaurants', methods=['POST'])
def add_restaurant():
    """adds restaurant to restaurant manager"""
    content = request.json
    try:
        if content['type'] == 'fast food':
            restaurant = FastFood(content['name'], content['num_employees'], content['location'],
                                  content['year_opened'], content['num_locations'], content['has_drivethrough'])
            restaurant.id = content['id']
            restaurant_manager.add(restaurant)
        else:
            restaurant = FineDining(content['name'], content['num_employees'], content['location'],
                                  content['year_opened'], content['num_michelin_stars'], content['chef_name'])
            restaurant.id = content['id']
            restaurant_manager.add(restaurant)
        response = app.response_class(
            status=200
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/restaurantmanager/restaurants/<int:id>', methods=['PUT'])
def update_restaurant(id):
    """updats existing restaurant"""
    content = request.json
    try:
        if content['type'] == 'fast food':
            restaurant = FastFood(content['name'], content['num_employees'], content['location'],
                                  content['year_opened'], content['num_locations'], content['has_drivethrough'])
            restaurant.id = id
            restaurant_manager.update(restaurant)
        else:
            restaurant = FineDining(content['name'], content['num_employees'], content['location'],
                                  content['year_opened'], content['num_michelin_stars'], content['chef_name'])
            restaurant.id = id
            restaurant_manager.update(restaurant)
        response = app.response_class(
            status=200
        )

    except Exception as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response

@app.route('/restaurantmanager/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    """delete existing restaurant"""
    try:
        restaurant_manager.delete(id)
        response = app.response_class(
            status=200
        )

    except Exception as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response

@app.route('/restaurantmanager/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    """return existing restaurant"""
    try:
        restaurant = restaurant_manager.get_restaurant_by_id(id)
        response = app.response_class(
            status=200,
            response=json.dumps(restaurant.to_dict()),
            mimetype='application/json'
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response

@app.route('/restaurantmanager/restaurants/all', methods=['GET'])
def get_all_restaurants():
    """return all restaurants"""
    try:
        restaurants = [ restaurant.to_dict() for restaurant in restaurant_manager.get_all() ]
        response = app.response_class(
            status=200,
            response=json.dumps(restaurants),
            mimetype='application/json'
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response

@app.route('/restaurantmanager/restaurants/all/<string:type>', methods=['GET'])
def get_all_restaurants_by_type(type):
    """return all restaurants by type"""
    try:
        restaurants = [ restaurant.to_dict() for restaurant in restaurant_manager.get_all_by_type(type) ]
        print(restaurants)
        response = app.response_class(
            status=200,
            response=json.dumps(restaurants),
            mimetype='application/json'
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/restaurantmanager/restaurants/stats', methods=['GET'])
def get_restaurant_stats():
    """return restaurants stats"""
    try:
        stats = restaurant_manager.get_restaurant_stats()
        stats_dict = {"total_num_restaurants": stats.get_total_num_restaurants(),
                      "num_fine_dining": stats.get_num_fine_dining(),
                      "num_fast_food": stats.get_num_fast_food(),
                      "avg_year_opened": stats.get_avg_year_opened()}

        response = app.response_class(
            status=200,
            response=json.dumps(stats_dict),
            mimetype='application/json'
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

if __name__ == "__main__":
    app.run()
