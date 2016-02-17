# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_address(app):
    old_contact = app.contact.get_contact_list()
    contacts = Contact(firstname="qqq", middlename="wwwwww", lastname="eeeeee", nickname="rrrrrrr", title="tttttt",
                               company="yyyyyyyy", address="uuuuuuu", home="iiiiii", mobile="ooooooooo", work="pppppp", fax="gggggg",
                               email2="aaaaaa", email3="ssssssss", homepage="ddddddd", address2="ffffff", phone2="gggggggg",
                               notes="hhhhhhh")
    app.contact.create(contacts)
    assert len(old_contact) + 1 == app.contact.count_contact()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contacts)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

# def test_add_address_firstname(app):
#     app.contact.create(Contact(firstname="qqq"))