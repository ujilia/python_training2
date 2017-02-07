# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf",
                                   company="fsfdfdf",
                                   address="4242", home="3424", mobile="2344", work="4234",
                                   fax="43244", email="434234", email2="3424", email3="4234", homepage="423424",
                                   byear="1199",
                                   ayear="2423", address2="324eeee", phone2="324rew",
                                   notes="324erwsd"))
    app.contact.modify(
        Contact(firstname="6578", middlename="f243rwe", lastname="43567", nickname="45553", title="35478657463524",
                company="7753",
                address="333333", home="34444", mobile="345678", work="2345678",
                fax="1234567", email="99994", email2="32344", email3="2345678", homepage="765", byear="2000",
                ayear="2010", address2="k876574", phone2="0809775",
                notes="3456789"))
    app.contact.return_to_home_page()
