import threading
import revpimodio2
import time

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

def kompressor_geht_an(value):
    revpi.io.O_10.value = value


def warte_auf_block_gesetzt():
    while revpi.io.I_2.value == 1:
        pass

def tür_öffnen(value):
    revpi.io.O_13.value = value

def ofen_rein_fahren():
    revpi.io.O_5.value = 1
    while revpi.io.I_5.value == 0:
        pass
    revpi.io.O_5.value = 0

def ofen_raus_fahren():
    revpi.io.O_6.value = 1
    while revpi.io.I_4.value == 0:
        pass
    revpi.io.O_6.value = 0

def kran_links():
    revpi.io.O_7.value = 1
    while revpi.io.I_3.value == 0:
        pass
    revpi.io.O_7.value = 0

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

def kran_rechts():
    revpi.io.O_8.value = 1
    while revpi.io.I_6.value == 0:
        pass
    revpi.io.O_8.value = 0

def drehteller_zur_säge_drehen():
    revpi.io.O_1.value = 1
    while revpi.io.I_7.value == 0:
        pass
    revpi.io.O_1.value = 0

def polier_säge(value):
    revpi.io.O_4.value = value

def drehteller_zum_fließband_drehen():
    revpi.io.O_1.value = 1
    while revpi.io.I_9.value == 0:
        pass
    revpi.io.O_1.value = 0

def pusher(value):
    revpi.io.O_14.value = value

def drehteller_zum_start_drehen():
    revpi.io.O_2.value = 1
    while revpi.io.I_10.value == 0:
        pass
    revpi.io.O_2.value = 0

def fließband_an_solange_kein_block_ist():
    revpi.io.O_3.value = 1
    while revpi.io.I_8.value == 1:
        pass
    revpi.io.O_3.value = 0




revpi.handlesignalend(turn_all_off)
revpi.mainloop(blocking=False)

while True:
    kompressor_geht_an(1)

    revpi.io.O_2.value = 1
    while revpi.io.I_10.value == 0:
        pass
    revpi.io.O_2.value = 0

    kompressor_geht_an(0)