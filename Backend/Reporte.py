# Importando las librerías y módulos requeridos
import json
from datetime import datetime
from Persistencia import AdministradorDB
from .ProfesionalSalud import ProfesionalSalud
from .Paciente import Paciente
from .Instalacion import Instalacion
from .Cita import Cita


class Reporte:
    """Este clase contiene el comportamiento necesario para administrar Reportes"""

    # Métodos de clase

    # Generar json con los datos de todos los profesionales de salud
    @staticmethod
    def generar_reporte_profesionales_salud():
        # Crear conexión con base de datos
        instancia_db_reportes = AdministradorDB()

        # Obtener ids de profesionales de salud
        profsalud = instancia_db_reportes.consultar_profesionales_salud()

        # Recorrer los ids obtenidos para crear unas instancias de profesional de salud que serán añadidas a una lista
        list_profsalud = list()
        for reg in profsalud:
            id_profsalud = reg[0]

            profsalud_instancia = ProfesionalSalud(id_profsalud)

            list_profsalud.append(profsalud_instancia.__dict__)

        # Formateando el json para su impresión final
        json_data = {
            "ProfesionalSalud": list_profsalud,
        }

        # Cerrar conexión con base de datos
        instancia_db_reportes.cerrar_conexion_db()

        # Generar json
        json_profsalud = json.dumps(json_data, indent=2)

        # Retornar json
        return json_profsalud

    # Generar json con los datos de todos los pacientes
    @staticmethod
    def generar_reporte_pacientes():
        # Crear conexión con base de datos
        instancia_db_reportes = AdministradorDB()

        # Obtener ids de profesionales de salud
        pacientes = instancia_db_reportes.consultar_pacientes()

        # Recorrer los ids obtenidos para crear unas instancias de profesional de salud que serán añadidas a una lista
        list_pacientes = list()
        for reg in pacientes:
            id_pacientes = reg[0]

            paciente_instancia = Paciente(id_pacientes)

            list_pacientes.append(paciente_instancia.__dict__)

        # Formateando el json para su impresión final
        json_data = {
            "Paciente": list_pacientes,
        }

        # Cerrar conexión con base de datos
        instancia_db_reportes.cerrar_conexion_db()

        # Generar json
        json_paciente = json.dumps(json_data, indent=2)

        # Retornar json
        return json_paciente

    # Generar json con los datos de todas las instalaciones
    @staticmethod
    def generar_reporte_instalaciones():
        # Crear conexión con base de datos
        instancia_db_reportes = AdministradorDB()

        # Obtener ids de profesionales de salud
        instalaciones = instancia_db_reportes.consultar_instalaciones()

        # Recorrer los ids obtenidos para crear unas instancias de profesional de salud que serán añadidas a una lista
        list_instalaciones = list()
        for reg in instalaciones:
            id_instalacion = reg[0]

            paciente_instancia = Instalacion(id_instalacion)

            list_instalaciones.append(paciente_instancia.__dict__)

        # Formateando el json para su impresión final
        json_data = {
            "Instalacion": list_instalaciones,
        }

        # Cerrar conexión con base de datos
        instancia_db_reportes.cerrar_conexion_db()

        # Generar json
        json_instalacion = json.dumps(json_data, indent=2)

        # Retornar json
        return json_instalacion

    # Generar json con los datos de todas las citas
    @staticmethod
    def generar_reporte_citas():
        # Crear conexión con base de datos
        instancia_db_reportes = AdministradorDB()

        # Obtener ids de profesionales de salud
        citas = instancia_db_reportes.consultar_citas()

        # Recorrer los ids obtenidos para crear unas instancias de profesional de salud que serán añadidas a una lista
        list_citas = list()
        for reg in citas:
            id_cita = reg[0]
            id_paciente_asociado = reg[1]
            id_instalacion_asociada = reg[2]
            id_profesionalSalud_asociado = reg[3]
            tipo = reg[4]
            estado = reg[5]
            fecha_inicio = datetime.fromtimestamp(reg[6]).strftime("%Y-%m-%d %H:%M")
            fecha_finalizacion = datetime.fromtimestamp(reg[7]).strftime("%Y-%m-%d %H:%M")

            cita_instancia = Cita(id_cita, id_paciente_asociado, id_instalacion_asociada, id_profesionalSalud_asociado,
                                  tipo, estado, fecha_inicio, fecha_finalizacion)

            list_citas.append(cita_instancia.__dict__)

        # Formateando el json para su impresión final
        json_data = {
            "Cita": list_citas,
        }

        # Cerrar conexión con base de datos
        instancia_db_reportes.cerrar_conexion_db()

        # Generar json
        json_cita = json.dumps(json_data, indent=2)

        # Retornar json
        return json_cita


if __name__ == "__main__":
    print(Reporte.generar_reporte_profesionales_salud())
