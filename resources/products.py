from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)


class Products(db.Model):
    __tablename__ ="products"
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    category=db.Column(db.String, nullable=False)
    brand=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    eco_rating=db.Column(db.String, nullable=False)
    manufacturer_link=db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

@app.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    output = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'brand': product.brand,
            'price': product.price,
            'eco_rating': product.eco_rating,
            'manufacturer_link': product.manufacturer_link,
            'created_at': product.created_at
        }
        output.append(product_data)
    return jsonify({'products': output})

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Products.query.get_or_404(product_id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'brand': product.brand,
        'price': product.price,
        'eco_rating': product.eco_rating,
        'manufacturer_link': product.manufacturer_link,
        'created_at': product.created_at
    }
    return jsonify(product_data)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Products(
        name=data['name'],
        description=data['description'],
        category=data['category'],
        brand=data['brand'],
        price=data['price'],
        eco_rating=data['eco_rating'],
        manufacturer_link=data['manufacturer_link']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'})

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Products.query.get_or_404(product_id)
    data = request.json
    product.name = data['name']
    product.description = data['description']
    product.category = data['category']
    product.brand = data['brand']
    product.price = data['price']
    product.eco_rating = data['eco_rating']
    product.manufacturer_link = data['manufacturer_link']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
