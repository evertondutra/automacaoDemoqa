from behave import given, when, then
from utils import Utils
from results import Results
from preenche import Preenche
from nose.tools import assert_true

# Estanciando a classe
utils = Utils()
preenche = Preenche()
results = Results()


@given(u'acesso a página demoqa')
def step_impl(context):
    # 1ª ação: navegar até o site para automação
    utils.navegar('https://demoqa.com/text-box')


@given(u'preencho o formulario')
def step_impl(context):
    # 2ª ação: Preencher os campos
    preenche.name('Teste Teste')
    preenche.email('teste.teste@teste.com')
    preenche.address('Cidade Teste')
    preenche.perAddress('Cidade TesteTeste')


@when(u'clico no botão submit')
def step_impl(context):
    # 3ª ação: Clicar no botão Submit
    preenche.cl_btn()


@then(u'devo visualizar resultado')
def step_impl(context):
    # 4ª acão: verificar resultado
    assert_true(results.get_text(), 'Nenhum campo foi preenchido')
