from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Test_user", l_name="testlastname"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    groups = orm.get_group_list()
    group = random.choice(groups)    # Выберем случайную группу
    users_in_group = orm.get_contacts_in_group(group)     # Получаем список пользователей в случайной группе

    if len(users_in_group) == 0:    # Если пользователей нет, добавляем нового
        all_users = orm.get_contact_list()
        user = random.choice(all_users)
        app.contact.add_contact_in_group(user.id, group.id)
    users_in_group = orm.get_contacts_in_group(group)
    user_to_del = random.choice(users_in_group)
    app.contact.del_user_from_group(user_to_del.id, group.id)
    new_users = orm.get_contacts_in_group(group)
    assert user_to_del not in new_users  # Проверяем что пользователь удален из группы


