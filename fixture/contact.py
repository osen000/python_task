

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_address_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_address_page()
        self.fill_address_page(contact)
        # enter contact
        wd.find_element_by_xpath(".//*[@id='content']/form/input[1]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_address_page(self, contact):
        wd = self.app.wd
        # self.open_add_address_page()
        # fill address page
        self.fill_address_form(contact)
        # wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_address_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # self.change_field_value("byear", contact.ayear)
        # self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # open edit contact
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill address page
        self.fill_address_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete first contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()


    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))