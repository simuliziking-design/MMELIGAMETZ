from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

products = [
    {'id': 1, 'name': 'Game 1', 'price': 10},
    {'id': 2, 'name': 'Game 2', 'price': 20},
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = [p for p in products if p['id'] in session.get('cart', [])]
    return render_template('cart.html', cart=cart_items)

if __name__ == '__main__':
    app.run(debug=True)