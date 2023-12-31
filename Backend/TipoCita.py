# Importando el módulo requerido
from enum import Enum


class TipoCita(Enum):
    CONSULTA_MEDICA = 1
    EXAMEN_FISICO = 2
    SESION_PSICOLOGICA = 3
    REVISION_DENTAL = 4
    CONTROL_NUTRICIONAL = 5
    VACUNACION = 6
    ANALISIS_DE_SANGRE = 7
    FISIOTERAPIA = 8
    CONSULTA_OCULAR = 9
    TRATAMIENTO_ORTODONTICO = 10
    TERAPIA_OCUPACIONAL = 11
    CIRUGIA = 12
    SEGUIMIENTO_EMBARAZO = 13
    CONSULTA_PEDIATRICA = 14
    TERAPIA_DE_PAREJA = 15
