from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
