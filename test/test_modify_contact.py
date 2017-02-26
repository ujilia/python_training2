# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="first firstname", lastname="first lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new firstname", lastname="new lastname")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
