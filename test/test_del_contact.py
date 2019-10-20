from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Alex", m_name="John", l_name="Johnson", n_name="s_Jhon", title="sometitle",
                               company="compnyname", address="someaddress", home_phone="4213123", mobile_phone="1212",
                               work_phone="somework", fax_number="faxnumber", email_1="asd", email_2="asdasd",
                               email_3="asdasda", homepage="asdasdc", second_address="asdasdasdcxzz",
                               secondary_phone="fwklmlsm", notes="skamdlkasmdlakmd"))
        app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
    app.return_to_home_page()

