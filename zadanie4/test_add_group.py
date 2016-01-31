# -*- coding: utf-8 -*-


import pytest
from zadanie4.group import Group
from zadanie4.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group1", header="group1", footer="group1"))
    app.logout()


def test_empty_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


