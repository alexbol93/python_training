# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    contact = Contact(name="Alex_m", m_name="John_m", l_name="Johnson_m", n_name="s_Jhon_m",
                                             title="sometitle_m", company="compnyname_m", address="someaddress_m",
                                             home_phone="4213123_m", mobile_phone="1212_m", work_phone="somework_m",
                                             fax_number="faxnumber_m", email_1="asd_m", email_2="asdasd_m",
                                             email_3="asdasda_m", homepage="asdasdc_m",
                                             second_address="_masdasdasdcxzz_m", secondary_phone="fwklmlsm_m",
                                             notes="skamdlkasmdlakmd_m")
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Alex", m_name="John", l_name="Johnson", n_name="s_Jhon", title="sometitle",
                               company="compnyname", address="someaddress", home_phone="4213123", mobile_phone="1212",
                               work_phone="somework", fax_number="faxnumber", email_1="asd", email_2="asdasd",
                               email_3="asdasda", homepage="asdasdc", second_address="asdasdasdcxzz",
                               secondary_phone="fwklmlsm", notes="skamdlkasmdlakmd"))
        app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.return_to_home_page()
