from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Reviews(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    rating = db.Column(db.String, nullable=False)
    review_text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, server_default=db.func.now())

class BrandedTShirts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'size': self.size,
            'color': self.color
        }

class SpeciesOfTrees(db.Model):
    __tablename__ = 'species_of_trees'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'description': self.description
        }

class BrandedHoodies(db.Model):
    __tablename__ = 'branded_hoodies'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'size': self.size,
            'color': self.color
        }

@app.route('/api/products/<product_type>', methods=['GET'])
def get_products(product_type):
    if product_type == 'tshirts':
        products = BrandedTShirts.query.all()
    elif product_type == 'trees':
        products = SpeciesOfTrees.query.all()
    elif product_type == 'hoodies':
        products = BrandedHoodies.query.all()
    else:
        return jsonify({'error': 'Invalid product type'}), 400
    
    serialized_products = [product.serialize() for product in products]
    return jsonify({'products': serialized_products})

@app.route('/api/products/<product_type>/<int:product_id>', methods=['GET'])
def get_product(product_type, product_id):
    if product_type == 'tshirts':
        product = BrandedTShirts.query.get(product_id)
    elif product_type == 'trees':
        product = SpeciesOfTrees.query.get(product_id)
    elif product_type == 'hoodies':
        product = BrandedHoodies.query.get(product_id)
    else:
        return jsonify({'error': 'Invalid product type'}), 400
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify(product.serialize())

@app.route('/api/products/<product_type>', methods=['POST'])
def create_product(product_type):
    data = request.json
    if product_type == 'tshirts':
        new_product = BrandedTShirts(
            brand=data['brand'],
            size=data['size'],
            color=data['color']
        )
    elif product_type == 'trees':
        new_product = SpeciesOfTrees(
            name=data['name'],
            scientific_name=data['scientific_name'],
            description=data['description']
        )
    elif product_type == 'hoodies':
        new_product = BrandedHoodies(
            brand=data['brand'],
            size=data['size'],
            color=data['color']
        )
    else:
        return jsonify({'error': 'Invalid product type'}), 400
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/api/products/<product_type>/<int:product_id>', methods=['PUT'])
def update_product(product_type, product_id):
    data = request.json
    if product_type == 'tshirts':
        product = BrandedTShirts.query.get(product_id)
    elif product_type == 'trees':
        product = SpeciesOfTrees.query.get(product_id)
    elif product_type == 'hoodies':
        product = BrandedHoodies.query.get(product_id)
    else:
        return jsonify({'error': 'Invalid product type'}), 400
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    if product_type == 'tshirts' or product_type == 'hoodies':
        product.brand = data.get('brand', product.brand)
        product.size = data.get('size', product.size)
        product.color = data.get('color', product.color)
    elif product_type == 'trees':
        product.name = data.get('name', product.name)
        product.scientific_name = data.get('scientific_name', product.scientific_name)
        product.description = data.get('description', product.description)
    
    db.session.commit()
    
    return jsonify({'message': 'Product updated successfully'})

@app.route('/api/products/<product_type>/<int:product_id>', methods=['DELETE'])
def delete_product(product_type, product_id):
    if product_type == 'tshirts':
        product = BrandedTShirts.query.get(product_id)
    elif product_type == 'trees':
        product = SpeciesOfTrees.query.get(product_id)
    elif product_type == 'hoodies':
        product = BrandedHoodies.query.get(product_id)
    else:
        return jsonify({'error': 'Invalid product type'}), 400
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
