from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Test_user", l_name="testlastname"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    groups = orm.get_group_list()

    contact = None
    # Цикл по списку групп, который найдет первую непустую группу
    for group in groups:
        contacts = orm.get_contacts_in_group(group)
        if len(contacts) == 0:
            continue
        else:
            group_with_contact = group
            contact = contacts[0]
            break

    # Если цикл прошел и все группы пустые то берем случайный контакт и помещаем его в случайную группу
    if contact is None:
        group_with_contact = random.choice(orm.get_group_list())
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_in_group(contact.id, group_with_contact.id)

    app.contact.del_user_from_group(contact.id, group_with_contact.id)
    new_users = orm.get_contacts_in_group(group)
    assert contact not in new_users  # Проверяем что пользователь удален из группы


