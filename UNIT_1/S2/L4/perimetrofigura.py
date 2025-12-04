print("Benvenuto, in questo programma potrai calcolare il perimetro di una figura geometrica a scelta tra: ")
choice = int(input("1. Quadrato; \n2. Cerchio; \n3. Rettangolo. \ninserisci il numero corrispondente: "))

match choice:
    case 1:
        print("Hai scelto un quadrato.")
        lato = float(input("Inserisci la lunghezza del lato: "))
        print(f"La formula è lato*4, nel nostro caso il lato è {lato}")
        result = round(lato*4 , 2)
        print(f"Il risultato, arrotondato, è: {result}")
    case 2:
        print("Hai scelto un cerchio.")
        raggio = float(input("Inserisci la lunghezza del raggio: "))
        print(f"La formula è 2*Pi greco*raggio, nel nostro caso il raggio è {raggio}")
        result = round(2*3.14*raggio , 2)
        print(f"Il risultato, arrotondato, è: {result}")
    case 3:
        print("Hai scelto un rettangolo.")
        base = float(input("Inserisci la lunghezza della base: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        if base == altezza:
            print("Quello che hai inserito è un quadrato.")
            print(f"La formula è lato*4, nel nostro caso il lato è {base}")
            result = round(base*4 , 2)
            print(f"Il risultato, arrotondato, è: {result}")
        else:
            print(f"La formula è base*2+altezza*2, nel nostro caso la base è {base} e l'altezza è {altezza}")
            result = round((base*2)+(altezza*2), 2)
            print(f"Il risultato, arrotondato, è: {result}")
    case _ :
        print ("La figura che hai scelto non rientra nelle opzioni.")