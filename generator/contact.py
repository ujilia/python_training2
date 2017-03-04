from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + " "*5 + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5 + ","*5 + "."*5 + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + "-"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@" + "-"*5 + "."*5 + "_"*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_name("firstname", 15), lastname=random_name("lastname", 15),
            address=random_address("address", 30), home=random_phone("home", 10),
            mobile=random_phone("mobile", 10), work=random_phone("work", 10),
            fax=random_phone("fax", 10), email=random_email("email", 40),
            email2=random_email("email2", 40), email3=random_email("email3", 40),
            address2=random_address("address2", 30), phone2=random_phone("phone2", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
