from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine
from config import config
with open('app/static/recipes.yml', 'r') as stream:
    recipes = yaml.load(stream, Loader=yaml.FullLoader)

# add the recipes dict as a globally available variable to the templates
@app.context_processor
def inject_stage_and_region():
    return dict(recipes=recipes)

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=environ.get("PORT", 5000))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
