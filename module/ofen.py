from eigenschaften.Richtung import Richtung
from eigenschaften.Revpi import revpi
import time

def ist_ofen_drinn():
    return True if revpi.io.I_5.value == 1 and revpi.io.I_4.value == 0 else False

def ist_ofen_draußen():
    return True if revpi.io.I_4.value == 1 and revpi.io.I_5.value == 0 else False

def bewege_ofen(richtung):
    if richtung == Richtung.REIN and ist_ofen_drinn() == False:
        revpi.io.O_5.value = 1
        while ist_ofen_drinn() == False:
            pass
        revpi.io.O_5.value = 0
    elif richtung == Richtung.RAUS and ist_ofen_draußen() == False:
        revpi.io.O_6.value = 1
        while ist_ofen_draußen() == False:
            pass
        revpi.io.O_6.value = 0

def tür_öffnen(value):
    revpi.io.O_13.value = value

def warte_auf_block_gesetzt():
    while revpi.io.I_2.value == 1:
        pass

def block_brennen():
    revpi.io.O_13.value = 0

    revpi.io.O_9.value = 1
    time.sleep(4)
    revpi.io.O_9.value = 0

    revpi.io.O_13.value = 1