from browser import Browser


# criando uma classe com a função navegar
class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)
