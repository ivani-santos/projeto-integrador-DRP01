from flask import Flask

def create_app():
    app = Flask(__name__)
    app.congig['secret_key'] = 'paralelo'
    
    return app
