# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(minlen, maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen, maxlen))])


testdata = [Contact(name=random_string("name", 10), m_name=random_string("m_name", 10),
                    l_name=random_string("l_name", 10), n_name=random_string("n_name", 10),
                    title=random_string("title", 10), company=random_string("c_name", 10),
                    address=random_string("adress", 10), home_phone=random_number(4, 9), mobile_phone=random_number(4, 9),
                    work_phone=random_number(4, 9), fax_number=random_number(4, 9), email_1=random_string("email@", 10),
                    email_2=random_string("email@", 10), email_3=random_string("email@", 10),
                    homepage=random_string("HP", 10), second_address=random_string("SA", 10),
                    secondary_phone=random_number(4, 9), notes=random_string("notice", 10)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.return_to_home_page()

