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

