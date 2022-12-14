def vocales(frase):
    listavocales = "aeiou"
    resultado = ""
    if len(frase) > 0:
        if frase[0].lower() in listavocales:
            resultado = frase[0] + vocales(frase[1:])
        else:
            resultado = vocales(frase[1:])
    return resultado

def orden(frase):
    return "".join(sorted(frase, key=str.upper))
frase = input("Introduce una frase: ")
print(orden(frase))

