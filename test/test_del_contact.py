from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf", company="fsfdfdf",
                address="4242", home="3424", mobile="2344", work="4234",
                fax="43244", email="434234", email2="3424", email3="4234", homepage="423424", byear="1199",
                ayear="2423", address2="324eeee", phone2="324rew",
                notes="324erwsd"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
