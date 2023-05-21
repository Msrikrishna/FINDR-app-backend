from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
from flask_parameter_validation import ValidateParameters, Route, Json, Query

app = Flask(__name__)
cors = CORS(app)


@app.route('/ping', methods={'GET'})
def ping():
    return "pong"


@app.route('/v1/review-submit', methods={'POST'})
def review_submit():
    data = request.json
    print(data)

    review_hash = ""
    review_content = ""
    owner_info = ""
    restaurant_id = ""

    try:
        review_hash = data['reviewHash']
        review_content = data['reviewContent']
        owner_info = data['ownerInfo']
        restaurant_id = data['restaurantId']
    except:
        return "Missing parameters from request object."

    save_review_to_db(review_hash, review_content, owner_info, restaurant_id)

    processed_hash = ""

    return processed_hash


@app.route('/v1/review-from-hashes', methods={'GET'})
def review_from_hashes():
    data = request.json
    print(data)

    review_hashes = []
    restaurant_id = ""

    try:
        review_hashes = data['reviewHashes']
        restaurant_id = data['restaurantId']
    except:
        return "Missing parameters from request object."

    return get_restaurant_reviews_from_db(restaurant_id, review_hashes)


@app.route('/v1/stake/all-restaurants-near-me', methods={'GET'})
def all_restaurants_near_me():
    data = request.json
    print(data)

    location_info = []

    try:
        location_info = data['locationInfo']
    except:
        return "Missing parameters from request object."

    restaurants = get_from_google_maps(location_info)

    return process_restaurants_with_staked_amount(restaurants)


@app.route('/v1/stake/info', methods={'GET'})
def user_info():
    data = request.json
    print(data)

    owner_info = ""

    try:
        owner_info = data['ownerInfo']
    except:
        return "Missing parameters from request object."

    return get_owner_info_from_db(owner_info)


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


def save_review_to_db(review_hash, review_content, owner_info, restaurant_id):
    return


def get_restaurant_reviews_from_db(restaurant_id, review_hashes) -> list:
    return []


def get_from_google_maps(location_info) -> list:
    return []


def process_restaurants_with_staked_amount(restaurants) -> list:
    return []


def get_owner_info_from_db(owner_info) -> list:
    return []


def get_score_from_ai_model(review_hash):
    pass

if __name__ == "__main__":
    app.run(debug=True)
