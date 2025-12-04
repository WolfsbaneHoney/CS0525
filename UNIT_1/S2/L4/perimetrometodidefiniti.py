print("Benvenuto, in questo programma potrai calcolare il perimetro di una figura geometrica a scelta tra: ")
choice = int(input("1. Quadrato; \n2. Cerchio; \n3. Rettangolo. \ninserisci il numero corrispondente: "))

def perimetroquadrato(lato):
    print(f"La formula è lato*4, nel nostro caso il lato è {lato}")
    result = lato*4
    return result

def perimetrocerchio(raggio):
    print(f"La formula è 2*Pi greco*raggio, nel nostro caso il raggio è {raggio}")
    result = 2*3.14*raggio
    return result

def perimetrorettangolo(base, altezza):
    print(f"La formula è base*2+altezza*2, nel nostro caso la base è {base} e l'altezza è {altezza}")
    result = (base+altezza)*2
    return result

match choice:
    case 1:
        print("Hai scelto un quadrato.")
        lato = float(input("Inserisci la lunghezza del lato: "))
        result = round(perimetroquadrato(lato), 2)
    case 2:
        print("Hai scelto un cerchio.")
        raggio = float(input("Inserisci la lunghezza del raggio: "))
        result = round(perimetrocerchio(raggio), 2)
    case 3:
        print("Hai scelto un rettangolo.")
        base = float(input("Inserisci la lunghezza della base: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        if base == altezza:
            print("Quello che hai inserito è un quadrato.")
            result = round(perimetroquadrato(base), 2)
        else:
            result = round(perimetrorettangolo(base, altezza), 2)
            print(f"Il risultato, arrotondato, è: {result}")
    case _ :
        print ("La figura che hai scelto non rientra nelle opzioni.")

if result:
    print(f"Il risultato arrondato è {result}")