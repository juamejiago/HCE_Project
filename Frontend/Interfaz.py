"""Este módulo gestiona toda la lógica requerida para llevar a cabo la administración del Frontend"""

# Importando las librerías y módulos requeridos
import streamlit as st
from datetime import datetime
from Backend import Usuario, Reporte, TipoCita, EstadoCita, Instalacion, Paciente, ProfesionalSalud
from Persistencia import AdministradorDB


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
                st.session_state["menucitain"] = True

                # Recarga el código
                st.rerun()

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
        if "loggedin" not in st.session_state:
            st.session_state["loggedin"] = False
        if st.session_state["loggedin"] == False:

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


# Mostrar menú general de citas
def menu_cita():
    with menucitaSection:
        st.markdown("# Administración de citas 📅")
        st.markdown("> Anímate a utilizar nuestro sistema para gestionar tus citas :sunglasses:")

        # Botones en la página de menú de citas
        if st.button("Agendar"):
            st.session_state["asignarin"] = True
            st.session_state["monitoreoin"] = False
            st.session_state["modificarin"] = False
            st.rerun()
        if st.button("Modificar"):
            st.session_state["modificarin"] = True
            st.session_state["monitoreoin"] = False
            st.session_state["asignarin"] = False
            st.rerun()

        if st.button("Monitorear"):
            st.session_state["asignarin"] = False
            st.session_state["monitoreoin"] = True
            st.session_state["modificarin"] = False
            st.rerun()

        st.divider()

        if st.button("Volver al Menú General", type="primary"):
            # Actualiza el estado de la variable dentro del diccionario de session_state a false
            st.session_state["menucitain"] = False
            st.session_state["monitoreoin"] = False
            st.session_state["asignarin"] = False
            st.session_state["modificarin"] = False

            # Recarga el código
            st.rerun()


# Mostrar interfaz de asignación de citas
def asignar_cita():
    with asignarSection:
        if st.session_state["asignarin"]:
            opciones_tipo_cita = [tipo.name.replace('_', ' ').title() for tipo in TipoCita]
            admin = AdministradorDB()

            pacientes = [tupla[0] for tupla in admin.consultar_pacientes()]
            profesionales = [tupla[0] for tupla in admin.consultar_profesionales_salud()]
            instalaciones = [tupla[0] for tupla in admin.consultar_instalaciones()]
            st.subheader('Agregar Nueva Cita')

            # Obtener información de la cita
            fecha = st.date_input('Fecha de la Cita')
            hora_inicio = st.time_input('Hora de Inicio')
            hora_fin = st.time_input('Hora de Finalización')

            # Desplegables para seleccionar paciente, profesional e instalación
            paciente = st.selectbox('Seleccione Paciente', pacientes)
            profesional = st.selectbox('Seleccione Profesional', profesionales)
            instalacion = st.selectbox('Seleccione Instalación', instalaciones)

            tipo = st.selectbox('Tipo de Cita', opciones_tipo_cita)

            # Botón para agregar la cita
            if st.button('Agregar Cita', type="primary"):

                Pdispo = Paciente.disponibilidad_paciente(paciente, fecha, hora_inicio, hora_fin)
                PSdispo = ProfesionalSalud.disponibilidad_profesional(profesional, fecha, hora_inicio, hora_fin)
                Idispo = Instalacion.disponibilidad_instalacion(instalacion, fecha, hora_inicio, hora_fin)

                if PSdispo and Pdispo and Idispo:
                    fecha = fecha.strftime("%Y-%m-%d")
                    hora_inicio = hora_inicio.strftime("%H:%M")
                    hora_fin = hora_fin.strftime("%H:%M")
                    fechaInicio = fecha + " " + hora_inicio
                    fechaFin = fecha + " " + hora_fin

                    tipo = next((t.value for t in TipoCita if t.name.replace('_', ' ').title() == tipo), None)
                    admin.crear_cita(paciente, instalacion, profesional, tipo, fechaInicio, fechaFin)
                    admin.cerrar_conexion_db()

                    st.success('Cita agregada exitosamente.')
                if PSdispo == False:
                    st.error("El profesional no tiene esa fecha disponible")
                if Pdispo == False:
                    st.error("El paciente no tiene esa fecha disponible")
                if Idispo == False:
                    st.error("La instalacion no tiene esa fecha disponible")


# Mostrar interfaz de monitoreo de citas
def monitorear_cita():
    with monitoreoSection:
        st.title("Buscador de Citas")

        search_query = st.text_input("Ingrese el id de la cita:")
        if search_query:
            if st.button("Buscar"):
                st.write("Resultados de la búsqueda:")

                admin = AdministradorDB()
                cita = admin.consultar_cita(search_query)
                if len(cita) == 0:
                    st.error(f"No existe una cita relacionada con el ID {search_query}")
                else:

                    cita = cita[0]
                    if cita:
                        estado = EstadoCita(cita[5]).name
                        fecha1 = cita[6]
                        fecha2 = cita[7]
                        tipo = TipoCita(cita[4]).name
                        st.write(
                            f"La cita con código de identificación C{cita[0]} se encuentra en estado actual {estado}"
                            f" y se programo con fecha de inicio  {fecha1} y fecha de finalización {fecha2} para el"
                            f" paciente con ID {cita[1]}. El tipo de esta cita corresponde a una {tipo} y tiene asignada"
                            f" la instalación con ID {cita[2]} con el profesional de salud con ID {cita[3]}.")
                        st.write("Estados")
                        admin = AdministradorDB()
                        estados = admin.consultar_estados(cita[0])
                        admin.cerrar_conexion_db()

                        for estado in estados:
                            tipo = EstadoCita(estado[2]).name
                            fecha = estado[4]
                            st.write(f"{tipo} {fecha} autor: {estado[5]}")
        else:
            st.error("Ingresar Id de la cita.")


# Mostrar interfaz de modificación de citas
def modificar_cita():
    with modificacionSection:
        instancia = AdministradorDB()
        st.title("Modificar Cita")
        search_query = st.text_input("Ingrese el id de la cita:")
        if search_query:
            cita = instancia.consultar_cita(search_query)
            if len(cita) == 0:
                st.error(f"No existe una cita relacionada con el ID {search_query}")
            else:
                if cita:
                    cita = cita[0]

                    id_cita, profesional = cita[0], cita[3]

                    pacientes = [tupla[0] for tupla in instancia.consultar_pacientes()]
                    profesionales = [tupla[0] for tupla in instancia.consultar_profesionales_salud()]
                    instalaciones = [tupla[0] for tupla in instancia.consultar_instalaciones()]
                    opciones_tipo_cita = [tipo.name.replace('_', ' ').title() for tipo in TipoCita]
                    estados = [e.name.replace('_', ' ').title() for e in EstadoCita if e.name != 'MODIFICADA']

                    # Desplegables para seleccionar paciente, profesional e instalación
                    paciente = st.selectbox('Seleccione Paciente', pacientes)
                    instalacion = st.selectbox('Seleccione Instalación', instalaciones)
                    tipo = st.selectbox('Tipo de Cita', opciones_tipo_cita)
                    estado = st.selectbox('Seleccione el estado a modificar de la cita', estados)

                    # Obtener información de la cita
                    fecha = st.date_input('Fecha de la Cita')
                    hora_inicio = st.time_input('Hora de Inicio')
                    hora_fin = st.time_input('Hora de Finalización')

                    # Botón para agregar la cita
                    if st.button('Confirmar modificación de cita.', type="primary"):

                        Pdispo = Paciente.disponibilidad_paciente(paciente, fecha, hora_inicio, hora_fin)
                        Idispo = Instalacion.disponibilidad_instalacion(instalacion, fecha, hora_inicio, hora_fin)

                        if Pdispo and Idispo:
                            fecha = fecha.strftime("%Y-%m-%d")
                            hora_inicio = hora_inicio.strftime("%H:%M")
                            hora_fin = hora_fin.strftime("%H:%M")
                            fechaInicio = fecha + " " + hora_inicio
                            fechaFin = fecha + " " + hora_fin

                            now = datetime.now()
                            t_modificacion = now.strftime("%Y-%m-%d %H:%M")
                            tipo = next((t.value for t in TipoCita if t.name.replace('_', ' ').title() == tipo), None)
                            estado = next((e.value for e in EstadoCita if e.name.replace('_', ' ').title() == estado),
                                          None)
                            print(id_cita, paciente, instalacion, profesional, tipo, estado,
                                  fechaInicio, fechaFin, t_modificacion)
                            instancia.modificacion_general(id_cita, paciente, instalacion, profesional, tipo, estado,
                                                           fechaInicio, fechaFin, t_modificacion)
                            st.success('Cita modificada exitosamente.')

                        if Pdispo == False:
                            st.error("El paciente no tiene esa fecha disponible")
                        if Idispo == False:
                            st.error("La instalacion no tiene esa fecha disponible")

                        instancia.cerrar_conexion_db()

        else:
            st.error("Ingrese el ID de la cita.")


if __name__ == "__main__":
    # Configurando el título de la página
    st.set_page_config(page_title="Módulo de gestión de citas")

    # Creando contenedores para mostrar el contenido de la app
    mainSection = st.container()
    loginSection = st.container()
    reportSection = st.container()
    menucitaSection = st.container()
    asignarSection = st.container()
    monitoreoSection = st.container()
    modificacionSection = st.container()

    # Manejo de transición en inicio de sesión
    with loginSection:
        if "loggedin" not in st.session_state:
            st.session_state["reportin"] = False
            st.session_state["loggedin"] = False
            st.session_state["menucitain"] = False
            st.session_state["asignarin"] = False
            st.session_state["monitoreoin"] = False
            st.session_state["modificarin"] = False
            mostrar_inicio_sesion()
        else:
            if st.session_state["loggedin"] and not st.session_state["reportin"] and not st.session_state[
                "menucitain"] and not st.session_state["asignarin"] and not st.session_state["monitoreoin"]:
                mostrar_menu_general()
            if st.session_state["loggedin"] and st.session_state["reportin"]:
                mostrar_reporte()
            if st.session_state["loggedin"] and st.session_state["menucitain"]:
                menu_cita()
            if st.session_state["loggedin"] and st.session_state["asignarin"] and not st.session_state["monitoreoin"]:
                asignar_cita()
            if st.session_state["loggedin"] and st.session_state["monitoreoin"]:
                monitorear_cita()
            if st.session_state["loggedin"] and st.session_state["modificarin"]:
                modificar_cita()

            else:
                mostrar_inicio_sesion()
