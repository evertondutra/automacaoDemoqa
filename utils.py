from browser import Browser


# Esta classe esta extendendo a classe Browser e adicionando a função navegar
class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)
