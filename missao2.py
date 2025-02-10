# Sistema Eleitoral Secreto

# Idade
idade = int(input('Digite sua idade: '))

if idade >= 18 and idade < 70:
    print(f'Sua idade é {idade} seu voto é obrigatório')
elif (idade >= 16 and idade < 18) or idade >= 70:
    print(f'Sua idade é {idade} seu voto é opcional')
else:
    print(f'Sua idade é {idade} você não pode votar')