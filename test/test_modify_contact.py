# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.open_home_page()
    app.contact.modify(Contact(firstname="fsf11f", middlename="fs333f", lastname="dasdd", nickname="4444444", title="hhhhhh", company="rrrrr",
                address="uyyuryi", home="jkji", mobile="23uirehj", work="jhfsdjh",
                fax="1234567", email="99994", email2="32344", email3="lllll", homepage="12wsd", byear="2000",
                ayear="2010", address2="khjjg", phone2="0809775",
                notes="90iuyhgf"))
    app.contact.return_to_home_page()
