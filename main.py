"""
methode main composée de deux fonctions
"""
from math import sqrt
#### Fonction secondaire


def isprime(p):
    """
    Retourne un boolean qui répond à la question:
    est ce que p est premier
    """
    if p == 1:
        return False
    for i in range(2,int(sqrt(p))+1):
        if p%i == 0:
            return False
    return True
#### Fonction principale


def main():
    """
    La fonction main fait appel à is prime pour tester son bon fonctionnement
    """
    # vos appels à la fonction secondaire ici
    print(isprime(1))
    print(isprime(2))
    print(isprime(4))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
