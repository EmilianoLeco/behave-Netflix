Feature: Inicio de sesion
  # Validacion de msj de error de inicio de sesion

  @test02
  Scenario Outline: loginToNetflixErrorTest
    Given El usuario navega a la página: "https://www.netflix.com/ar/"
    When El usuario hace click en Iniciar Sesión
    And Ingresa el siguiente email: "BmOxGGL@gmail.com"
    And Ingresa la siguiente contraseña: "holamundo"
    And Desmarca el botón de "Recuerdame"
    And Realiza click en "Iniciar Sesión"
    Then Valida mensaje de error: "<MSG>"
    And Valida boton "Recuerdame" seleccionado
    Examples:
      | MSG                                                                                               |
      | No podemos encontrar una cuenta con esta dirección de email. Reinténtalo o crea una cuenta nueva. |

  @test03
  Scenario: fakeEmailTest
    Given El usuario navega a la página: "https://www.netflix.com/ar/"
    When El usuario ingresa un email en el LandingPage
    And El usuario hace click en "Comenzar"
    Then Es dirigido a la pagina de registro



