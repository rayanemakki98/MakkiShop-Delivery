from datetime import timedelta
from flask_babel import Babel
from flask import Flask, session, g, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

# Declare Variables
db = SQLAlchemy()
lm = LoginManager()
mail = Mail()
babel = Babel()


# Create our app here!
def create_app():

    app = Flask(__name__)

    # our app config links here!
    if app.config["ENV"] == "production":
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # print Env
    print(f'ENV is set to: {app.config["ENV"]}')


    # initiate components
    db.init_app(app)
    lm.init_app(app)
    mail.init_app(app)
    babel.init_app(app)

    lm.blueprint_login_views = {
        'admin': '/admin/login',
        'client': '/client/login'
    }


    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)

    # import modules here!
    from .models import Contacts, News, Admin
    from .enterprise import entbp
    from .enterprise_auth import entauth
    from .main import mainbp

    @lm.user_loader
    def load_user(user_id, endpoint='user'):
        #cx = Client.query.get(int(user_id))
        admin = Admin.query.get(int(user_id))

        return admin

    app.register_blueprint(mainbp)
    #app.register_blueprint(client)
    #app.register_blueprint(clientauth)
    app.register_blueprint(entbp)
    app.register_blueprint(entauth)

    return app

db.create_all(app=create_app())
