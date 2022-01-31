from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi
from eigenschaften.Strom import Strom

def kran_links(strom):
    revpi.io.O_7.value = strom.value

def kran_rechts(strom):
    revpi.io.O_8.value = strom.value

def saugnapf(strom):
    revpi.io.O_11.value = strom.value

def saugnapf_halterung(strom):
    revpi.io.O_12.value = strom.value

def ist_kran_links():
    return True if revpi.io.I_3.value == 1 and revpi.io.I_6.value == 0 else False

def ist_kran_rechts():
    return True if revpi.io.I_6.value == 1 and revpi.io.I_3.value == 0 else False

def bewege_kran(richtung):
    if richtung == Richtung.RECHTS and ist_kran_rechts() == False:
        kran_rechts(Strom.AN)
        while ist_kran_rechts() == False:
            pass
        kran_rechts(Strom.AUS)
    elif richtung == Richtung.LINKS and ist_kran_links() == False:
        kran_links(Strom.AN)
        while ist_kran_links() == False:
            pass
        kran_links(Strom.AUS)

