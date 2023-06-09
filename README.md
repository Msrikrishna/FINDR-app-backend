## FINDR Backend
This is a backend for FINDR project hosted on [Frontend](https://github.com/Msrikrishna/FINDR-app-frontend)
Once this is run, the frontend seamlessly interacts with the backend to store and retrieve review Hash data.

### Pre-requisite

#### Background:
- Java 17
- Springboot 3

#### To run:
- `mvn package` to make the package jar file. Then, run the next command.
- `java -cp target/findr-0.0.1-SNAPSHOT.jar com.findr.findr.FindrApplication`

#### Swagger:
- http://localhost:8080/swagger-ui/index.html

### Endpoints

#### POST /v1/review-submit
- Request:
```
{
  "reviewHash": "",
  "reviewContent": "",
  "ownerInfo": "",
  "restaurantId": ""
}
```

#### POST /v1/reviews-from-hashes/{restaurantId}
- Request:
```
[rest](http://localhost:8080/v1/reviews-from-hashes/1)
```

- Body:
```
[
  {
    "reviewHash": "",
  }
]
```

- Response:
```
[
  {
    "reviewHash": "",
    "reviewContent": "",
    "ownerInfo": "",
    "restaurantId": "1"
  }
]
```
