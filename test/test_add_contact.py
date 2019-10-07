# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="Alex", m_name="John", l_name="Johnson", n_name="s_Jhon", title="sometitle",
                               company="compnyname", address="someaddress", home_phone="4213123", mobile_phone="1212",
                               work_phone="somework", fax_number="faxnumber", email_1="asd", email_2="asdasd",
                               email_3="asdasda", homepage="asdasdc", second_address="asdasdasdcxzz",
                               secondary_phone="fwklmlsm", notes="skamdlkasmdlakmd"))
    app.return_to_home_page()

