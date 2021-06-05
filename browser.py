from selenium import webdriver


# criando a classe browser para poder ser usada em outros steps
class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()

