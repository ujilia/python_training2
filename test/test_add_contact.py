# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fsff", middlename="fsf", lastname="fsdf", nickname="sdff", title="dsfdsf", company="fsfdfdf", address="4242", home="3424", mobile="2344", work="4234",
                               fax="43244", email="434234", email2="3424", email3="4234", homepage="423424", byear="1199", ayear="2423", address2="324eeee", phone2="324rew",
                               notes="324erwsd"))
    app.contact.return_to_home_page()
    app.session.logout()