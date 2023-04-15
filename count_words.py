def  count_words(frase):
    diccionario = {
        
    }
    lista = frase.split(" ")
    for i in lista:
        i = i.lower()
        n = 0
        x = 0
        while x != len(lista):
            palabra = lista[x].lower()
            if palabra == i:
                n += 1
            x += 1
        diccionario [i] = n
    return diccionario