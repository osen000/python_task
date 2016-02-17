from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email2=None, email3=None, homepage=None,
                 address2=None, phone2=None, notes=None, id=None, fio=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        # self.byear = byear
        # self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.fio = fio

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s" % (self.id, self.fio)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.fio is None or other.fio is None or self.fio == other.fio)
