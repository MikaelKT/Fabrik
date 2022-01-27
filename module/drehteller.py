from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi

def bewege_drehteller_zum_polierer():
    revpi.io.O_1.value = 1
    while ist_drehteller_bei_polierer() == False:
        pass
    revpi.io.O_1.value = 0

def ist_drehteller_bei_start():
    return True if revpi.io.I_10.value == 1 and revpi.io.I_7.value == 0 and revpi.io.I_9.value == 0 else False

def ist_drehteller_bei_fließband():
    return True if revpi.io.I_9.value == 1 and revpi.io.I_7.value == 0 else False

def bewege_drehteller_zum_polierer():
    revpi.io.O_1.value = 1
    while ist_drehteller_bei_polierer() == False:
        pass
    revpi.io.O_1.value = 0

def bewege_drehteller_zum_fließband():
    revpi.io.O_1.value = 1
    while ist_drehteller_bei_fließband() == False:
        pass
    revpi.io.O_1.value = 0

def bewege_drehteller(richtung):
    if richtung == Richtung.RECHTS and ist_drehteller_bei_fließband() == False:
        if richtung == Richtung.RECHTS and ist_drehteller_bei_start() == True:
            bewege_drehteller_zum_polierer()
        elif richtung == Richtung.RECHTS and ist_drehteller_bei_polierer() == True:
            bewege_drehteller_zum_fließband()
    elif richtung == Richtung.LINKS and ist_drehteller_bei_start() == False:
        bewege_drehteller_zum_kran()

def pusher(value):
    revpi.io.O_14.value = value

def bewege_drehteller_zum_kran():
    revpi.io.O_2.value = 1
    while ist_drehteller_bei_start() == False:
        pass
    revpi.io.O_2.value = 0

def ist_drehteller_bei_polierer():
    return True if revpi.io.I_7.value == 1 and revpi.io.I_9.value == 0 else False
