# -*- coding: utf-8 -*-

from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contacts = Contact(firstname="New Contact2")
    app.contact.modify_contact_by_id(contact.id, contacts)
    assert len(old_contact) == app.contact.count_contact()
    new_contact = db.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


