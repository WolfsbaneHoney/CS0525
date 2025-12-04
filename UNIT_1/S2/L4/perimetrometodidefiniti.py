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
        result = perimetroquadrato(lato)
    case 2:
        print("Hai scelto un cerchio.")
        raggio = float(input("Inserisci la lunghezza del raggio: "))
        result = perimetrocerchio(raggio)
    case 3:
        print("Hai scelto un rettangolo.")
        base = float(input("Inserisci la lunghezza della base: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        if base == altezza:
            print("Quello che hai inserito è un quadrato.")
            result = perimetroquadrato(base)
        else:
            result = perimetrorettangolo(base, altezza)

try:
    print(f"Il risultato arrondato è {result:.2f}")
except:
    print ("La figura che hai scelto non rientra nelle opzioni.")
