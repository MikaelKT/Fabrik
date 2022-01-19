import threading
from xml.sax.xmlreader import InputSource
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

def kompressor_geht_an():
    revpi.io.O_10.value = 1

def kompressor_geht_aus():
    revpi.io.O_10.value = 0


def warte_auf_block_gesetzt():
    while revpi.io.I_2.value == 1:
        pass

def tür_öffnen():
    revpi.io.O_13.value = 1

def tür_schließen():
    revpi.io.O_13.value = 0

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

def saugnapf_an():
    revpi.io.O_11.value = 1

def saugnapf_aus():
    revpi.io.O_11.value = 0

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

def polier_säge():
    revpi.io.O_4.value = 1

def polier_säge_aus():
    revpi.io.O_4.value = 0

def drehteller_zum_fließband_drehen():
    revpi.io.O_1.value = 1
    while revpi.io.I_9.value == 0:
        pass
    revpi.io.O_1.value = 0

def pusher():
    revpi.io.O_14.value = 1

def pusher_aus():
    revpi.io.O_14.value = 0

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
    
    warte_auf_block_gesetzt()

    kompressor_geht_an()
    
    tür_öffnen()

    ofen_rein_fahren()

    block_brennen()

    ofen_raus_fahren()

    tür_schließen()

    kran_links()

    saugnapf_halter_runterfahren()

    time.sleep(1)

    saugnapf_an()
    
    time.sleep(1)

    saugnapf_halter_hochfahren()

    kran_rechts()

    saugnapf_halter_runterfahren()
    
    time.sleep(1)

    saugnapf_aus()

    time.sleep(1)
    
    saugnapf_halter_hochfahren()

    time.sleep(1)
    
    drehteller_zur_säge_drehen()

    polier_säge()
    
    time.sleep(4)
    
    polier_säge_aus()

    drehteller_zum_fließband_drehen()

    pusher()

    time.sleep(0.5)
    
    pusher_aus()

    kompressor_geht_aus()
    
    threading.Thread(target=drehteller_zum_start_drehen).start()

    threading.Thread(target=fließband_an_solange_kein_block_ist).start()