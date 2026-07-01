import os
import time


def menu():

    print("Benvenuti alla rubrica di nomi e numeri!\n Inserire i dati desiderati per proseguire\n---------------")
    time.sleep(2)


def rubrica_nomi():

    nome = input("Che nome vuoi scegliere? => ")
    
    if not os.path.exists("names.txt"):
        f = open("names.txt", "x")

    file_nomi = open("names.txt", "a")
    file_nomi.write(f"{nome}")
    file_nomi.close()

    file_nomi = open("names.txt", "r")
    file_nomi.read()
    file_nomi.close()


def rubrica_telefono():

    print("Ora è il momento di salvare il tuo numero di telefono!\n---------------")
    time.sleep(2)

    telefono = int(input)



menu()
rubrica_nomi()
rubrica_telefono()
