from models import db,Restaurant,RestaurantPizza,Pizza
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///instance/app.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

with SessionLocal() as session:
    session.query(RestaurantPizza).delete()  # Delete associations first
    session.query(Pizza).delete()
    session.query(Restaurant).delete()  # Delete restaurants last (due to foreign keys)
    session.commit()
    
restaurants = [
    Restaurant(name="Cheesy Delight", address="789 Oak St"),
    Restaurant(name="Taste of Italy", address="123 Maple Ave"),
    Restaurant(name="Spice House", address="YH2T+8R7, Kileleshwa Rd, Nairobi"),
    Restaurant(name="Gourmet Haven", address="3rd Floor Victoria Plaza, Victoria Street"),
    Restaurant(name="Urban Bites Cafe", address="XW73+PQK 456, Diplomatic Drive, Nairobi"),
    Restaurant(name="Safari Grill", address="Simba Lodge, Ngong Rd, 12345 - 00600, Nairobi"),
]

pizzas = [
    Pizza(name="Supreme Feast", ingredients="Pepperoni, sausage, bell peppers, onions, olives"),
    Pizza(name="Vegetarian Bliss", ingredients="Tomatoes, mushrooms, spinach, feta cheese"),
    Pizza(name="Seafood Sensation", ingredients="Shrimp, crab, garlic, parsley"),
    Pizza(name="Hawaiian Delight", ingredients="Ham, pineapple, bacon"),
    Pizza(name="Mediterranean Magic", ingredients="Tomato sauce, feta cheese, olives, sun-dried tomatoes, basil"),
]

restaurant_pizzas = [
    RestaurantPizza(restaurants=restaurants[5], pizzas=pizzas[0], price=15),
    RestaurantPizza(restaurants=restaurants[0], pizzas=pizzas[1], price=13),
    RestaurantPizza(restaurants=restaurants[1], pizzas=pizzas[4], price=14),
    RestaurantPizza(restaurants=restaurants[2], pizzas=pizzas[2], price=25),
    RestaurantPizza(restaurants=restaurants[1], pizzas=pizzas[3], price=18),
    RestaurantPizza(restaurants=restaurants[3], pizzas=pizzas[3], price=8),
    RestaurantPizza(restaurants=restaurants[4], pizzas=pizzas[4], price=20),
    RestaurantPizza(restaurants=restaurants[5], pizzas=pizzas[2], price=7),
]

with SessionLocal() as session:
    session.add_all(restaurants)
    session.add_all(pizzas)
    session.add_all(restaurant_pizzas)
    session.commit()