# Created by emiliano at 14/1/20
Feature: Netflix

  @test00
  Scenario: validarTituloTest
    Given El usuario navega a la página: "https://www.netflix.com/ar/"
    When Espero a que cargue la pagina
    Then Valido titulo: "Netflix Argentina: Ve series online, ve películas online"

  @test01
  Scenario: startSessionPageTest
    Given El usuario navega a la página: "https://www.netflix.com/ar/"
    When El usuario hace click en Iniciar Sesión
    And Valido titulo: "Netflix"
    And Valido texto: "Inicia sesión"
    Then Valido texto: "Iniciar sesión con Facebook"

