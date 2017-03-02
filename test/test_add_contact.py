# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + " "*5 + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5 + ","*5 + "."*5 + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@" + "-"*5 + "."*5 + "_"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_name("firstname", 15), lastname=random_name("lastname", 15),
            address=random_address("address", 30), home=random_phone("home", 10),
            mobile=random_phone("mobile", 10), work=random_phone("work", 10),
            fax=random_phone("fax", 10), email=random_email("email", 40),
            email2=random_email("email2", 40), email3=random_email("email3", 40),
            address2=random_address("address2", 30), phone2=random_phone("phone2", 10))
    for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
