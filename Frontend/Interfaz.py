"""Este módulo gestiona toda la lógica requerida para llevar a cabo la administración del Frontend"""

# Importando las librerías y módulos requeridos
import streamlit as st
from Backend import Usuario


# Mostrar interfaz de menú general
def mostrar_menu_general():
    if st.session_state["loggedin"]:
        with mainSection:
            # Muestra información general del proyecto
            st.markdown("# Menú general")
            st.divider()
            st.markdown("### Bienvenido al menú de gestión de citas")
            st.markdown("**Optimiza tu Agenda, Simplifica tu Vida**")
            st.markdown('''*Tu tiempo, reduce el estrés y lleva la gestión de citas a un nivel superior con nuestro programa 
            en línea. Únete a nosotros y experimenta la comodidad y eficacia que solo un sistema de gestión de citas 
            moderno puede ofrecer. ¡Haz que tu agenda trabaje para ti!
            Estos son los servicios que ofrecemos:*''')
            st.markdown('''
            >* :pretty[Creación de citas] 
            >* :pretty[Cancelación de citas]
            >* :pretty[Modificación de citas]
            >* :pretty[Generación de reportes]'''
                        )
            st.markdown("!Anímate a usarlos¡")
            st.divider()
            st.markdown("Autores:")
            st.markdown("* Juan Pablo Mejía Gómez")
            st.markdown("* Yamid Andrés Campo Gallego")
            st.markdown("* Maria Alejandra Echavarria Correa")
            st.markdown("* Esteban Ossa Lopera")


# Mostrar interfaz de inicio de sesión
def mostrar_inicio_sesion():
    with loginSection:
        if not st.session_state["loggedin"]:

            # Crear títulos de página
            st.markdown("# Bienvenido al módulo de gestión de citas :sunglasses:")
            st.markdown("## Por favor ingresa tus datos de inicio de sesión")
            st.divider()
            st.markdown('''
            ##### Credenciales para ingresar al sistema  
            > Usuario: Medico  
            > Contraseña: 12345
            ''')
            st.divider()

            # Crear campos para solicitar datos para almacenarlos en las claves user y password respectivamente
            # del diccionario session_state
            st.session_state.user = st.text_input("Inserte su nombre de usuario")
            st.session_state.password = st.text_input("Inserte su contraseña", type="password")

            # Verifica que el botón de Iniciar sesión haya sido presionado
            if st.button("Iniciar sesión"):

                # Verifica que las credenciales insertadas existan en la base de datos
                if Usuario.verificar_inicio_sesion(st.session_state.user, st.session_state.password):

                    # Actualiza el estado de la variable dentro del diccionario de session_state a true
                    st.session_state["loggedin"] = True

                    # Recarga el código
                    st.rerun()

                else:

                    # Muestra un mensaje de error
                    st.error("Usuario o contraseña incorrectos.")


# Mostrar interfaz de salida de sesión
def mostrar_salida_sesion():
    pass


if __name__ == "__main__":
    # Configurando el título de la página
    st.set_page_config(page_title="Módulo de gestión de citas")

    # Creando contenedores para mostrar el contenido de la app
    headerSection = st.container()
    mainSection = st.container()
    loginSection = st.container()
    logoutSection = st.container()

    # Manejo de transición en inicio de sesión
    with headerSection:
        if "loggedin" not in st.session_state:
            st.session_state["loggedin"] = False
            mostrar_inicio_sesion()
        else:
            if st.session_state["loggedin"]:
                mostrar_menu_general()
                mostrar_salida_sesion()
            else:
                mostrar_inicio_sesion()
