from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    groups = Group(name="New Group")
    app.group.modify_group_by_id(group.id, groups)
    assert len(old_groups) == app.group.count_group()
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count_group() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New Header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
