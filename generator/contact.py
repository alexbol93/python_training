from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


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


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(minlen, maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen, maxlen))])


testdata = [Contact(name=random_string("name", 10), m_name=random_string("m_name", 10),
                    l_name=random_string("l_name", 10), n_name=random_string("n_name", 10),
                    title=random_string("title", 10), company=random_string("c_name", 10),
                    address=random_string("adress", 10), home_phone=random_number(4, 9), mobile_phone=random_number(4, 9),
                    work_phone=random_number(4, 9), fax_number=random_number(4, 9), email_1=random_string("email@", 10),
                    email_2=random_string("email@", 10), email_3=random_string("email@", 10),
                    homepage=random_string("HP", 10), second_address=random_string("SA", 10),
                    secondary_phone=random_number(4, 9), notes=random_string("notice", 10)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
