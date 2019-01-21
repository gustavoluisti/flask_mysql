from . import categories
from flask import request
from db import db
from db.models import Category

@categories.route('/', methods=['GET'])
def list():
    return "Listing Categories  "


@categories.route('/', methods=['POST'])
def create():
    name = request.json['name']

    new_category = Category(name)

    db.session.add(new_category)
    db.session.commit()

    return jsonify(id = new_category.id, name = new_category.name)