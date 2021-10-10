from flask_bootstrap import Bootstrap
import yaml
from flask import Flask, render_template, url_for


app = Flask(__name__)
bootstrap = Bootstrap(app)

with open('static/recipes.yml', 'r') as stream:
    recipes = yaml.load(stream, Loader=yaml.FullLoader)

# add the recipes dict as a globally available variable to the templates
@app.context_processor
def inject_stage_and_region():
    return dict(recipes=recipes)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<meal>')
def meal_choice(meal):
    return render_template('meal.html', meal=meal)

@app.route('/<meal>/<name>')
def recipe(meal, name):
    return render_template('recipe.html', meal=meal, name=name)


if __name__ == '__main__':
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
