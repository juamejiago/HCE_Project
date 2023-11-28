"""Este módulo gestiona toda la lógica requerida para llevar a cabo la administración del Frontend"""

# Importando las librerías y módulos requeridos
import streamlit as st
from Backend import Usuario, Reporte


# Mostrar interfaz de reporte
def mostrar_reporte():
    if st.session_state["reportin"]:
        with reportSection:
            # Muestra información general del servicio de reportes
            st.markdown("# Generación de reportes 📝")
            st.divider()
            st.markdown("### Bienvenido al menú de generación de reportes del módulo de gestión de citas")
            st.markdown("> *Favor seleccione el tipo de reporte que desea generar:* ")

            # Mostrar los reportes de todos los profesionales de salud
            with st.expander("Reporte por profesionales de salud", expanded=False):
                # Obteniendo el json de los pacientes
                profesionales_salud = Reporte.generar_reporte_profesionales_salud()

                # Mostrando el archivo json en la interfaz
                st.json(profesionales_salud, expanded=True)

                # Mostrando el botón para descargar en la interfaz
                st.download_button(
                    label="Descargar JSON",
                    file_name="ProfesionalesSalud.json",
                    mime="application/json",
                    data=profesionales_salud,
                )

            # Mostrar los reportes de todos los pacientes
            with st.expander("Reporte por pacientes", expanded=False):
                # Obteniendo el json de los pacientes
                pacientes_json = Reporte.generar_reporte_pacientes()

                # Mostrando el archivo json en la interfaz
                st.json(pacientes_json, expanded=True)

                # Mostrando el botón para descargar en la interfaz
                st.download_button(
                    label="Descargar JSON",
                    file_name="Pacientes.json",
                    mime="application/json",
                    data=pacientes_json,
                )

            # Mostrar los reportes de todas las instalaciones
            with st.expander("Reporte por instalaciones", expanded=False):
                # Obteniendo el json de las instalaciones
                instalaciones_json = Reporte.generar_reporte_instalaciones()

                # Mostrando el archivo json en la interfaz
                st.json(instalaciones_json, expanded=True)

                # Mostrando el botón para descargar en la interfaz
                st.download_button(
                    label="Descargar JSON",
                    file_name="Instalaciones.json",
                    mime="application/json",
                    data=instalaciones_json,
                )

            # Mostrar los reportes de todos las citas
            with st.expander("Reporte por citas", expanded=False):
                # Obteniendo el json de las citas
                citas_json = Reporte.generar_reporte_citas()

                # Mostrando el archivo json en la interfaz
                st.json(citas_json, expanded=True)

                # Mostrando el botón para descargar en la interfaz
                st.download_button(
                    label="Descargar JSON",
                    file_name="Citas.json",
                    mime="application/json",
                    data=citas_json,
                )

            st.divider()

            if st.button("Volver", type="primary"):
                # Actualiza el estado de la variable dentro del diccionario de session_state a true
                st.session_state["reportin"] = False

                # Recarga el código
                st.rerun()


# Mostrar interfaz de menú general
def mostrar_menu_general():
    if st.session_state["loggedin"]:
        with mainSection:
            # Muestra información general del proyecto
            st.markdown("# Menú general 👋")

            # Comprueba si el botón de cerrar sesión ha sido presionado
            if st.button("Cerrar sesión", type="primary"):

                # Actualiza el estado de la variable dentro del diccionario de session_state a false
                st.session_state["loggedin"] = False

                # Recarga el código
                st.rerun()

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

            st.divider()

            # Comprueba si el botón de menú de reportes ha sido presionado
            if st.button("Menú de reportes", type="primary"):
                # Actualiza el estado de la variable dentro del diccionario de session_state a true
                st.session_state["reportin"] = True

                # Recarga el código
                st.rerun()

            # Comprueba si el botón de menú de citas ha sido presionado
            if st.button("Menú de citas", type="primary"):
                pass

            st.divider()

            st.markdown("!Anímate a usarlos¡")
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
            st.markdown("# Bienvenido al módulo de gestión de citas 👨‍⚕️")
            st.markdown("## Por favor ingresa tus datos de inicio de sesión")
            st.divider()
            st.markdown('''
            ##### Credenciales para ingresar al sistema  
            > ID: 1  
            > Contraseña: 12345
            ''')
            st.divider()

            # Crear campos para solicitar datos para almacenarlos en las claves user y password respectivamente
            # del diccionario session_state
            st.session_state.id = st.text_input("Inserte el ID del profesional de salud")
            st.session_state.password = st.text_input("Inserte su contraseña", type="password")

            # Verifica que el botón de Iniciar sesión haya sido presionado
            if st.button("Iniciar sesión"):

                # Verifica que las credenciales insertadas existan en la base de datos
                if Usuario.verificar_inicio_sesion(st.session_state.password, st.session_state.id):

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
    mainSection = st.container()
    loginSection = st.container()
    reportSection = st.container()

    # Manejo de transición en inicio de sesión
    with loginSection:
        if "loggedin" not in st.session_state:
            st.session_state["reportin"] = False
            st.session_state["loggedin"] = False
            mostrar_inicio_sesion()
        else:
            if st.session_state["loggedin"] and not st.session_state["reportin"]:
                mostrar_menu_general()
                mostrar_salida_sesion()
            elif st.session_state["loggedin"] and st.session_state["reportin"]:
                mostrar_reporte()
            else:
                mostrar_inicio_sesion()
