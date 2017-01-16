from django.db import models

class Profile(object):

    def __init__(self, name='', email='', phone='',company=''):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company
