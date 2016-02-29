from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname = random_string("nickname", 10),
                    title = random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_string("home", 10),
                    mobile=random_string("mobile", 10), work=random_string("work", 10),
                    fax=random_string("fax", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                    address2=random_string("address2", 10),phone2=random_string("phone2", 10),notes=random_string("notes", 10))
            for i in range(3)
]
