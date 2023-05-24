# FINDR-app-backend
FINDR is a blockchain/ AI powered review app which gamifies the restaurant review process and offers incentives for the restaurant goers, reviewers and anyone who are generally interested in this space


### Running locally

#### Install packages: 
`pip install -r requirements.txt`
#### Run app: 
`python3 server.py` (Replace python3 with your python path if you do not use `python3` to start up a python terminal)

### Endpoints

### Endpoint 1: `http://127.0.0.1:5000/v1/review-submit`
#### Request:
```commandline
{
    "reviewHash" : "cde",
    "reviewContent" : "This is the second review",
    "ownerInfo": "test_user_2",
    "restaurantId": "1"
}
```

#### Response:
```commandline
OK
```

### Endpoint 2: `http://127.0.0.1:5000/v1/review-from-hashes`
#### Request:
```commandline
{
    "restaurantId":"1"
}
```

#### Response:
```commandline
{
  "restaurant_id": 1,
  "name": "restaurant_one",
  "coordinates": 12345,
  "staked_amount": 0,
  "reviews": [
    {
      "review_hash": "cde",
      "review_content": "This is the second review",
      "owner_info": "test_user_2",
      "restaurant_id": "1"
    }
  ]
}
```

### Endpoint 3: `http://127.0.0.1:5000/v1/stake/all-restaurants-near-me`
#### Request:
```commandline
{
    "locationInfo": "123"
}
```

#### Response:
```commandline
{
"1": {
"restaurant_id": 1,
"name": "restaurant_one",
"coordinates": 12345,
"staked_amount": 0,
"reviews": {
"cde": {
"review_hash": "cde",
"review_content": "This is the second review",
"owner_info": "test_user_2",
"restaurant_id": "1"
}
}
},
"2": {
"restaurant_id": 2,
"name": "restaurant_two",
"coordinates": 12345,
"staked_amount": 0,
"reviews": {}
},
"3": {
"restaurant_id": 3,
"name": "restaurant_three",
"coordinates": 12345,
"staked_amount": 0,
"reviews": {}
},
"4": {
"restaurant_id": 4,
"name": "restaurant_four",
"coordinates": 12345,
"staked_amount": 0,
"reviews": {}
},
"5": {
"restaurant_id": 5,
"name": "restaurant_five",
"coordinates": 12345,
"staked_amount": 0,
"reviews": {}
}
}
```

