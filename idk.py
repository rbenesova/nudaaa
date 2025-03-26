while True:
    secteni = input("jakou chcete pocetni operaci")
    a = int(input("zadejte prvini cislo"))
    b = int(input("zadejte druhe cislo"))
    if secteni == "scitani":
        print(a+b)
    elif secteni == "odcitani":
        print(a-b)
    elif secteni == "nasobeni":
        print(a*b)
    elif secteni == "deleni":
        print(a/b)
    papa = input("jestli uz nic necgcete napiste papa")
    if papa == "papa":
        break