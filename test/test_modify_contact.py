# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_modify_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contacts = Contact(firstname="New Contact2")
    contacts.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contacts)
    assert len(old_contact) == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contacts
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


