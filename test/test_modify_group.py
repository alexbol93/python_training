from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify(Group(name="test_text_modify"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify(Group(header="test_text_modify"))
