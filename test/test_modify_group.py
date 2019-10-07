from model.group import Group


def test_modify_group_name(app):
    app.group.modify(Group(name="test_text_modify"))


def test_modify_group_header(app):
    app.group.modify(Group(header="test_text_modify"))
