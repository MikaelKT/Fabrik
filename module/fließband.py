from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi

def ist_fließband_sensor_durchbrochen():
    return True if revpi.io.I_8.value == 0 else False

def fließband_an(richtung):
    if richtung == Richtung.RAUS and ist_fließband_sensor_durchbrochen() == False:
        revpi.io.O_3.value = 1
        while ist_fließband_sensor_durchbrochen() == False:
            pass
        revpi.io.O_3.value = 0