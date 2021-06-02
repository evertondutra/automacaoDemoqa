from utils import Utils
from preenche import Preenche


# Estanciando a classe
utils = Utils()
preenche = Preenche()

# 1ª ação: navegar até o site para automação
utils.navegar('https://demoqa.com/text-box')

# 2ª ação: Preencher os campos
preenche.name('Teste Teste')
preenche.email('teste.teste@teste.com')


