# Importando la librería de ORM Python para gestionar sqlite3
import sqlite3 as sq


class AdministradorDB:
    """Este clase contiene el comportamiento necesario para manejar consultas de Base de Datos"""

    # Atributos de clase

    # Atributo con el nombre de la base de datos para realizar la conexión
    db_name = ""

    # Constructor
    def __init__(self):
        self.con = sq.connect(AdministradorDB.db_name)
        self.cursor = self.con.cursor()

    # Métodos de instancia

    # Método para consultar todos los profesionales de salud
    def consultar_profesionales_salud(self):
        rows = self.cursor.execute("SELECT * FROM ProfesionalSalud").fetchall()
        return rows

    # Método para consultar todos los pacientes
    def consultar_pacientes(self):
        rows = self.cursor.execute("SELECT * FROM Paciente").fetchall()
        return rows

    # Método para consultar todas las instalaciones
    def consultar_instalacion(self):
        rows = self.cursor.execute("SELECT * FROM Instalacion").fetchall()
        return rows

    # Método para consultar el estado de una cita
    def consultar_estado_cita(self, id_cita):
        rows = self.cursor.execute("SELECT * FROM Cita").fetchall()
        return rows[id_cita]

    def crear_profesional_salud(self):
        self.cursor.execute("INSERT INTO ProfesionalSalud DEFAULT VALUES")
        self.con.commit()

    # Método para crear un nuevo paciente
    def crear_paciente(self):
        self.cursor.execute("INSERT INTO Paciente DEFAULT VALUES")
        self.con.commit()

    # Método para crear una nueva instalación
    def crear_instalacion(self):
        self.cursor.execute("INSERT INTO Instalacion DEFAULT VALUES")
        self.con.commit()

    # Método para consultar los horarios de cita que tiene agendado un profesional de salud
    def consultar_horario_cita_por_profsalud(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE \ProfesionalSaludAsociado = ?',
                                   (id_for,)).fetchall()
        return rows

    # Método para consultar los horarios de cita que tiene agendado un paciente
    def consultar_horario_cita_por_paciente(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE PacienteAsociado = ?',
                                   (id_for,)).fetchall()
        return rows

    # Método para consultar los horarios de cita que tiene agendado una instalación
    def consultar_horario_cita_por_instalacion(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE InstalacionAsociada = ?',
                                   (id_for,)).fetchall()
        return rows

    # Método para cancelar una cita
    def cancelar_cita(self, id_cita):
        self.cursor.execute('UPDATE Cita SET Estado = ? WHERE ID = ?', (1, id_cita))
        self.con.commit()

    # Método para cerrar la conexión con la base de datos
    def cerrar_conexion_db(self):
        self.con.close()


# Definiendo el nombre del Path hacia la base de datos en función de donde estemos ejecutando el código
if __name__ == '__main__':
    AdministradorDB.db_name = "HCE_DB.db"
else:
    AdministradorDB.db_name = "Persistencia/HCE_DB.db"
