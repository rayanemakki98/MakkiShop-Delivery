from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import EqualTo, DataRequired, Email
from app.vars import Tools, admin_type

tools = Tools()

class ContactForm(FlaskForm):
    name = StringField('Nom *', [DataRequired()])
    email = StringField('Adresse Courriel *', [DataRequired()])
    phone = StringField('Telephone', [DataRequired()])
    message = TextAreaField('Message *', [DataRequired()])
    submit = SubmitField('Envoyer')


class AdminSignup(FlaskForm):

    ent_name = StringField("Nom de L'Entreprise",[DataRequired()])
    ent_type = SelectField(choices=admin_type)
    ent_director = StringField("Directeur L'Entreprise", [DataRequired()])
    ent_country = SelectField(choices=tools.countries(),
                                       default=tools.countries()['Lebanon'])
    ent_city = StringField("Ville", [DataRequired()])
    ent_address = StringField("Adresse", [DataRequired()])
    ent_email = StringField("Email", [Email(message="Invalid Email!"),
                                       DataRequired()])
    ent_phone = StringField("Phone", [DataRequired()])
    ent_password = PasswordField('Mot de Passe',
                                  [DataRequired(message='Must Enter a valid Password!')])
    confirm_password = PasswordField("Confirmer le mot de passe",
                                     [EqualTo(ent_password, message='Password must match!')])

    submit = SubmitField('Submit')


class AdminLogin(FlaskForm):
    ent_email = StringField("Email", [Email(message="Invalid Email!"),
                                      DataRequired()])
    ent_phone = StringField("Phone", [DataRequired()])
    ent_password = PasswordField('Mot de Passe',
                                 [DataRequired(message='Must Enter a valid Password!')])

    submit = SubmitField('Se Connecter')


class AddProduct(FlaskForm):
    name = StringField("Nom du Produit", [DataRequired()])
    categ = StringField("Categorie", [DataRequired()])
    barcode = StringField("Barcode", [DataRequired()])
    quantity = StringField("Quantity", [DataRequired()])
    ent_type = StringField("Entreprise", [DataRequired()], render_kw={'readonly': True})

    submit = SubmitField('Ajouter')

