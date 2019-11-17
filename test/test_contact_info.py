import re
from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    for id in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[id].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[id])
        assert contacts_from_home_page[id].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[id])
        assert contacts_from_home_page[id].name == contacts_from_db[id].name
        assert contacts_from_home_page[id].l_name == contacts_from_db[id].l_name
        assert contacts_from_home_page[id].address == contacts_from_db[id].address


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_phone,  contact.mobile_phone,
                                                                     contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email_1,  contact.email_2, contact.email_3]))