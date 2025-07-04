print('#'*15,'PESSOAS CADASTRADAS',15*'#')
maior = 0
mulher = 0
while True:
        sexo = (input('Digite seu sexo [M/F]: ')).upper()[0]
        if sexo != 'M' and sexo != 'F':
                print('Digite apenas M ou F:')
        print('-' * 20)
        idade = int(input('Digite sua idade: '))
        if idade > 17:
            maior = maior+1

        if sexo == 'F':
            if idade < 20:
                mulher += 1
        print('-' * 20)
        p = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if p == 'N':
            break
        print('='*20)
print(f'Há {maior}  maiores de idade.')
print(f'No total há {mulher} mulheres cadastradas menores de 20 anos.')
print(f'O sexo mais cadastrado foi {sexo}')