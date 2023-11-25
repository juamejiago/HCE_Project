# Importando la librería de ORM para python
import sqlite3 as sq

# Consultar de base de datos
"""con = sq.connect("HCE_DB.db")
cursor = con.cursor()
rows = cursor.execute("SELECT * FROM Cita").fetchall()
print(rows)
con.close()"""

# Guardar de base de datos
"""con = sq.connect("HCE_DB.db")
cursor = con.cursor()
cursor.execute("INSERT INTO ProfesionalSalud VALUES (3)")
con.commit()
con.close()"""


class AdministradorDB:
    """Este clase contiene el comportamiento necesario para manejar consultas de Base de Datos"""

    # Atributos de clase
    db_name = "HCE_DB.db"

    # Constructor
    def __init__(self):
        self.con = sq.connect(AdministradorDB.db_name)
        self.cursor = self.con.cursor()

    # Métodos de instancia
    def consultar_profesionales_salud(self):
        rows = self.cursor.execute("SELECT * FROM ProfesionalSalud").fetchall()
        return rows

    def consultar_pacientes(self):
        rows = self.cursor.execute("SELECT * FROM Paciente").fetchall()
        return rows

    def consultar_instalacion(self):
        rows = self.cursor.execute("SELECT * FROM Instalacion").fetchall()
        return rows

    def consultar_estado_cita(self, id_cita):
        rows = self.cursor.execute("SELECT * FROM Cita").fetchall()
        return rows[id_cita]

    def crear_profesional_salud(self):
        self.cursor.execute("INSERT INTO ProfesionalSalud DEFAULT VALUES")
        self.con.commit()

    def crear_paciente(self):
        self.cursor.execute("INSERT INTO Paciente DEFAULT VALUES")
        self.con.commit()

    def crear_instalacion(self):
        self.cursor.execute("INSERT INTO Instalacion DEFAULT VALUES")
        self.con.commit()

    def consultar_horario_cita_por_profsalud(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE \ProfesionalSaludAsociado = ?',
                                   (id_for,)).fetchall()
        return rows

    def consultar_horario_cita_por_paciente(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE PacienteAsociado = ?',
                                   (id_for,)).fetchall()
        return rows

    def consultar_horario_cita_por_instalacion(self, id_for):
        rows = self.cursor.execute('SELECT FechaInicio, FechaFinalizacion FROM Cita WHERE InstalacionAsociada = ?',
                                   (id_for,)).fetchall()
        return rows

    def cancelar_cita(self, id_cita):
        self.cursor.execute('UPDATE Cita SET Estado = ? WHERE ID = ?', (1, id_cita))
        self.con.commit()

    def cerrar_conexion_db(self):
        self.con.close()