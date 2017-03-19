from model.contact import Contact
from random import randrange
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf", company="fsfdfdf",
                address="4242", home="3424", mobile="2344", work="4234",
                fax="43244", email="434234", email2="3424", email3="4234", homepage="423424", byear="1199",
                ayear="2423", address2="324eeee", phone2="324rew",
                notes="324erwsd"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
