from enum import Enum
from threading import Thread
import revpimodio2
import time
import modules.ofen

class Richtung(Enum):
    LINKS = 1
    RECHTS = 2
    REIN = LINKS
    RAUS = RECHTS

class Strom(Enum):
    AN = 1
    AUS = 0

revpi = revpimodio2.RevPiModIO(autorefresh = True)

def turn_all_off():
    revpi.io.O_1.value = 0
    revpi.io.O_2.value = 0
    revpi.io.O_3.value = 0
    revpi.io.O_4.value = 0
    revpi.io.O_5.value = 0
    revpi.io.O_6.value = 0
    revpi.io.O_7.value = 0
    revpi.io.O_8.value = 0
    revpi.io.O_9.value = 0
    revpi.io.O_10.value = 0
    revpi.io.O_11.value = 0
    revpi.io.O_12.value = 0
    revpi.io.O_13.value = 0
    revpi.io.O_14.value = 0


def ist_kran_links():
    return True if revpi.io.I_3.value == 1 and revpi.io.I_6.value == 0 else False

def ist_kran_rechts():
    return True if revpi.io.I_6.value == 1 and revpi.io.I_3.value == 0 else False

def ist_fließband_sensor_durchbrochen():
    return True if revpi.io.I_8.value == 0 else False

def ist_kompressor_an():
    return True if revpi.io.O_10.value == 1 else False

def ist_drehteller_bei_polierer():
    return True if revpi.io.I_7.value == 1 and revpi.io.I_9.value == 0 else False

def ist_drehteller_bei_fließband():
    return True if revpi.io.I_9.value == 1 and revpi.io.I_7.value == 0 else False

def ist_drehteller_bei_start():
    return True if revpi.io.I_10.value == 1 and revpi.io.I_7.value == 0 and revpi.io.I_9.value == 0 else False

def schalte_kompressor(strom):
    if strom == Strom.AN and ist_kompressor_an() == False:
        revpi.io.O_10.value = 1
    elif strom == Strom.AUS and ist_kompressor_an() == True:
        revpi.io.O_10.value = 0


def warte_auf_block_gesetzt():
    while revpi.io.I_2.value == 1:
        pass

def tür_öffnen(value):
    revpi.io.O_13.value = value
    
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

def bewege_ofen(richtung):
    if richtung == Richtung.REIN and modules.ofen.ist_ofen_drinn() == False:
        revpi.io.O_5.value = 1
        while modules.ofen.ist_ofen_drinn() == False:
            pass
        revpi.io.O_5.value = 0
    elif richtung == Richtung.RAUS and modules.ofen.ist_ofen_draußen() == False:
        revpi.io.O_6.value = 1
        while modules.ofen.ist_ofen_draußen() == False:
            pass
        revpi.io.O_6.value = 0

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

def bewege_drehteller_zum_kran():
    revpi.io.O_2.value = 1
    while ist_drehteller_bei_start() == False:
        pass
    revpi.io.O_2.value = 0
    
def bewege_drehteller(richtung):
    if richtung == Richtung.RECHTS and ist_drehteller_bei_fließband() == False:
        if richtung == Richtung.RECHTS and ist_drehteller_bei_start() == True:
            bewege_drehteller_zum_polierer()
        elif richtung == Richtung.RECHTS and ist_drehteller_bei_polierer() == True:
            bewege_drehteller_zum_fließband()
    elif richtung == Richtung.LINKS and ist_drehteller_bei_start() == False:
        bewege_drehteller_zum_kran()

def fließband_an(richtung):
    if richtung == Richtung.RAUS and ist_fließband_sensor_durchbrochen() == False:
        revpi.io.O_3.value = 1
        while ist_fließband_sensor_durchbrochen() == False:
            pass
        revpi.io.O_3.value = 0

def polierer(value):
    revpi.io.O_4.value = value

def pusher(value):
    revpi.io.O_14.value = value

def saugnapf_halter_runterfahren():
    revpi.io.O_12.value = 1

def saugnapf_halter_hochfahren():
    revpi.io.O_12.value = 0

def saugnapf_an(value):
    revpi.io.O_11.value = value

def block_brennen():
    revpi.io.O_13.value = 0

    revpi.io.O_9.value = 1
    time.sleep(4)
    revpi.io.O_9.value = 0

    revpi.io.O_13.value = 1

def reset_all():
    schalte_kompressor(Strom.AN)
    if modules.ofen.ist_ofen_draußen() == False:
        revpi.io.O_13.value = 1
        bewege_ofen(Richtung.RAUS)
        revpi.io.O_13.value = 0
    bewege_kran(Richtung.RECHTS)
    if ist_drehteller_bei_start() == False:
        bewege_drehteller_zum_kran()
    if modules.ofen.ist_ofen_draußen() == True and ist_drehteller_bei_start() == True and ist_kran_rechts() == True and ist_kompressor_an() == True:
        return True


revpi.handlesignalend(turn_all_off)
revpi.mainloop(blocking=False)



while True:
    
    if reset_all() == True:
        
        schalte_kompressor(Strom.AN)

        warte_auf_block_gesetzt()
        
        tür_öffnen(1)
        
        bewege_ofen(Richtung.REIN)

        block_brennen()

        bewege_ofen(Richtung.RAUS)

        tür_öffnen(0)

        bewege_kran(Richtung.LINKS)

        saugnapf_halter_runterfahren()

        time.sleep(1)

        saugnapf_an(1)
        
        time.sleep(1)

        saugnapf_halter_hochfahren()

        bewege_kran(Richtung.RECHTS)

        saugnapf_halter_runterfahren()
        
        time.sleep(1)

        saugnapf_an(0)

        time.sleep(1)
        
        saugnapf_halter_hochfahren()

        time.sleep(1)
        
        bewege_drehteller(Richtung.RECHTS)

        polierer(1)
        
        time.sleep(4)
        
        polierer(0)

        bewege_drehteller(Richtung.RECHTS)

        pusher(1)

        time.sleep(0.5)
        
        pusher(0)

        schalte_kompressor(Strom.AUS)
        
        th = Thread(target=bewege_drehteller(Richtung.LINKS))
        th.start()
        th1=Thread(target=fließband_an(Richtung.RAUS))
        th1.start()