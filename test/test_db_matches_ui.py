from model.group import Group
import re
from timeit import timeit


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=''.join(group.name.strip().split()))

    db_list = list(map(clean, db.get_group_list()))
    ui_list = list(map(clean, ui_list))

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# def test_group_list(app, db):
#     ui_list = app.group.get_group_list()
#
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#
#     db_list = map(clean, db.get_group_list())
#
#     db_list = sorted(db_list, key=Group.id_or_max)
#
#     for group in db_list:
#         group.name = merge_names(group.name)
#
#     assert sorted(ui_list, key=Group.id_or_max) == db_list
#
#
# def clear(s):
#     return re.sub("[() -]", "", s)
#
#
# def merge_names(group):
#     return ' '.join(group.split())
# return "\n".join(filter(lambda x: x != "",
#                         map(lambda x: clear(x),
#                             filter(lambda x: x is not None,
#                                    [group]))))
