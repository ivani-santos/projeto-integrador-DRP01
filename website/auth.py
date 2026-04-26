from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login-fotografo')
def login_fotografo():
    return render_template("login_fotografo.html")

@auth.route('/login-client')
def login_client():
    return render_template("login_client.html")

@auth.route('/logout')
def logout():
    return "<p>Sair</p>"

@auth.route('/signup-fotografo')
def signup_fotografo():
    return render_template("signup_fotografo.html")

@auth.route('/signup-client')
def signup_client():
    return render_template("signup_client.html")
