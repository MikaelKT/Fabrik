from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi
from eigenschaften.Strom import Strom

def fließband(strom):
    revpi.io.O_3.value = strom.value

def ist_fließband_sensor_durchbrochen():
    return True if revpi.io.I_8.value == 0 else False

def fließband_an(richtung):
    if richtung == Richtung.RAUS and ist_fließband_sensor_durchbrochen() == False:
        fließband(Strom.AN)
        while ist_fließband_sensor_durchbrochen() == False:
            pass
        fließband(Strom.AUS)