# -*- coding: utf-8 -*-
from model.group import Group


# def test_modify_first_group(app):
#   app.group.modify_first_group(Group(name="new", header="change", footer="new change"))
#   app.group.return_to_groups_page()
#   app.session.logout()


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))