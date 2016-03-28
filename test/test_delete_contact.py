# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

# def test_edit_first_contact(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create(Contact(firstname="Contact"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     assert len(old_contact) - 1 == app.contact.count_contact()
#     new_contact = app.contact.get_contact_list()
#     old_contact[0:1] = []
#     assert old_contact == new_contact


def test_delete_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Contact"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact