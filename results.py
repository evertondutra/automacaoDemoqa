from browser import Browser


# Extendendo a classe Browser para verificar o resultado
class Results(Browser):
    def get_text(self):
        return self.driver.find_element_by_id('output').text
