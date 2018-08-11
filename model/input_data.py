class Admin:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


class Customer:
    def __init__(self, firstname=None, lastname=None, address=None, postcode=None, city=None, country=None, zone=None,
                 email=None, phone=None, password=None, username1=None, password1=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.postcode = postcode
        self.city = city
        self.country = country
        self.zone = zone
        self.email = email
        self.phone = phone
        self.password = password
        self.username1 = username1
        self.password1 = password1


class Product:
    def __init__(self, username=None, password=None, product_name=None, code_product=None, quantity=None, image=None, date_valid_from=None,
                 date_valid_to=None, keywords=None, short_description=None, trumbowyg_editor=None, head_title=None,
                 meta_description=None, purchase_price=None, prices_usd=None, prices_eur=None
                 ):
        self.username = username
        self.password = password
        self.product_name = product_name
        self.code_product = code_product
        self.quantity = quantity
        self.image = image
        self.date_valid_from = date_valid_from
        self.date_valid_to = date_valid_to
        self.keywords = keywords
        self.short_description = short_description
        self.trumbowyg_editor = trumbowyg_editor
        self.head_title = head_title
        self.meta_description = meta_description
        self.purchase_price = purchase_price
        self.prices_usd = prices_usd
        self.prices_eur = prices_eur
