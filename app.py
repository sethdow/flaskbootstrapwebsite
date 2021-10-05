import flask_bootstrap
import yaml
from flask import Flask, render_template, url_for

app = Flask(__name__)

bootstrap = flask_bootstrap.Bootstrap(app)
with open('static/recipes.yml', 'r') as stream:
    recipes = yaml.load(stream)

print(recipes)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    myDict = {'name':name}
    print(myDict)
    return render_template('user.html',myDict = myDict)

@app.route('/recipe/<meal>/<name>')
def recipe(meal,name):
    return render_template('recipe.html',meal=meal,name=name, recipes=recipes)

if __name__ == '__main__':
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
