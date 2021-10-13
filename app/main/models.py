from .. import db

class Recipe(db.Document):
    meal = db.StringField()
    recipe = db.StringField()