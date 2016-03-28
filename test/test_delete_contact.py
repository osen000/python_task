# -*- coding: utf-8 -*-

from model.contact import Contact
import random

# def test_edit_first_contact(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create(Contact(firstname="Contact"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     assert len(old_contact) - 1 == app.contact.count_contact()
#     new_contact = app.contact.get_contact_list()
#     old_contact[0:1] = []
#     assert old_contact == new_contact


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contact) - 1 == app.contact.count_contact()
    new_contact = db.get_contact_list()
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)