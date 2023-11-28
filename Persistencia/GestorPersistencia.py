# Importando la librería de ORM Python para gestionar sqlite3
import sqlite3 as sq


class AdministradorDB:
    """Este clase contiene el comportamiento necesario para manejar consultas de Base de Datos"""

    # Atributos de clase

    # Atributo con el nombre de la base de datos para realizar la conexión
    db_name = ""

    # Constructor
    def __init__(self):
        self.con = sq.connect("C:\\Users\\DELL\\PycharmProjects\\pythonProject8\\Persistencia\\HCE_DB.db")
        self.cursor = self.con.cursor()

    # Métodos de instancia
    def crear_cita(self, paciente, instalacion, profesional, tipo, fi, ff):
        sql = "INSERT INTO Cita (PacienteAsociado, InstalacionAsociada, ProfesionalSaludAsociado, Tipo, Estado, FechaInicio, FechaFinalizacion) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sql, (paciente, instalacion, profesional, tipo, 7, fi, ff))
        self.con.commit()
        id_cita = self.cursor.lastrowid
        sql = "INSERT INTO Estado (Cita_Asociada, Tipo, Detalle, Fecha, Autor) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sql, (id_cita, 6, "", fi, profesional))
        self.con.commit()
    def consultar_cita(self, id):
        cita = self.cursor.execute("SELECT * FROM Cita WHERE  ID= ?",
                                   (id,)).fetchall()
        return cita
    def consultar_citas(self):
        citas=self.cursor.execute("SELECT * FROM Cita").fetchall()
        return citas
    def consultar_estados(self,id):
        estados=self.cursor.execute("SELECT * FROM Estado WHERE Cita_Asociada=?",(id,)).fetchall()
        return estados
    # Método para consultar todos los profesionales de salud
    def consultar_profesionales_salud(self):
        rows = self.cursor.execute("SELECT * FROM ProfesionalSalud").fetchall()
        return rows

    # Método para consultar todos los pacientes
    def consultar_pacientes(self):
        rows = self.cursor.execute("SELECT * FROM Paciente").fetchall()
        return rows

    # Método para consultar todas las instalaciones
    def consultar_instalaciones(self):
        rows = self.cursor.execute("SELECT * FROM Instalacion").fetchall()
        return rows

        # Método para consultar todas las citas
    def consultar_citas(self):
        rows = self.cursor.execute("SELECT * FROM Cita").fetchall()
        return rows

    # Método para consultar el estado de una cita
    def consultar_estado_cita(self, id_cita):
        rows = self.cursor.execute("SELECT * FROM Cita").fetchall()
        return rows[id_cita][5]

    # Método para consultar por las credenciales de sesión de un usuario
    def consultar_credenciales_sesion(self, password, ID):
        rows = self.cursor.execute("SELECT Contrasena, ID FROM Usuario \
        WHERE (contrasena, ID) = (?, ?)", (password, ID)).fetchall()
        return rows

    # Método para crear un nuevo profesional de salud
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
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE ProfesionalSaludAsociado = ? AND Estado=7',
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

    def modificar_estado(self, id_cita, modific):
        self.cursor.execute('UPDATE Cita SET Estado = ? WHERE ID = ?', (modific, id_cita))
        self.con.commit()

    def modifciar_paciente_cita(self, id_cita, paciente):
        self.cursor.execute('UPDATE Cita SET PacienteAsociado = ? WHERE ID = ?', (paciente, id_cita))
        self.con.commit()

    def modifciar_instalacion_cita(self, id_cita, instalacion):
        self.cursor.execute('UPDATE Cita SET InstalacionAsociada = ? WHERE ID = ?',
                            (instalacion, id_cita))
        self.con.commit()

    def modifciar_tipo_cita(self, id_cita, tipo):
        self.cursor.execute('UPDATE Cita SET Tipo = ? WHERE ID = ?', (tipo, id_cita))
        self.con.commit()

    def modifciar_fecha_cita(self, id_cita, fechaIn, fechaOut):
        self.cursor.execute('UPDATE Cita SET FechaInicio = ?, FechaFinalizacion = ? WHERE ID = ?',
                            (fechaIn, fechaOut, id_cita))
        self.con.commit()

    # Método para cerrar la conexión con la base de datos
    def cerrar_conexion_db(self):
        self.con.close()


# Definiendo el nombre del Path hacia la base de datos en función de donde estemos ejecutando el código
if __name__ == '__main__':
    AdministradorDB.db_name = "HCE_DB.db"
else:
    AdministradorDB.db_name = r"C:\Users\DELL\PycharmProjects\pythonProject8\Persistencia\HCE_DB.db"
