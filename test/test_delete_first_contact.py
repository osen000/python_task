# -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    app.contact.delete_first_contact()
