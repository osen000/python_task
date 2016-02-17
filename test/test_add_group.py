# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group1", header="group1", footer="group1")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_empty_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

