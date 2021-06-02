from browser import Browser


class Preenche(Browser):
    def name(self, name):
        self.driver.find_element_by_id('userName').send_keys(name)

    def email(self, email):
        self.driver.find_element_by_id('userEmail').send_keys(email)

    def address(self, address):
        self.driver.find_element_by_id('currentAddress').send_keys(address)

    def perAddress(self, perAddress):
        self.driver.find_element_by_id('permanentAddress').send_keys(perAddress)

    # clicar no botão submit
    def cl_btn(self):
        self.driver.find_element_by_id('submit').click()
