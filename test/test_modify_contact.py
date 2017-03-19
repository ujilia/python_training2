# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first firstname", lastname="first lastname"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = "Changed firstname"
    contact.lastname = "Changed lastname"
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
