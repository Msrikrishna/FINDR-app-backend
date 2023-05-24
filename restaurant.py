import json

class Restaurant:
    def __init__(self, restaurant_id, name, coordinates, staked_amount):
        self.restaurant_id = restaurant_id
        self.name = name
        self.coordinates = coordinates
        self.staked_amount = staked_amount
        self.reviews = {}

    def update_staked_amount(self, staked_amount):
        self.staked_amount = staked_amount

    def add_review(self, review):
        self.reviews[review.review_hash] = review

    def __repr__(self):
        return json.dumps({
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "coordinates": self.coordinates,
            "staked_amount": self.staked_amount,
            "reviews": [review.__dict__ for review in self.reviews.values()]
        })


class Review:
    def __init__(self, review_hash, review_content, owner_info, restaurant_id):
        self.review_hash = review_hash
        self.review_content = review_content
        self.owner_info = owner_info
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return json.dumps(self.__dict__)


class Staker:
    def __init__(self, staked_amount, restaurant_id, staked_rewards):
        self.staked_amount = staked_amount
        self.restaurant_id = restaurant_id
        self.staked_rewards = staked_rewards

    def __repr__(self):
        return json.dumps(self.__dict__)

