import yaml
from flask import Flask, render_template, url_for

from . import main




@main.route('/')
def home():
    return render_template('home.html')

@main.route('/<meal>')
def meal_choice(meal):
    return render_template('meal.html', meal=meal)

@main.route('/<meal>/<name>')
def recipe(meal, name):
    return render_template('recipe.html', meal=meal, name=name)

