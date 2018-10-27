import random

orzel = 0
reszka = 0
rzut = 0

while rzut != 100:
    moneta = random.randint(1,2)
    if moneta == 1:
        orzel += 1
    else:
        reszka += 1
    rzut += 1

print("Wyrzucono", orzel, "razy orła i", reszka, "razy reszkę")
input("\n\nAby zakończyć program, naciśnij klawisz Enter")
