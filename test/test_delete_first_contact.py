# -*- coding: utf-8 -*-


def test_edit_first_contact(app):
    app.contact.delete_first_contact()