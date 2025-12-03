import re

def countwordoccurency(text):
    text = re.sub(r"^\w\s", " ", text.lower())
    words = text.split()
    count = {} #dizionario con chiave = parola, valore = numero delle parole
    for word in words:
        if word in count:
            count[word] += 1
        else: 
            count[word] = 1
    return count

userinput = input("Inserisci un testo di cui contare le parole: ")

print(countwordoccurency(userinput))