from flask_security import UserMixin
from app import db, create_app


class Contacts(UserMixin, db.Model):
    __tablename__ = 'contacts'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    message =db.Column(db.String(500), nullable=False)
    sended = db.Column(db.String(32), nullable=False)
    responded = db.Column(db.String(32), nullable=True, default='none')

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message,
            'sended': self.sended,
            'responded': self.responded
        }


class News(UserMixin, db.Model):
    __tablename__ = 'news'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(36), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=False)
    details = db.Column(db.String(500), nullable=False)
    created = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'subtitle': self.subtitle,
            'details': self.details,
            'created': self.created
        }


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    ent_name = db.Column(db.String(64), nullable=False, unique=True)
    ent_type = db.Column(db.String(64), nullable=False)
    ent_director = db.Column(db.String(64), nullable=False)
    ent_country = db.Column(db.String(64), nullable=False)
    ent_city = db.Column(db.String(64), nullable=False)
    ent_address = db.Column(db.String(64), nullable=False)
    ent_email = db.Column(db.String(100), nullable=False, unique=True)
    ent_phone = db.Column(db.String(15), nullable=False)
    ent_password = db.Column(db.String(255), nullable=False)
    ent_code = db.Column(db.String(10), nullable=False, unique=True)
    created = db.Column(db.String(32), nullable=False)
    login_at = db.Column(db.String(32), nullable=True, default='None')
    logout_at = db.Column(db.String(32), nullable=True, default='None')

    def __repr__(self):
        return {
            'id': self.id,
            'Entreprise': self.ent_name,
            'Directeur': self.ent_director,
            'Pays': self.ent_country,
            'Ville': self.ent_city,
            'Adresse': self.ent_address,
            'Email': self.ent_email,
            'Phone': self.ent_phone,
            'EntCode': self.ent_code,
            'Created': self.created,
            'Login at': self.login_at,
            'Logout at': self.logout_at
        }

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Product(db.Model, UserMixin):

    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    categorie = db.Column(db.String(64), nullable=False)
    barcode = db.Column(db.String(16), nullable=False)
    quantity = db.Column(db.String(10), nullable=False)
    ent_type = db.Column(db.String(64), nullable=False)
    created = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f'id: {self.id}, ' \
               f'product_name: {self.name}, ' \
               f'categorie: {self.categorie}, ' \
               f'barcode: {self.barcode}, ' \
               f'quantity: {self.quantity}, ' \
               f'Enteprise Type: {self.ent_type}, ' \
               f'created: {self.created}'


db.create_all(app=create_app())