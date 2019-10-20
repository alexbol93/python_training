from model.group import Group


def test_modify_group_name(app):
    group = Group(name="test_text_modify")
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="test_text_modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
