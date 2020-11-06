from datetime import datetime as dt
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_security import logout_user
from app import db, mail
from app.forms import ContactForm
from app.models import Contacts, News
from app.vars import *


# Blueprint
mainbp = Blueprint(
    'mainbp',
    __name__,
    static_folder='static',
    template_folder='templates'
)

@mainbp.route('/')
def home():
    req_news = News.query.all()
    return render_template('home.html',
                           title='Makki Shop Delivery',
                           req_news=req_news,
                           bg='img/homebg.jpg',
                           main_categories=main_categories
                           )

@mainbp.route('/about')
def about():
    return render_template('about.html',
                           title = 'About Us'
                           )

@mainbp.route('/contact')
def contact():
    contactform = ContactForm()
    return render_template('contact.html',
                           title='Contact Us',
                           contacts=contacts,
                           contactform=contactform)

@mainbp.route('/contact', methods=['POST'])
def contact_post():
    tools = Tools()
    contactform = ContactForm()
    new_message = Contacts(
        name=contactform.name.data,
        email=contactform.email.data,
        phone=contactform.phone.data,
        message=contactform.message.data,
        sended=dt.now()
    )

    tools.send_mail(
        subject='Makki Shop Delivery | Nous Contacter',
        sender='rayanemakki98@gmail.com',
        recipients=[contactform.email.data],
        body= f'Bonjour {contactform.name.data}, \n'
              f'\n'
              f'Nous avons bien reçu votre message: \n'
              f'({contactform.message.data}). \n'
              f'Un agent du soutien technique vous contactera '
              f'dès que possible.'
              f'\n\n'
              f'Cordialement, \n'
              f'\n\n'
              f'Medicapp = RKTEAM | Soutien Techinque et Service à La Clientèle \n'
              f'email: rayanemakki98@gmail.com'
    )
    db.session.add(new_message)
    db.session.commit()
    flash('Le message a été reçu, Vous allez recevoir un Courieel de confirmation')
    return redirect(url_for('main.contact'))

@mainbp.route('/news/<page>')
def news(page):
    req_news = News.query.all()
    return render_template('news.html',
                           title='Nouvelles et Mises à Jour',
                           page=page,
                           req_news=req_news,
                           bg='img/newbg.jpg'
                           )



@mainbp.route('/FAQ')
def faq():
    return render_template('FAQ.html',
                           title='FAQ',
                           )

@mainbp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('mainbp.home'))