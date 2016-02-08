# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_address(app):
    app.contact.create(Contact(firstname="qqq", middlename="wwwwww", lastname="eeeeee", nickname="rrrrrrr", title="tttttt",
                               company="yyyyyyyy", address="uuuuuuu", home="iiiiii", mobile="ooooooooo", work="pppppp", fax="gggggg",
                               email2="aaaaaa", email3="ssssssss", homepage="ddddddd", address2="ffffff", phone2="gggggggg",
                               notes="hhhhhhh"))


def test_add_address(app):
    app.contact.fill_address_page(Contact(firstname="qqq"))