def césar(phrase, cle):
    acrypter = phrase.upper()
    lg = len(acrypter)
    MessageCrypte = ""

    for i in range(lg):
        if acrypter[i] == ' ':
            MessageCrypte += ' '
        else:
            asc = ord(acrypter[i]) + cle
            MessageCrypte += chr(asc + 26 * ((asc<65)-(asc>90)))

    return MessageCrypte

print(césar("Hello World",15))

