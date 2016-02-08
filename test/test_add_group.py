# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group1", header="group1", footer="group1"))


def test_empty_add_group(app):
    app.group.create(Group(name="", header="", footer=""))

