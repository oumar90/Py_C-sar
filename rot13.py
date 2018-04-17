
def rot13(s):
    result = ""

    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result

# Test method.
if __name__ == '__main__':
  while 1:  
    print("##################################################################")
    print("#                                                                #")
    print("#         Author : Oumar Djimé Ratou                             #")
    print("#         Algorithme : ROT13                                     #")
    print("#                                                                #")
    print("##################################################################")

    print()

    print("***************************************************************************")
    print("************     Chiffrement et dechiffrement de rot13*********************")
    print("************  (C) Chiffrement.                       *******************")
    print("************  (D) Déchiffrement.                     *******************")
    print("************  (Q) Quitter.                           *******************")
    print("***************************************************************************")
    choix = input("Veillez choisir votre choix :").upper()

    if choix == 'C':
        message = input("Veillez entrer le message à chiffrer :")
        print("Le message crypté est : {}.".format(rot13(message)))
    elif choix == 'D':    
        message1 = input("Veillez entrer le message à déchiffrer :")
        print("Le message decrypté est {}.".format(rot13(rot13(message1))))
    else:
        print("Merci d'avoir utiliser cette programme")
        break    