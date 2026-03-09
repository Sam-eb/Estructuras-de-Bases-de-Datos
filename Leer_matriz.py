with open ("Matriz_one.txt", "r", encoding='utf-8') as file:
    cont = -1
    while True:
        cont += 1
        bloque = file.read(320)
        if not bloque:
            break
    print(cont)