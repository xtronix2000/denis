alph, keyw, txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "LEMON", "ATTACKATDAWN"



def vigenere(abc, text, key, state):
    tabula_recta = []
    for k in range(0, len(abc)):  # fill the aplhabet table
        tabula_recta.append(abc[k:] + abc[:-(len(abc) - k)])  # cyclic left shift
    j = 0
    while len(key) < len(text):  # fill key string
        key += key[j]
        j += 1
        if j == 5:
            j = 0
    for i in range(len(text)):
        if state:
            text += tabula_recta[tabula_recta[0].find(key[i])][tabula_recta[0].find(text[i])]  # encryption
        else:
            text += tabula_recta[0][tabula_recta[tabula_recta[0].find(key[i])].find(text[i])]  # decryption
    return text[int(len(text) / 2):]


# example
print("Plain text:", txt)
print("Encrypted:", vigenere(alph, txt, keyw, True))
print("Decrypted:", vigenere(alph, vigenere(alph, txt, keyw, True), keyw, False))
