# -*- coding: utf-8 -*-


from zadanie7.model.contact import Contact


def test_add_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_address_page(Contact(firstname="qqq", middlename="wwwwww", lastname="eeeeee", nickname="rrrrrrr", title="tttttt",
                               company="yyyyyyyy", address="uuuuuuu", home="iiiiii", mobile="ooooooooo", work="pppppp", fax="gggggg",
                               email2="aaaaaa", email3="ssssssss", homepage="ddddddd", byear="2000", ayear="2000",
                               address2="ffffff", phone2="gggggggg", notes="hhhhhhh"))
    app.session.logout()