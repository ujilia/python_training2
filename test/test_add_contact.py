# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf",
                      company="fsfdfdf",
                      address="4242", home="3424", mobile="2344", work="4234",
                      fax="43244", email="434234", email2="3424", email3="4234", homepage="423424", byear="1199",
                      ayear="2423", address2="324eeee", phone2="324rew",
                      notes="324erwsd")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
