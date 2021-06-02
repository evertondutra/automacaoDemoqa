from browser import Browser


class Preenche(Browser):
    def name(self, name):
        self.driver.find_element_by_id('userName').send_keys(name)
