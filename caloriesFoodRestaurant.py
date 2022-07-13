'''Universidade cruzeiro do sul
   Bruno Gonçalves de souza
   02/04/2022
   Exercício 14 - – Criar um programa que informe a quantidade total
   de calorias de uma refeição a partir do usuário que deverá informar
   o prato, a sobremesa e a bebida (veja a tabela a seguir). Sugestão:
   enumere cada opção de prato, sobremesa e bebida. Ou seja:
   Prato: 1 - vegetariano, 2 – Peixe, 3 – Frango, 4 – Carne;
   Sobremesa: 1 – Abacaxi, 2 – Sorvete diet, 3 – Mouse diet, 4
   – Mouse chocolate; Bebida: 1 – Chá, 2 - Suco de laranja, 3
   – Suco de melão, 4 – Refrigerante diet'''

print('''Opções de prato:
    0 - Nenhum
    1 - Vegetariano
    2 - Peixe
    3 - Frango
    4 - Carne''')
prato = int(input("Informe o prato desejado (ex: 1): "))
print("----------------------------------------------")
print('''Opções de Sobremesa:
    0 - Nenhum
    1 - Abacaxi
    2 - Sorvete diet
    3 - Mouse diet
    4 - Mouse choc''')
sobremesa = int(input("Informe a sobremesa desejada (ex: 2): "))
print("----------------------------------------------")
print('''Opções de Bebida:
    0 - Nenhum
    1 - Chá
    2 - Suco de laranja
    3 - Suco de melão
    4 - Refrig. diet''')
bebida = int(input("Informe a bebida desejada (ex: 4): "))
print("----------------------------------------------")
if  prato == 0:
    calorias1 = 0
elif prato == 1:
    calorias1 = 180
elif prato == 2:
    calorias1 = 230
elif prato == 3:
    calorias1 = 250
elif prato == 4:
    calorias1 = 350
else:
    calorias1 = 0
    print("Prato inválido")
    
if sobremesa == 0:
    calorias2 = 0
elif sobremesa == 1:
    calorias2 = 75
elif sobremesa == 2:
    calorias2 = 110
elif sobremesa == 3:
    calorias2 = 170
elif sobremesa == 4:
    calorias2 = 200
else:
    calorias2 = 0
    print("Sobremesa inválida")

if bebida == 0:
    calorias3 = 0
elif bebida == 1:
    calorias3 =20
elif bebida == 2:
    calorias3 =70
elif bebida == 3:
    calorias3 =100
elif bebida == 4:
    calorias3 = 65
else:
    calorias3 = 0
    print("Bebida inválida")
print("                   ")
print(f'''Prato: {calorias1} calorias
Sobremesa: {calorias2} calorias
Bebida: {calorias3} calorias

Total = {calorias1 + calorias2 + calorias3} calorias''')

    



