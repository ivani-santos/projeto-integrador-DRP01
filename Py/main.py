#Este arquivo importa o Flask e cria as bases do site, banco de dados...

from flask import Flask

from flask_bootstrap import Bootstrap5

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run()