import hashlib
def encontrar_hash(hash_o):
    hash_i = ""
    cont = 0
    while hash_o != hash_i:
        m = hashlib.sha256()
        cadena = ("0"*(10-len(str(cont)))+str(cont))
        m.update(cadena.encode("utf-8"))
        hash_i= m.hexdigest()
        cont +=1

    return cadena

