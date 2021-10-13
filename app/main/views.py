from flask import render_template, url_for
import yaml
from . import main
from .models import Recipe

with open('app/static/recipes.yml', 'r') as stream:
    recipes = yaml.load(stream, Loader=yaml.FullLoader)

@main.context_processor
def inject_recipes():
    return dict(recipes=recipes)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/dbtesting')
def recipe_save():
    Recipe(recipe='Recipe name', meal='lunch').save()
    return 'OK', 200

@main.route('/meal/<meal>')
def meal_choice(meal):
    return render_template('meal.html', meal=meal)

@main.route('/meal/<meal>/recipe/<name>')
def recipe(meal, name):
    return render_template('recipe.html', meal=meal, name=name)

