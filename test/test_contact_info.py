from model.contact import Contact
import re

def test_contact_info(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_db) == len(contact_from_home_page)
    for c in range(len(contact_from_db)):
        assert contact_from_home_page[c].id == contact_from_db[c].id
        assert contact_from_home_page[c].firstname == contact_from_db[c].firstname
        assert contact_from_home_page[c].lastname == contact_from_db[c].lastname
        assert contact_from_home_page[c].address == contact_from_db[c].address
        assert contact_from_home_page[c].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[c])
        assert contact_from_home_page[c].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[c])

def clear_phone(s):
    return re.sub("[() -]", "", s)


def clear_email(s1):
    return re.sub("[() ]", "", s1)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


# def test_contact_info(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#
#
# def clear_phone(s):
#     return re.sub("[() -]", "", s)
#
#
# def clear_email(s1):
#     return re.sub("[() ]", "", s1)
#
#
# def merge_phones_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear_phone(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))
#
#
# def merge_emails_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear_email(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.email, contact.email2, contact.email3]))))


