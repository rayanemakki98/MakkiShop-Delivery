from flask import Blueprint, redirect, url_for, flash
from flask_login import login_user, current_user
from datetime import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import Admin, Product
from app.forms import AdminLogin, AdminSignup, AddProduct
from app  import db
from app.vars import *

entauth = Blueprint(
    'entauth',
    __name__,
    static_folder='static',
    template_folder='templates'
)

@entauth.route('/admin/login', methods=['POST'])
def login_post():
    # ajouter Form Login
    form = AdminLogin()
    # Query User by email
    search = Admin.query.filter_by(ent_email=form.ent_email.data).first()
    # verify email existence in data
    if not search or not check_password_hash(search.ent_password, form.ent_password.data):
        flash("Email ou Mot de Passe Invalide! Veuillez Réessayer de nouveau!")
        return redirect(url_for('entbp.login'))

    else:
        login_user(search)
        return redirect(url_for('entbp.profile',
                                name=search.ent_name,
                                pays=search.ent_country,
                                ville=search.ent_city))


@entauth.route('/admin/signup', methods=['POST'])
def signup_post():
    form = AdminSignup()

    search = Admin.query.filter_by(ent_email=form.ent_email.data).first()

    ent_code = f'{form.ent_country.data[0].capitalize()}{form.ent_city.data[0].capitalize()}{form.ent_phone.data[-4:]}'

    if search:
        flash('Adresse Courriel déjà existant!')
        return redirect(url_for('entbp.signup'))

    new_admin = Admin(
        ent_name=form.ent_name.data,
        ent_type=form.ent_type.data,
        ent_director=form.ent_director.data,
        ent_country=form.ent_country.data,
        ent_city=form.ent_city.data,
        ent_address=form.ent_address.data,
        ent_email=form.ent_email.data,
        ent_phone=form.ent_phone.data,
        ent_password=generate_password_hash(form.ent_password.data, method='sha256'),
        ent_code=ent_code,
        created=dt.now(),
    )

    #   add the new user to the database
    db.session.add(new_admin)
    db.session.commit()

    """
    send_mail(
        "Création d'un compte Medicapp | Client",
        'rayanemakki98@gmail.com',
        [form.email.data],
        f"Bonjour {form.fname.data}!\n"
        f"Félicitations! Votre compte Medicapp a été bien créé "
        f"avec succès.\n"
        f"\n"
        f"\n"
        f"Au plaisir!"
    )
    """

    return redirect(url_for('entbp.login',
                            name=form.ent_name.data,
                            pays=form.ent_country.data,
                            ville=form.ent_city.data
                            ))



@entauth.route('/admin/profile/<name>/<pays>/<ville>/<type>', methods=['POST'])
def addProductPost(name, pays, ville, type):

    add_product = AddProduct()

    search = Product.query.filter_by(barcode=add_product.barcode.data).first()

    if search:
        flash('product already exist!')
        return redirect(url_for(
            'entbp.addProduct',
            name=current_user.ent_name,
            pays=current_user.ent_country,
            ville=current_user.ent_city,
            type=current_user.ent_type
        ))
    else:
        new_product = Product(
            name=add_product.name.data,
            categ=add_product.categ.data,
            barcode=add_product.barcode.data,
            quantity=add_product.quantity.data,
            ent_type=add_product.ent_type.data,
            created=dt.utcnow()
        )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for(
            'entbp.addProduct',
            name=current_user.ent_name,
            pays=current_user.ent_country,
            ville=current_user.ent_city,
            type=current_user.ent_type
        ))
