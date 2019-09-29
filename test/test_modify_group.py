from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="test_modify", header="test_text_modify", footer="test_text_modify"))
    app.session.logout()