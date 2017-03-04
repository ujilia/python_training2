# -*- coding: utf-8 -*-
from model.contact import Contact
# import random
# import string


testdata = [
    Contact(firstname="firstname1", lastname="lastname1",
            address="address1", home="home1",
            mobile="mobile1", work="work1",
            fax="fax1", email="email1",
            email2="email2_2", email3="email3_3",
            address2="address2_2", phone2="phone2_2")
    # Contact(firstname="firstname2", lastname="lastname2",
    #         address="address2", home="home2",
    #         mobile="mobile2", work="work2",
    #         fax="fax2", email="email2",
    #         email2="email2_2_2", email3="email3_3_3",
    #         address2="address2_2_2", phone2="phone2_2_2")
]

# def random_name(prefix, maxlen):
#     symbols = string.ascii_letters + " "*5 + "-"*5
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_address(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " "*5 + ","*5 + "."*5 + "-"*5
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_phone(prefix, maxlen):
#     symbols = string.digits + "-"*5
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_email(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + "@" + "-"*5 + "."*5 + "_"*5
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

