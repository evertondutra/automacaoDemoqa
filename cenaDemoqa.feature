# language: pt

  Funcionalidade: fluxo de preenchimento de formulario

    @demoqa
    Cenário: preencher o formulario do site demoqa
      Dado que acesso o site demoqa.com
      E preencho os input
      Quando clico no botão submit
      Então devo visualizar o resultado do preenchimento