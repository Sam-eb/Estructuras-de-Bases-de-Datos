import os 
import time
with open("Matriz_guide.txt", "w") as arc:
    arc.write("100000")

with open("Matriz_one.txt", "w") as m:
    m.write(" ")
    start = time.localtime()
    while (os.path.getsize("Matriz_one.txt") < 10**10):
        m.write("11111111111111111111111111111111")
    end = time.localtime()
    print("Demoro un total de:", end - start)

