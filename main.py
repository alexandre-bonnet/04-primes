from math import sqrt

#### Fonction secondaire


def isprime(p):
    from math import sqrt
    for i in range(2,int(sqrt(val))+1):
        if val%i == 0:
            return False
            break
    else :
        return True
    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    val = eval(input("Entrez le nombre à vérifier"))
    if(isprime(val)):
        print("Ce nombre est premier")
    else :
        print("Ce nombre n'est pas premier")

    isprime(1)
    isprime(2)
    isprime(4)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
