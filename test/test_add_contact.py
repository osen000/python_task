# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_address(app):
    old_contact = app.contact.get_contact_list()
    contacts = Contact(firstname="qqq", middlename="wwwwww", lastname="eeeeee", nickname="rrrrrrr", title="tttttt",
                               company="yyyyyyyy", address="uuuuuuu", home="iiiiii", mobile="ooooooooo", work="pppppp", fax="gggggg",
                               email2="aaaaaa", email3="ssssssss", homepage="ddddddd", address2="ffffff", phone2="gggggggg",
                               notes="hhhhhhh")
    app.contact.create(contacts)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contacts)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    print("h")

# def test_add_address_firstname(app):
#     app.contact.create(Contact(firstname="qqq"))