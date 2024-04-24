from faker import Faker
import random

fake = Faker()

def generate_users(num):
    users = []
    for _ in range(num):
        user = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address()
        }
        users.append(user)
    return users

def generate_products(num):
    products = []
    for _ in range(num):
        product = {
            'name': fake.word().capitalize(),
            'price': round(random.uniform(5, 100), 2),
            'description': fake.text()
        }
        products.append(product)
    return products

def generate_orders(users, products, num):
    orders = []
    for _ in range(num):
        order = {
            'user': fake.random_element(users),
            'product': fake.random_element(products),
            'quantity': fake.random_number(digits=1, fix_len=True),
            'total_price': round(random.uniform(10, 500), 2)
        }
        orders.append(order)
    return orders

def generate_fake_data(num_users, num_products, num_orders):
    users = generate_users(num_users)
    products = generate_products(num_products)
    orders = generate_orders(users, products, num_orders)
    return users, products, orders
