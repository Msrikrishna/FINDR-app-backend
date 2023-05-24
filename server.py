from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
from flask_parameter_validation import ValidateParameters, Route, Json, Query
from restaurant import Restaurant, Review

app = Flask(__name__)
cors = CORS(app)

restaurant_one = Restaurant(1, "restaurant_one", 12345, 0)
restaurant_two = Restaurant(2, "restaurant_two", 12345, 0)
restaurant_three = Restaurant(3, "restaurant_three", 12345, 0)
restaurant_four = Restaurant(4, "restaurant_four", 12345, 0)
restaurant_five = Restaurant(5, "restaurant_five", 12345, 0)

restaurants = {
    str(restaurant_one.restaurant_id): restaurant_one,
    str(restaurant_two.restaurant_id): restaurant_two,
    str(restaurant_three.restaurant_id): restaurant_three,
    str(restaurant_four.restaurant_id): restaurant_four,
    str(restaurant_five.restaurant_id): restaurant_five,
}

reviews = {}


@app.route('/ping', methods={'GET'})
def ping():
    return "pong"


@app.route('/v1/review-submit', methods={'POST'})
def review_submit():
    data = request.json

    try:
        review_hash = data['reviewHash']
        review_content = data['reviewContent']
        owner_info = data['ownerInfo']
        restaurant_id = data['restaurantId']
    except:
        return "Missing parameters from request object."

    save_review_to_db(review_hash, review_content, owner_info, restaurant_id)
    return "OK"


@app.route('/v1/review-from-hashes', methods={'GET'})
def review_from_hashes():
    data = request.json

    try:
        restaurant_id = data['restaurantId']
    except:
        return "Missing parameters from request object."

    restaurant = get_restaurant_reviews_from_db(restaurant_id)
    print(restaurant)
    return repr(restaurant)


@app.route('/v1/stake/all-restaurants-near-me', methods={'GET'})
def all_restaurants_near_me():
    data = request.json

    try:
        location_info = data['locationInfo']
    except:
        return "Missing parameters from request object."

    restaurants_json = json.dumps(convert_to_json(restaurants), cls=CustomEncoder, indent=4)
    print(restaurants_json)
    return restaurants_json


@app.route('/v1/stake/info', methods={'GET'})
def user_info():
    data = request.json

    try:
        owner_info = data['ownerInfo']
    except:
        return "Missing parameters from request object."

    # if owner_info not in reviews:
    #     return {}
    return {}


@app.route('/v1/ai/submit-judgement', methods={'POST'})
def submit_judgement():
    data = request.json
    print(data)

    review_hash = ""

    try:
        review_hash = data['reviewHash']
    except:
        return "Missing parameters from request object."

    return get_score_from_ai_model(review_hash)


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Review):
            return obj.__dict__
        return super().default(obj)


def convert_to_json(obj):
    if isinstance(obj, dict):
        converted_dict = {}
        for key, value in obj.items():
            converted_dict[key] = convert_to_json(value)
        return converted_dict
    elif isinstance(obj, list):
        converted_list = []
        for item in obj:
            converted_list.append(convert_to_json(item))
        return converted_list
    elif isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    else:
        return obj.__dict__


def save_review_to_db(review_hash, review_content, owner_info, restaurant_id):
    review = Review(review_hash, review_content, owner_info, restaurant_id)
    if review.owner_info not in reviews:
        reviews[str(review.owner_info)] = []
    reviews[str(review.owner_info)].append(repr(review))
    restaurant = restaurants[restaurant_id]
    restaurant.add_review(review)
    print(restaurants)
    print(reviews)


def get_restaurant_reviews_from_db(restaurant_id):
    return restaurants[restaurant_id]


def get_from_google_maps(location_info) -> list:
    return []


def process_restaurants_with_staked_amount(restaurants) -> list:
    return []


def get_score_from_ai_model(review_hash):
    pass


if __name__ == "__main__":
    app.run(debug=True)
