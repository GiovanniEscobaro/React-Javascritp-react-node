edad=input("Danos tu edad por favor: ")
edad=int(edad)
if edad<=13:
    print(f"Eres un niño de {edad}")
elif edad>13 and edad<= 17 :
    print(f"Eres adolecente de {edad}")
elif edad>18 and edad<= 64 :
    print(f"Eres adulto de {edad}")
elif edad>65:
    print(f"Eres adulto moyor de {edad}")

# Bucles while y for

contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1

for numero in range(0, 5):
    print("Número for:", numero)

numero=int(input('Que tabla quieres ver: '))
for i in range(0,11):
    resultadotabla= numero * i
    print(f"{numero} * {i} = {resultadotabla}")
