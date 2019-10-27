from sys import maxsize


class Contact:

    def __init__(self, name=None, m_name=None, l_name=None, n_name=None, title=None, company=None, address=None,
                 all_phones_from_home_page=None, home_phone=None, mobile_phone=None, work_phone=None, fax_number=None,
                 all_emails_from_home_page=None, email_1=None, email_2=None, email_3=None, homepage=None,
                 second_address=None, secondary_phone=None, notes=None, id=None):
        self.name = name
        self.m_name = m_name
        self.l_name = l_name
        self.n_name = n_name
        self.title = title
        self.company = company
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_number = fax_number
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.second_address = second_address
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.l_name)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and (self.name == other.name)
                and (self.l_name == other.l_name))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
