from app import create_app
import os


# add the recipes dict as a globally available variable to the templates
app = create_app(os.environ.get('FLASK_CONFIG', 'default'))

print(app.config.get("MONGODB_HOST"))



