# Contando letras

def contarLetras(nome):
    qntd = 0
    
    for letra in nome:
        qntd += 1
    return qntd

nome = input('Digite um nome: ')
qntdLetras = contarLetras(nome)

print(f'{nome} tem {qntdLetras}')
