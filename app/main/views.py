from flask import render_template, url_for
import yaml
from . import main
from .models import Meal, Recipe, Nutrition, TripEntry
from .forms import NameForm, RiverForm

with open('app/static/recipes.yml', 'r') as stream:
    recipes = yaml.load(stream, Loader=yaml.FullLoader)

test = \
    {
    'meal': 'breakfast',
    'recipe': {
        'name':'GF pancake',
        'description':'Buckwheat, Cornmeal, and Yogurt round out this thin GF pancake',
        'main_image': 'pancakes',
        'adapted_from': None,
        'nutrition':{'calories': 252,'protein': 11,'servings': 2},
        'sections': [{'instruction': 'DRY INGREDIENTS', 'image': 'flour', 'ingredients': ['50g Cornmeal', '50g Buckwheat Flour', '1.5 t Baking Powder', '1.5 t Sugar', '.25 t salt', 'flour']},
                     {'instruction': 'WET INGREDIENTS', 'ingredients': ['1 Egg', '50g High Protein Yogurt', '75 mL Hot Water(To Soften the Cornmeal)', '50 mL Milk'], 'image': 'milkandeggs'},
                     {'instruction': 'MIX AND FRY', 'ingredients': ['This mix tends to separate, just mix right before pouring the batter into the pan'], 'image':'pancakes'}]
        }
    }

@main.context_processor
def inject_recipes():
    return dict(recipes=recipes)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/nameform', methods = ['GET','POST'])
def recipe_uploading():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('recipe_form.html', form=form, name=name )

@main.route('/riverform', methods = ['GET','POST'])
def db_form_upload():
    form = RiverForm()
    if form.validate_on_submit():
        trip_entry = TripEntry(
            riverSection=form.riverSection.data,
            difficulty=form.difficulty.data,
            date=form.date.data,
            flow=form.flow.data,
            water_level=form.water_level.data
        )
        trip_entry.save()
    return render_template('recipe_form.html', form=form)

@main.route('/dbtesting')
def recipe_save():
    # Building a nested document
    nutrition = Nutrition(**test['recipe']['nutrition'])
    recipe = Recipe(nutrition=nutrition, **{k:v for k,v in test['recipe'].items() if k != 'nutrition'})
    Meal(meal=test.get('meal'), recipe=recipe).save()
    return 'OK', 200

@main.route('/meal/<meal>')
def meal_choice(meal):
    return render_template('meal.html', meal=meal)

@main.route('/meal/<meal>/recipe/<name>')
def recipe(meal, name):
    return render_template('recipe.html', meal=meal, name=name)

