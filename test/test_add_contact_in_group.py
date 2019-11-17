from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, orm):
    if app.group.count() == 0: # Если нет группы - создаем
        app.group.create(Group(name="test_group"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(group) # Получаем список контактов которых нет в выбраной группе - если таких нет, создаем новый контакт
    if contacts == []:
        app.contact.create(Contact(name="Alex", m_name="John", l_name="Johnson", n_name="s_Jhon", title="sometitle",
                               company="compnyname", address="someaddress", home_phone="4213123", mobile_phone="1212",
                               work_phone="somework", fax_number="faxnumber", email_1="asd", email_2="asdasd",
                               email_3="asdasda", homepage="asdasdc", second_address="asdasdasdcxzz",
                               secondary_phone="fwklmlsm", notes="skamdlkasmdlakmd"))
        contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(contacts)
    else:
        contact = random.choice(contacts)
    app.contact.add_contact_in_group(contact.id, group.id) # Добавляем контакт в выбраную группу
    contacts_in_group = orm.get_contacts_in_group(group)# Выгружаем список контактов в группе
    assert contact in contacts_in_group # Проверяем что контакт есть в группе
