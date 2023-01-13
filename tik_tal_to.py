felder = [[2,2,2],
          [2,2,2],
          [2,2,2]]
print(felder[0],"\n", felder[1],"\n", felder[2])
zähler = 0
#################################################################
while zähler < 5:
    reihe = int(input("Spieler 0 wähle eine reihe:"))
    spalte = int(input("Spieler 0 wähle eine spalte:"))
    while felder[reihe][spalte] == 1 or felder[reihe][spalte] == 0:
        print("Feld schon besetzt")
        reihe = int(input("Spieler 0 wähle eine reihe:"))
        spalte = int(input("Spieler 0 wähle eine spalte:"))
    felder[reihe][spalte] = 0
    print(felder[0],"\n", felder[1],"\n", felder[2])
    a = 0
    b = 0
    c = 1
    d = 2
    x = 1
    while a < 3:
        if felder[a][b] == felder[a][c] == felder[a][d] and felder[a][b] != 2:
            if felder[a][b] == 0:
                print("Spieler 0 hat gewonnena")
                exit()
            else:
                print("Spieler 1 hat gewonnenb")
                exit()
        else:
            a = a + 1
    while b < 3:
        a = 0
        if felder[a][b] == felder[c][b] == felder[d][b] and felder[a][b] != 2:
            if felder[a][b] == 0:
                print("Spieler 0 hat gewonnenc")
                exit()
            else:
                print("Spieler 1 hat gewonnend")
                exit()
        else:
            b = b + 1
    b = 0
    if (felder[0][0] == felder[1][1] == felder[2][2] or felder[2][0] == felder[1][1] == felder[0][2]) and felder[1][1] != 2:
        if felder[1][1] == 0:
            print("Spieler 0 hat gewonnene")
            exit()
        else:
            print("Spieler 1 hat gewonnenf")
            exit()
    else:
        if zähler == 4:
            print("unentschieden")
            exit()
#######################################################
    reihe = int(input("Spieler 1 wähle eine reihe:"))
    spalte = int(input("Spieler 1 wähle eine spalte:"))
    while felder[reihe][spalte] == 1 or felder[reihe][spalte] == 0:
        print("Feld schon besetzt")
        reihe = int(input("Spieler 1 wähle eine reihe:"))
        spalte = int(input("Spieler 1 wähle eine spalte:"))
    felder[reihe][spalte] = 1
    print(felder[0],"\n",felder[1],"\n",felder[2])
    a = 0
    b = 0
    c = 1
    d = 2
    x = 1
    while a < 3:
        if felder[a][b] == felder[a][c] == felder[a][d] and felder[a][b] != 2:
            if felder[a][b] == 0:
                print("Spieler 0 hat gewonneng")
                exit()
            else:
                print("Spieler 1 hat gewonnenh")
                exit()
        else:
            a = a + 1
    a = 0
    while b < 3:
        if felder[a][b] == felder[c][b] == felder[d][b] and felder[a][b] != 2:
            if felder[a][b] == 0:
                print("Spieler 0 hat gewonneni")
                exit()
            else:
                print("Spieler 1 hat gewonnenj")
                exit()
        else:
            b = b + 1
    b = 0
    if (felder[0][0] == felder[1][1] == felder[2][2] or felder[2][0] == felder[1][1] == felder[0][2]) and felder[1][1] != 2:
        if felder[1][1] == 0:
            print("Spieler 0 hat gewonnenk")
            exit()
        else:
            print("Spieler 1 hat gewonnenl")
            exit()
    else:
        zähler = zähler + 1
print("unentschieden")

