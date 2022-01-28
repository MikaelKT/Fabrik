from eigenschaften.Revpi import revpi
from eigenschaften.Richtung import Richtung
from eigenschaften.Strom import Strom
from threading import Thread
import time
from module.fließband import fließband_an
from module.kompressor import schalte_kompressor, ist_kompressor_an
from module.ofen import bewege_ofen, block_brennen, ist_ofen_draußen, tür_öffnen, warte_auf_block_gesetzt
from module.kran import bewege_kran, ist_kran_rechts, saugnapf_an, saugnapf_halter_hochfahren, saugnapf_halter_runterfahren
from module.drehteller import bewege_drehteller, ist_drehteller_bei_start, bewege_drehteller_zum_kran, pusher
from module.polierer import polierer




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




def reset_all():
    schalte_kompressor(Strom.AN)
    if ist_ofen_draußen() == False:
        revpi.io.O_13.value = 1
        bewege_ofen(Richtung.RAUS)
        revpi.io.O_13.value = 0
    bewege_kran(Richtung.RECHTS)
    if ist_drehteller_bei_start() == False:
        bewege_drehteller_zum_kran()
    if ist_ofen_draußen() == True and ist_drehteller_bei_start() == True and ist_kran_rechts() == True and ist_kompressor_an() == True:
        return True


revpi.handlesignalend(turn_all_off)
revpi.mainloop(blocking=False)



while True:
    
    if reset_all() == True:
        

        schalte_kompressor(Strom.AN)

        # 1 schritt = ofen
        warte_auf_block_gesetzt()
        tür_öffnen(1)
        bewege_ofen(Richtung.REIN)
        block_brennen()
        bewege_ofen(Richtung.RAUS)
        tür_öffnen(0)
        
        # 2 schritt = transport Kran
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
        
        # 3 schritt = polierung
        bewege_drehteller(Richtung.RECHTS)
        polierer(1)
        time.sleep(4)
        polierer(0)
        
        
        # schritt 4 = transport Teller
        bewege_drehteller(Richtung.RECHTS)
        pusher(1)
        time.sleep(0.5)
        pusher(0)
        
        
        
        bewege_drehteller(Richtung.LINKS)
        bewege_drehteller(Richtung.LINKS)
        fließband_an(Richtung.RAUS)