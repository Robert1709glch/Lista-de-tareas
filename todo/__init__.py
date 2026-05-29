#Este archivo hace que python tome la carpeta como un modulo
import os
from flask import Flask

def create_app():
    app= Flask(__name__)
    #From mapping define variables de config que se pueden usar en la app
    app.config.from_mapping(
        SECRET_KEY='supersecretkey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )
    from . import db

    db.init_app(app)
    
    @app.route('/')
    def hola():
        return "Si funciono:)"
    return app