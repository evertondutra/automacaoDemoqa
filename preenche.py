from browser import Browser


class PreencheElementos(object):
    idName = 'userName'
    idEmail = 'userEmail'
    idAddress = 'currentAddress'
    IdPermanentAddress = 'permanentAddress'
    botomSubmit = 'submit'

# Classe com funções identificando elemento na página e executando ações
class Preenche(Browser):
    def name(self, name):
        self.driver.find_element_by_id(PreencheElementos.idName).send_keys(name)

    def email(self, email):
        self.driver.find_element_by_id(PreencheElementos.idEmail).send_keys(email)

    def address(self, address):
        self.driver.find_element_by_id(PreencheElementos.idAddress).send_keys(address)

    def per_address(self, per_address):
        self.driver.find_element_by_id(PreencheElementos.IdPermanentAddress).send_keys(per_address)

    # clicar no botão submit
    def cl_btn(self):
        self.driver.find_element_by_id(PreencheElementos.botomSubmit).click()
