from webshop import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float)
    description = db.Column(db.String)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Article('{self.name}', '{self.price}', '{self.description}', '{self.image_file}')"