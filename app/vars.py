from flask_mail import Message

from app import mail


class Tools:

    def cutStringOnComma(self, x):
        liste = []
        for i in x.split(', '):
            liste.append(i)
        return liste

    def cutStringOnSpace(self, x):
        liste = []
        for i in x.split(' '):
            liste.append(i)
        return liste

    # select countyr from pycountry
    def countries(self):
        import pycountry
        pays = {}
        for country in pycountry.countries:
            pays[country.name] = country.name
        return pays

    # Envoyer Un Courriel automatique
    def send_mail(self, subject, sender, recipients, body):
        msg = Message(
            subject=subject,
            sender=sender,
            recipients=recipients
        )

        msg.body = body
        mail.send(msg)
        return "EMAIL SENT!"


contacts = {
    'Telephone': ['tel:5819843613', '+1 (581) 984-3613'],
    'Courriel': ['mailto:rayanemakki98@gmail.com', 'rayanemakki98@gmail.com'],
    'Messenger': ['#messenger', '@Medicapp'],
    'Chatzone': ['#chatzone', 'Discutez avec un de nos employés!']
}

main_categories = {
    'Restaurants': ['Restaurants', 'img/restaurants.jpg'],
    'Super Market Makki': ['Super Market Makki', 'img/makki.jpg'],
    'Markets & Malls': ['Markets and Malls', 'img/markets.jpg'],
    'Fruits et Légumes': ['Fruits et Légumes', 'img/legumes.jpg'],
    'Viandes': ['Viandes', 'img/viandes.jpg'],
    'Fashion': ['Mode et Vêtements', 'img/fashion.jpg'],
    'Electronique & Techno': ['Electro & Techno', 'img/info.jpg'],
    'Maison': ['Article Ménagers', 'img/house.jpg']
}

admin_type = [
    'Restaurant',
    'Market',
    'Mini Market',
    'Mall',
    'Légumes et Fruits',
    'Viandes',
    'Electronique',
    'Telephone',
    'Meubles',
    # add other here!
]