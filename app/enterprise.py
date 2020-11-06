from flask import Blueprint, render_template
from flask_security import login_required, current_user
from datetime import datetime as dt
from app.models import Admin, Product
from app.vars import *
from app.forms import AdminLogin, AdminSignup, AddProduct
from sqlalchemy import asc, desc

entbp = Blueprint(
    'entbp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@entbp.route('/admin/login')
def login():
    form = AdminLogin()
    return render_template('enterprise/login.html',
                           title='Se Connecter',
                           form=form,
                           bg='img/loginbg.jpg'
                           )

@entbp.route('/admin/signup')
def signup():
    form = AdminSignup()
    time = dt.now()
    return render_template('enterprise/signup.html',
                           title='Créer Un Compte',
                           form=form,
                           time=time,
                           bg='img/signupbg.jpg'
                           )

@entbp.route('/admin/profile/<name>/<pays>/<ville>')
@login_required
def profile(name, pays, ville):
    tools = Tools()

    user = Admin.query.filter_by(ent_email=current_user.ent_email).first()

    return render_template('enterprise/profile.html',
                           title="Profile",
                           name=name,
                           pays=pays,
                           ville=ville,
                           current_user=current_user,
                           tools=tools,
                           user=user,
                           bg='img/profilebg.jpg'
                           )

@entbp.route('/admin/profile/<name>/<pays>/<ville>/<type>')
@login_required
def myStore(name, pays, ville, type):
    add_product = AddProduct()

    product = Product.query.filter_by(ent_type=current_user.ent_type).all()

    return render_template(
        'enterprise/store.html',
        title='My Store',
        name=name,
        pays=pays,
        ville=ville,
        type=type,
        current_user=current_user,
        bg='img/storebg.jpg',
        product=product,
        ap=add_product
    )