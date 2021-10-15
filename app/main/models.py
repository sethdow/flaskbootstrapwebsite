from .. import db

# class Sections(db.EmbeddedDocument):
#     instruction: db.StringField()
#     ingredients: db.ListField()
#     image: db.StringField()


###### QUICK TEST #######
class TripEntry(db.Document):
    riverSection = db.StringField()
    difficulty = db.FloatField()
    date = db.DateField()
    flow = db.IntField()
    water_level = db.StringField()

############## RECIPE ###############
class Nutrition(db.EmbeddedDocument):
    servings = db.IntField()
    protein = db.IntField()
    calories = db.IntField()

class Recipe(db.EmbeddedDocument):
    name = db.StringField()
    description = db.StringField()
    main_image = db.StringField()
    adapted_from = db.StringField()
    nutrition = db.EmbeddedDocumentField(Nutrition)
    sections = db.ListField()

class Meal(db.Document):
    meal = db.StringField()
    recipe = db.EmbeddedDocumentField(Recipe)

