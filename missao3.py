# Recuperando o Sistema de Notas

nota = int(input('Digite sua nota: '))

if nota >= 90 and nota <= 100:
    print(f'Parabéns, você tirou A.')
elif nota >= 80 and nota <= 89:
    print(f'Muito bem, você tirou B.')
elif nota >= 70 and nota <= 79:
    print(f'Bom trabalho, você tirou C.')
elif nota >= 60 and nota <= 69:
    print(f'Fique atento, você tirou D.')
elif nota < 60 and nota >= 0:
    print(f'Estude um pouco mais, você tirou F.')
else:
    print(f'Valor inválido tente novamente!')