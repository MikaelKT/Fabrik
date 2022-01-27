from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi

def ist_kran_links():
    return True if revpi.io.I_3.value == 1 and revpi.io.I_6.value == 0 else False

def ist_kran_rechts():
    return True if revpi.io.I_6.value == 1 and revpi.io.I_3.value == 0 else False

def bewege_kran(richtung):
    if richtung == Richtung.RECHTS and ist_kran_rechts() == False:
        revpi.io.O_8.value = 1
        while ist_kran_rechts() == False:
            pass
        revpi.io.O_8.value = 0
    elif richtung == Richtung.LINKS and ist_kran_links() == False:
        revpi.io.O_7.value = 1
        while ist_kran_links() == False:
            pass
        revpi.io.O_7.value = 0
        


def saugnapf_an(value):
    revpi.io.O_11.value = value

def saugnapf_halter_runterfahren():
    revpi.io.O_12.value = 1

def saugnapf_halter_hochfahren():
    revpi.io.O_12.value = 0

