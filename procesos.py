# -*- coding: utf-8 -*-
"""procesos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T40i7H_dNuwYz0yxEIHwfgfI5BWjketM
"""

class Actividad:
  def __init__(self, nombre, descripcion, objetivo, roles, artefactosEntrada, artefactoSalida):
    self.nombre = nombre
    self.descripcion = descripcion
    self.objetivo = objetivo
    self.roles = roles
    self.artefactosEntrada = artefactosEntrada
    self.artefactoSalida = artefactoSalida

class aplicacion:
  def __init__(self, tipoUsuario, funcionalidades, plataforma, interfaz, lenguajeProgramacion, pruebas, tiendaApp, marketing):
    self.tipoUsuario = tipoUsuario
    self.funcionalidades = funcionalidades
    self.plataforma = plataforma
    self.interfaz = interfaz
    self.lenguajeProgramacion = lenguajeProgramacion
    self.pruebas = pruebas
    self.tiendaApp = tiendaApp
    self.marketing = marketing

class Respuesta:
  def __init__(self, id, categoria, respuesta):
    self.id = id
    self.categoria = categoria
    self.respuesta = respuesta

class Pregunta:
  def __init__(self, id, categoria, enunciado, opciones):
    self.id = id
    self.categoria = categoria
    self.enunciado = enunciado
    self.opciones = opciones

class PuntoVariacion:
  def __init__(self, actividad, categoria, alternativa, respuestaComparativa):
    self.actividad = actividad
    self.categoria = categoria
    self.alternativa = alternativa
    self.respuestaComparativa = respuestaComparativa

class Usuario:
  def __init__(self, nombre,correo,nombreApp):
    self.nombre = nombre
    self.correo = correo
    self.nombreApp = nombreApp

  def solicitar_credenciales(self):
        """Solicita al usuario su nombre, correo y nombre de la app y los guarda en el objeto."""
        self.nombre = input("Ingrese su nombre: ")
        self.correo = input("Ingrese su correo electrónico: ")
        self.nombreApp = input("Ingrese el nombre de la aplicación: ")

  def imprimir_credenciales(self):
        """Imprime las credenciales del usuario."""
        print(f"Nombre: {self.nombre}")
        print(f"Correo electrónico: {self.correo}")
        print(f"Nombre de la aplicación: {self.nombreApp}")

actividad1 = Actividad(
    nombre = "Análisis de requisitos",
    descripcion ="Definir las necesidades y funcionalidades de la aplicación.",
    objetivo = "Entender las expectativas del usuario y las características del mercado.",
    roles ="Analista de requisitos, gerente de producto.",
    artefactosEntrada = "Casos de uso, historias de usuario.",
    artefactoSalida = "Especificación de requisitos."
  )

actividad2 = Actividad(
    nombre = "Diseño",
    descripcion ="Diseñar la arquitectura, la interfaz de usuario y la experiencia de usuario de la aplicación",
    objetivo = "Crear una aplicación intuitiva, atractiva y eficiente.",
    roles ="Diseñador UX/UI, arquitecto de software.",
    artefactosEntrada = "Especificación de requisitos.",
    artefactoSalida = "Prototipos, wireframes, mockups."
  )

actividad3 = Actividad(
    nombre = "Implementación",
    descripcion ="Desarrollar el código fuente de la aplicación.",
    objetivo = "Crear una aplicación robusta, escalable y segura.",
    roles ="Desarrolladores de software, ingenieros de QA.",
    artefactosEntrada = "Prototipos, wireframes, mockups.",
    artefactoSalida = "Código fuente, pruebas unitarias."
  )

actividad4 = Actividad(
    nombre = "Pruebas",
    descripcion ="Realizar pruebas de funcionalidad, rendimiento y seguridad de la aplicación.",
    objetivo = "Asegurar la calidad de la aplicación antes de su lanzamiento.",
    roles ="Ingenieros de QA, testers.",
    artefactosEntrada = "Código fuente, pruebas unitarias.",
    artefactoSalida = "Informe de pruebas."
  )

actividad5 = Actividad(
    nombre = "Lanzamiento",
    descripcion ="Publicar la aplicación en las tiendas de aplicaciones.",
    objetivo = "Poner la aplicación a disposición de los usuarios.",
    roles ="Gerente de producto, equipo de marketing.",
    artefactosEntrada = "Aplicación finalizada.",
    artefactoSalida = "Aplicación disponible en las tiendas de aplicaciones."
  )

pregunta1 = Pregunta(
    id=1,  # Identificador único de la pregunta
    categoria="Público",  # Categoría a la que pertenece la pregunta
    enunciado="¿A qué público estará destinada tu aplicación?",  # Enunciado de la pregunta
    opciones=["Todos", "Un sector en especial"],  # Lista de opciones disponibles
)

pregunta2 = Pregunta(
    id=2,  # Identificador único de la pregunta
    categoria="Funcionalidades basicas",  # Categoría a la que pertenece la pregunta
    enunciado="¿Que tipo de funcionalidades basicas tendra su aplicacion ?",  # Enunciado de la pregunta
    opciones=["Mensajes de texto, voz, imagenes", "chats grupales, canales de difusion"],  # Lista de opciones disponibles
)

pregunta3 = Pregunta(
    id=3,  # Identificador único de la pregunta
    categoria="Funcionalidades avanzadas",  # Categoría a la que pertenece la pregunta
    enunciado="¿Que tipo de funcionalidades avanzadas tendra su aplicacion ?",  # Enunciado de la pregunta
    opciones=["Videollamadas", "Pagos integrados"],  # Lista de opciones disponibles
)

pregunta4 = Pregunta(
    id=4,  # Identificador único de la pregunta
    categoria="Plataforma",  # Categoría a la que pertenece la pregunta
    enunciado="¿En que plataforma estara disponible tu aplicacion ?",  # Enunciado de la pregunta
    opciones=["iOS", "web", "android","Todos"],  # Lista de opciones disponibles
)

pregunta5 = Pregunta(
    id=5,  # Identificador único de la pregunta
    categoria="Interfaz",  # Categoría a la que pertenece la pregunta
    enunciado="¿La interfaz de usuario sera de tipo ?",  # Enunciado de la pregunta
    opciones=["Personalizable","Minimalista"],  # Lista de opciones disponibles
)
pregunta6 = Pregunta(
    id=6,  # Identificador único de la pregunta
    categoria="Pruebas Usuarios",  # Categoría a la que pertenece la pregunta
    enunciado="¿La aplicacion sera probada por usuarios selecionados del publico en general antes de su lanzamiento ?",  # Enunciado de la pregunta
    opciones=["Si","No"],  # Lista de opciones disponibles
)
pregunta7 = Pregunta(
    id=7,  # Identificador único de la pregunta
    categoria="Marketing",  # Categoría a la que pertenece la pregunta
    enunciado="¿Que tipo de marketing tendra la aplicacion?",  # Enunciado de la pregunta
    opciones=["Online", "Offline"],  # Lista de opciones disponibles
)

usuario = Usuario(None, None, None)  # Objeto inicializado con valores nulos
usuario.solicitar_credenciales()  # Solicita datos al usuario

def imprimir_resumen(respuestas):
    """Imprime un resumen de las respuestas del usuario."""
    print(f"Cliente\n")
    usuario.imprimir_credenciales()
    print(f"\nEspecificaciones del cliente para la aplicacion")
    for respuesta in respuestas:
        print(f"- {respuesta.categoria}: {respuesta.respuesta}")

def presentar_pregunta(pregunta, respuestas):
    """Presenta la pregunta al usuario, obtiene su respuesta y la guarda en el vector de respuestas."""
    print(f"\nCategoría: {pregunta.categoria}")
    print(f"Enunciado: {pregunta.enunciado}")
    for i, opcion in enumerate(pregunta.opciones):
        print(f"{i+1}. {opcion}")

    # Obtener respuesta del usuario
    respuesta_usuario = input("Ingrese su respuesta (número de opción): ")

    try:
        # Convertir la respuesta a entero
        respuesta_usuario = int(respuesta_usuario) - 1

        # Validar rango de respuesta
        if 0 <= respuesta_usuario < len(pregunta.opciones):
            respuesta_seleccionada = pregunta.opciones[respuesta_usuario]

            # Crear objeto Respuesta
            nueva_respuesta = Respuesta(
                id=len(respuestas) + 1,
                categoria=pregunta.categoria,
                respuesta=respuesta_seleccionada
            )

            # Agregar objeto Respuesta al vector
            respuestas.append(nueva_respuesta)
            """print(f"Respuesta guardada: {respuesta_seleccionada}")"""
        else:
            print("Opción inválida. Intente nuevamente.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")



preguntas = [pregunta1, pregunta2, pregunta3, pregunta4,  pregunta5, pregunta6, pregunta7]  # Vector de preguntas ya creado
respuestas = []  # Vector de respuestas vacío

# Presentar y guardar respuestas para cada pregunta
print(f"\nPREFERENCIAS DEL CLIENTE")
print(f"----------------------------")
print(f"\nResponda las siguientes preguntas con el fin de establecer las preferencias y aspectos que espera ud de la aplicacion a desarrollar")
for pregunta in preguntas:
    presentar_pregunta(pregunta, respuestas)

def imprimirDescVar(punto_variacion):
    print("Reglas de adaptacion para los puntos de variacion")
    print(f"\nActividad: {punto_variacion.actividad.nombre}")
    print(f"Descripción: {punto_variacion.actividad.descripcion}")
    print(f"Objetivo: {punto_variacion.actividad.objetivo}")
    print(f"\nRoles: {punto_variacion.actividad.roles}")
    print(f"Para la categoria: {punto_variacion.categoria}")
    print(f"La opcion escogida por el usuario para {punto_variacion.respuestaComparativa.categoria} es: {punto_variacion.respuestaComparativa.respuesta}")

punto_variacion1 = PuntoVariacion(actividad1, "Tipo usuario", "",respuestas[0])
punto_variacion2 = PuntoVariacion(actividad1, "Funcionalidades", "",respuestas[2])
punto_variacion3 = PuntoVariacion(actividad2, "Plataforma", "",respuestas[3])
punto_variacion4 = PuntoVariacion(actividad2, "Estilo Interfaz", "",respuestas[4])
punto_variacion5 = PuntoVariacion(actividad3, "Lenguaje de programacion", "",respuestas[3])
punto_variacion6 = PuntoVariacion(actividad3, "Framework de desarrollo", "",respuestas[3])
punto_variacion7 = PuntoVariacion(actividad4, "Tipo de pruebas", "",respuestas[5])
punto_variacion8 = PuntoVariacion(actividad4, "Nivel de automatizacion", "",respuestas[5])
punto_variacion9 = PuntoVariacion(actividad5, "Tienda de aplicaciones", "",respuestas[3])
punto_variacion10 = PuntoVariacion(actividad5, "Estrategia Marketing", "",respuestas[6])

punto_variaciones = [
  punto_variacion1,
  punto_variacion2,
  punto_variacion3,
  punto_variacion4,
  punto_variacion5,
  punto_variacion6,
  punto_variacion7,
  punto_variacion8,
  punto_variacion9,
  punto_variacion10
]

def reglasAdaptacion(punto_variacion):
  """Asigna el valor de la variable `alternativa` en un objeto `PuntoVariacion`."""
  imprimirDescVar(punto_variacion)
  if punto_variacion.categoria == "Tipo usuario":
    if punto_variacion.respuestaComparativa.respuesta == "Todos":
      punto_variacion.alternativa = "Usuarios personales"
    else:
      punto_variacion.alternativa = "Usuarios profesionales"

  elif punto_variacion.categoria == "Funcionalidades":
    if punto_variacion.respuestaComparativa.respuesta == "Videollamadas":
      punto_variacion.alternativa = "Funcionalidades avanzadas"
    else:
      punto_variacion.alternativa = "Funcionalidades avanzadas"

  elif punto_variacion.categoria == "Plataforma":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "iOS"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "Web"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Android"
    else:
      punto_variacion.alternativa = "Todas"

  elif punto_variacion.categoria == "Estilo Interfaz":
    if punto_variacion.respuestaComparativa.respuesta == "Personalizable":
      punto_variacion.alternativa = "Personalizable"
    else:
      punto_variacion.alternativa = "Minimalista"

  elif punto_variacion.categoria == "Lenguaje de programacion":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "Swift"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "JavaScript"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Android Studio"
    else:
      punto_variacion.alternativa = "JavaScript"

  elif punto_variacion.categoria == "Framework de desarrollo":
    if punto_variacion.respuestaComparativa.respuesta == "Todos":
      punto_variacion.alternativa = "Multiplataforma (React Native, Flutter)"
    else:
      punto_variacion.alternativa = "Nativo"

  elif punto_variacion.categoria == "Tipo de pruebas":
    if punto_variacion.respuestaComparativa.respuesta == "No":
      punto_variacion.alternativa = "Pruebas unitarias"
    else:
      punto_variacion.alternativa = "Pruebas de aceptación"

  elif punto_variacion.categoria == "Nivel de automatizacion":
    if punto_variacion.respuestaComparativa.respuesta == "No":
      punto_variacion.alternativa = "Pruebas manuales"
    else:
      punto_variacion.alternativa = "Pruebas automatizadas"

  elif punto_variacion.categoria == "Tienda de aplicaciones":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "App Store"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "URL"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Google Play Store"
    else:
      punto_variacion.alternativa = "Todas las tiendas"

  elif punto_variacion.categoria == "Estrategia Marketing":
    if punto_variacion.respuestaComparativa.respuesta == "Online":
      punto_variacion.alternativa = "Marketing online"
    else:
      punto_variacion.alternativa = "Marketing offline"

  print(f"\nAlternativa: {punto_variacion.alternativa}")
  print(f"\n --------------------------------------------------------------------")

for punto_variacion in punto_variaciones:
  reglasAdaptacion(punto_variacion)

def imprimirAlternativa(punto_variacion):
  """Asigna el valor de la variable `alternativa` en un objeto `PuntoVariacion`."""
  if punto_variacion.categoria == "Tipo usuario":
    if punto_variacion.respuestaComparativa.respuesta == "Todos":
      punto_variacion.alternativa = "Usuarios personales"
    else:
      punto_variacion.alternativa = "Usuarios profesionales"

  elif punto_variacion.categoria == "Funcionalidades":
    if punto_variacion.respuestaComparativa.respuesta == "Videollamadas":
      punto_variacion.alternativa = "Funcionalidades avanzadas"
    else:
      punto_variacion.alternativa = "Funcionalidades avanzadas"

  elif punto_variacion.categoria == "Plataforma":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "iOS"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "Web"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Android"
    else:
      punto_variacion.alternativa = "Todas"

  elif punto_variacion.categoria == "Estilo Interfaz":
    if punto_variacion.respuestaComparativa.respuesta == "Personalizable":
      punto_variacion.alternativa = "Personalizable"
    else:
      punto_variacion.alternativa = "Minimalista"

  elif punto_variacion.categoria == "Lenguaje de programacion":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "Swift"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "JavaScript"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Android Studio"
    else:
      punto_variacion.alternativa = "JavaScript"

  elif punto_variacion.categoria == "Framework de desarrollo":
    if punto_variacion.respuestaComparativa.respuesta == "Todos":
      punto_variacion.alternativa = "Multiplataforma (React Native, Flutter)"
    else:
      punto_variacion.alternativa = "Nativo"

  elif punto_variacion.categoria == "Tipo de pruebas":
    if punto_variacion.respuestaComparativa.respuesta == "No":
      punto_variacion.alternativa = "Pruebas unitarias"
    else:
      punto_variacion.alternativa = "Pruebas de aceptación"

  elif punto_variacion.categoria == "Nivel de automatizacion":
    if punto_variacion.respuestaComparativa.respuesta == "No":
      punto_variacion.alternativa = "Pruebas manuales"
    else:
      punto_variacion.alternativa = "Pruebas automatizadas"

  elif punto_variacion.categoria == "Tienda de aplicaciones":
    if punto_variacion.respuestaComparativa.respuesta == "iOS":
      punto_variacion.alternativa = "App Store"
    elif punto_variacion.respuestaComparativa.respuesta == "web":
      punto_variacion.alternativa = "URL"
    elif punto_variacion.respuestaComparativa.respuesta == "android":
      punto_variacion.alternativa = "Google Play Store"
    else:
      punto_variacion.alternativa = "Todas las tiendas"

  elif punto_variacion.categoria == "Estrategia Marketing":
    if punto_variacion.respuestaComparativa.respuesta == "Online":
      punto_variacion.alternativa = "Marketing online"
    else:
      punto_variacion.alternativa = "Marketing offline"

  print(f"{punto_variacion.categoria}: {punto_variacion.alternativa}")

imprimir_resumen(respuestas)
print(f"\nPROCESO ADAPTADO")
print(f"Epecificaciones para el desarollo de: {usuario.nombreApp}\n")
for punto_variacion in punto_variaciones:
  imprimirAlternativa(punto_variacion)