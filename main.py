

print("Bora comer aquele lanchão ?")

basico = 0
completo = 0
cao = 0

while True:

    print("Lanche Básico ( B ) : R$ 5")
    print("Lanche Completo ( C ) : R$ 12")
    print("Lanche do Cão ( K ): R$ 50")

    print("Quer mais nada ? ( N )")


    resposta = input()

    if resposta == "B":
        basico = basico + 1
        print("Lanche basico comprado")
    elif resposta == "C":
        completo = completo + 1
        print("Lanche completo comprado")
    elif resposta == "K":
        cao = cao + 1
        print("Lanche cao comprado")
    elif resposta == "N":
        break
    else:
        print("Não entendi, repita")


gasto = basico*5 + completo*12 + cao*50
print(f"Voce gastou : {gasto}")
