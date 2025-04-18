from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config['SECRET_KEY'] = 'dev'
    app.config['DATABASE'] = 'bugs.db'
    app.register_blueprint(main)
    return app

# Create the app instance at the module level
app = create_app()