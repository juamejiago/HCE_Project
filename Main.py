import streamlit as st
from .Persistencia.GestorPersistencia import AdministradorDB

# Se plantea una rutina de inicialización que cargue los objetos de la base de datos
def inicializacion():
    AdministradorDB.consultar_inventario_recursos()


def main():
    pass

def inicio_sesion():
    # En esta función se despliega gráficamente el inicio, se leen las credenciales, se comprueba en la base de datos y retorna un token de logueo que usará el profesional.
    st.title("Modulo Gestion de Citas")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type='password')

    if st.button("Iniciar sesión"):
        if username == "usuario" and password == "contraseña":
            st.success("Inicio de sesión exitoso")
            # Aquí colocarías el código para redirigir a la página principal o realizar alguna acción posterior al inicio de sesión
        else:
            st.error("Credenciales incorrectas")
def crearCita():
    # En esta función se despliega gráficamente la interfaz de creación de cita, conectandose con los objetos necesario como Cita, Profesional, Instalación, Paciente y Base de datos.
    pass
def infoCita():
    pass
def modificarCita():
    pass
def cancelarCita():
    pass
def infoEstado():
    pass
if __name__ == '__main__':
    main()
