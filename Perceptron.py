import random

waga = []
tabela = []
# unipolarny = przedział albo wybór (między) 0 i/a 1
# dyskretny = 0 lub 1, boolean
#input array/lista
#waga array/lista
#prog = round(float(random.random()),2)

#przyjmuję wektor wejść i zwracam odpowiedź perceptrona
#def compute():

#przyjmuję wektor wejść i poprawną odpowiedź, i tu wsadzam regułe delta do modyfikacji progu
#def learn():

    #reguła delta

with open ("C:/Users/frane/OneDrive/Pulpit/iris.txt") as plik:
    next(plik)
    for line in plik:
        tabela.append(line)
print(tabela)
#generator wag losowych
for i in range(5):
    waga.append(round(float(random.random()),2))
print(waga)
print(sum(waga))
print(waga[3])