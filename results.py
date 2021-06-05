from browser import Browser


class Results(Browser):
    def get_text(self):
        return self.driver.find_element_by_id('output').text
