# Flask Code Challenge - Pizza Restaurants

For this assessment, you'll be working with a Pizza Restaurant domain.

Note: You are required to come up with a fully functional React frontend application, so you can test if your API is working. A fully functional front end will also be assessed for this code challenge. Below is a zip file to get you started.

[python-code-challenge-pizzas.zip](python-code-challenge-pizzas.zip)

## Models

You need to create the following relationships:

- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`

## Validations

Add validations to the `RestaurantPizza` model:

- must have a `price` between 1 and 30

## Routes

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.

(GET /restaurants)
Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]```

(GET /restaurants/:id)
If the `Restaurant` exists, return JSON data in the format below:
```bash
{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:
``bash
{
  "error": "Restaurant not found"
}

(DELETE /restaurants/:id)
If the `Restaurant` exists, it should be removed from the database, along with any `RestaurantPizza`s that are associated with it (a `RestaurantPizza` belongs to a `Restaurant`, so you need to delete the `RestaurantPizza`s before the `Restaurant` can be deleted).
After deleting the `Restaurant`, return an _empty_ response body, along with the appropriate HTTP status code.
If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:

```bash
{
  "error": "Restaurant not found"
}```

(GET /pizzas)
Return JSON data in the format below:
``bash
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]```

(POST /restaurant_pizzas)
This route should create a new `RestaurantPizza` that is associated with an existing `Pizza` and `Restaurant`. It should accept an object with the following properties in the body of the request:
``bash
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
If the `RestaurantPizza` is created successfully, send back a response with the data related to the `Pizza`:
``bash
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the `RestaurantPizza` is **not** created successfully, return the following JSON data, along with the appropriate HTTP status code:
``bash
{
  "errors": ["validation errors"]
}
