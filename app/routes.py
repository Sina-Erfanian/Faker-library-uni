from flask import render_template, request
from app import app
from app.fake_data_generator import generate_fake_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_fake_data', methods=['GET', 'POST'])
def generate_fake():
    if request.method == 'POST':
        num_users = int(request.form.get('num_users'))
        num_products = int(request.form.get('num_products'))
        num_orders = int(request.form.get('num_orders'))
    else:
        num_users = 5
        num_products = 10
        num_orders = 20

    users, products, orders = generate_fake_data(num_users, num_products, num_orders)
    return render_template('fake_data.html', users=users, products=products, orders=orders)
