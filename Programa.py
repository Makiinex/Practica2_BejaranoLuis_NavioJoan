def vocales(frase):
    listavocales = "aeiou"
    resultado = ""
    if len(frase) > 0:
        if not frase[0].lower() in listavocales:
            resultado = frase[0] + vocales(frase[1:])
        else:
            resultado = vocales(frase[1:])
    return resultado

def inverso(frase):
    resultado = ""
    if len(frase) > 0:
        resultado = frase[-1] + inverso(frase[:-1])
    return resultado

def consonantes(frase):
    listavocales = "aeiou"
    resultado = ""
    if len(frase) > 0:
        if frase[0].lower() in listavocales:
            resultado = frase[0] + consonantes(frase[1:])
        else:
            resultado = consonantes(frase[1:])
    return resultado

def orden(frase):
    return "".join(sorted(frase, key=str.upper))
frase = input("Introduce una frase: ")
print(orden(frase))

menu00 = "\nQuè vols fer?\n1. Elimina les vocals\n2. Elimina les " \
         "consonants\n3. Ordena la frase al revés i printala per pantalla\n4. Ordena les " \
         "paraules de la frase en ordre ascendent i printales per pantalla\n5. Sortir"
salir = False
flg00 = True

while not salir:
    frase = input("Introduce una frase: ")
    if frase == "":
        print("La frase no pot estar buida!")
    if frase.isspace():
        print("La frase no pot estar buida!")
    else:
        while flg00:
            print(menu00)
            opt = input("\nOption: ")
            if not opt.isdigit():
                print("Només es poden posar nombres!")
            if not int(opt) in range(1,6):
                print("Opció incorrecta")
            else:
                opt = int(opt)
                if opt == 1:
                    print(vocales(frase))
                if opt == 2:
                    print(consonantes(frase))
                if opt == 3:
                    print(inverso(frase))
                if opt == 4:
                    print(orden(frase))
                if opt == 5:
                    flg00 = False
                    salir = True