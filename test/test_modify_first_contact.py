# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    old_contact = app.contact.get_contact_list()
    contacts = Contact(firstname="New Contact2")
    contacts.id = old_contact[0].id
    app.contact.modify_first_contact(contacts)
    assert len(old_contact) == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact[0] = contacts
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


