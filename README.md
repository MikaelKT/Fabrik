# Fabrik

ohne pneumatik:

O_1 = drehteller dreht nach rechts
O_2 = drehteller dreht nach links
O_3 = fließband an
O_4 = polierer(säge idk)
O_5 = ofen reinfahren
O_6 = ofen ausfahren
O_7 = kran nach links
O_8 = kran nach rechts
O_9 = rote lampe (brenner)

mit pneumatik:

O_10 = kompressor an
O_11 = saugnapf an
O_12 = kran saugnapf halter herunterfahren
O_13 = ofentür nach oben
O_14 = drücker zum material schubsen

i_10 = drehtellererkennungsknopf




revpi.io.O_8.value = 1
while revpi.io.I_6.value == 0:
    pass
revpi.io.O_8.value = 0



1 bei lichtschranke heißt = nicht unterbrochen (also sie bekommt strom genau das gegenteil eines knopfes der bei 1 strom bekommt)
0 bei lichtschranke heißt = unterbrochen (also sie bekommt kein strom)




