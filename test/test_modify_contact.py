# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="Alex_m", m_name="John_m", l_name="Johnson_m", n_name="s_Jhon_m",
                                             title="sometitle_m", company="compnyname_m", address="someaddress_m",
                                             home_phone="4213123_m", mobile_phone="1212_m", work_phone="somework_m",
                                             fax_number="faxnumber_m", email_1="asd_m", email_2="asdasd_m",
                                             email_3="asdasda_m", homepage="asdasdc_m",
                                             second_address="_masdasdasdcxzz_m", secondary_phone="fwklmlsm_m",
                                             notes="skamdlkasmdlakmd_m"))
    app.return_to_home_page()
    app.session.logout()