from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="test_text_modify", id=random_group.id)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(random_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test_group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify(Group(header="test_text_modify"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
