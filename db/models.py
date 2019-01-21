from db import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))

    def __init__(sef, name):
        self.name = name
    
    def __repr__(self):
        return 'Category %r' % self.name
