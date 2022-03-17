import os
from flask import Flask

def create_app():
    app = Flask(__name__)   #creamos la app

    app.config.from_mapping(        #configuramos la app
        SENDGRID_API_KEY=os.environ.get("SENDGRID_API_KEY"),     #el primer argumento es la variable de la aplicación que va a contener su respectiva información
                                                            #luego el segundo argumento (lo de la derecha) es de donde sacamos ese valor, el cual es del sistema operativo y el nombre de esta variable de entorno es lo que está entre comillas
        FROM_EMAIL=os.environ.get("FROM_EMAIL"),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE=os.environ.get("FLASK_DATABASE")
    )

    from . import db    #importamos nuestro módulo db

    db.init_app(app)    #iniciamos la base de datos

    from . import mail  #importamos mail que contiene los bluePrints

    app.register_blueprint(mail.bp)     #registramos en nuestra app(o su contexto) el bp de mail

    return app
