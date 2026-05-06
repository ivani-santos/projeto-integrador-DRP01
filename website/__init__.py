#cria o site e define o que está nele, como plantas e chaves de acesso aos cookies
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'paralelo'
    
    from .views import views
    from .auth import auth
    from .profile import profile
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/')
    
    return app
