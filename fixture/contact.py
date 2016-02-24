
from model.contact import Contact
import re

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

    def create(self, contacts):
        wd = self.app.wd
        self.open_add_address_page()
        self.fill_address_page(contacts)
        # enter contact
        wd.find_element_by_xpath(".//*[@id='content']/form/input[1]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_address_page(self, contacts):
        wd = self.app.wd
        # self.open_add_address_page()
        # fill address page
        self.fill_address_form(contacts)
        # wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_address_form(self, contacts):
        wd = self.app.wd
        self.change_field_value("firstname", contacts.firstname)
        self.change_field_value("middlename", contacts.middlename)
        self.change_field_value("lastname", contacts.lastname)
        self.change_field_value("nickname", contacts.nickname)
        self.change_field_value("title", contacts.title)
        self.change_field_value("company", contacts.company)
        self.change_field_value("address", contacts.address)
        self.change_field_value("home", contacts.home)
        self.change_field_value("mobile", contacts.mobile)
        self.change_field_value("work", contacts.work)
        self.change_field_value("fax", contacts.fax)
        self.change_field_value("email2", contacts.email2)
        self.change_field_value("email3", contacts.email3)
        self.change_field_value("homepage", contacts.homepage)
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # self.change_field_value("byear", contact.ayear)
        # self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contacts.address2)
        self.change_field_value("phone2", contacts.phone2)
        self.change_field_value("notes", contacts.notes)

    def open_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    # def open_edit_contact_by_index(self,index):
    #     wd = self.app.wd
    #     wd.find_elements_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img")[index].click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # open edit contact
        self.open_contact_to_edit_by_index(index)
        # self.open_edit_contact_by_index(index)
        # fill address page
        self.fill_address_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        #select first contact
        self.select_contact_by_index(index)
        #delete first contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                fio1 = element.find_element_by_name("selected[]").get_attribute("title")
                fio = fio1[8:-1]
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(id=id, fio=fio))
        return list(self.contact_cache)

    def get_contact_list_al(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_email=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, address=address, email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)