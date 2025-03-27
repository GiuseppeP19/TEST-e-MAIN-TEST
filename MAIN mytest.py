from mytest import somma
from mytest import sottrazione
from mytest import moltiplicazione
from mytest import divisione

def menu():
    print("1, Somma")
    print("2, Sottrazione")
    print("3, Moltiplicazione")
    print("4, Divisione")
    return input()


if __name__ == "__main__":
    while True:
        scelta = menu()
        if scelta == "1":
           somma()
        elif scelta == "2": 
            sottrazione()    
        elif scelta == "3":
            moltiplicazione()
        elif scelta == "4":
            divisione()
       