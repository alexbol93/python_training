# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="Alex", m_name="John", l_name="Johnson", n_name="s_Jhon", title="sometitle",
                        company="compnyname", address="someaddress", home_phone="4213123", mobile_phone="1212",
                        work_phone="somework", fax_number="faxnumber", email_1="asd", email_2="asdasd",
                        email_3="asdasda", homepage="asdasdc", second_address="asdasdasdcxzz",
                        secondary_phone="fwklmlsm", notes="skamdlkasmdlakmd"))
    app.return_to_home_page()
    app.logout()

