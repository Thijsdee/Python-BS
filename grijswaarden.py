'''
Dit Progamma is geschreven door Thijs Deelstra
Leerlingnummer = 134203
'''

# bereken het gemiddelde van de r,g,b en doe dat in een hex kleur string
def berekenGrijsWaarde(rood, groen, blauw):
    gemiddelde = int((rood + groen + blauw) / 3)
    gemiddeldehex = str(hex(gemiddelde)[2:]) 
    grijsWaardeRes = ""
    for i in range(0,3):
        grijsWaardeRes += gemiddeldehex 
    return grijsWaardeRes

# Intro
print("Grijstint berekenen!")

# Vraag de hexadecimale waarde aan de gebruiker
kleurHex = str(input("Geef de hexadecimale kleur, laat 0x weg: "))
 
# Deel rood, groen en blauw op in delen
tintRood = int(kleurHex[0:2],16)
tintGroen = int(kleurHex[2:4],16)
tintBlauw = int(kleurHex[4:6],16)

# Roept de functie berekenGrijsWaarde op en geeft de rgb waardes mee
grijswaarde = berekenGrijsWaarde(tintRood, tintGroen, tintBlauw)
 
#Geef het resultaat weer (let op, bestaat uit 6 hexadecimalen).
print("De grijswaarde is:", grijswaarde)