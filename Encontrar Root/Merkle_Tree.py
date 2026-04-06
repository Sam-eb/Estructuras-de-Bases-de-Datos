import hashlib
class Merkle_Tree():

    def hash_text(self, text):
        m = hashlib.sha256(text.encode())
        hash = m.hexdigest()
        return hash

    def hash_texts(self, texts):
    
        hashed_texts = []
        for text in texts:
            m = hashlib.sha256(text.encode())
            hash = m.hexdigest()
            hashed_texts.append(hash)
        return hashed_texts

    def __init__(self, texts):
        self.root = None
        self.texts = self.hash_texts(texts)
        self.hojas = [self.hash_texts(texts)]

    def calcular_hojas(self):
        new_hashed_texts = []
        for i in range(0, len(self.texts), 2):
            if (i == len(self.texts)-1):
                new_hashed_texts.append(self.texts[i])
                break
            text1 = self.texts[i]    
            text2 = self.texts[i + 1]
            new_text = text1 + text2
            hashed_new_text = self.hash_text(new_text)
            new_hashed_texts.append(hashed_new_text)
        self.texts = new_hashed_texts
        self.hojas.append(new_hashed_texts)

    def calcular_merkle_root(self):
        while (len(self.texts) != 1):
            self.calcular_hojas()
        self.root = self.texts



