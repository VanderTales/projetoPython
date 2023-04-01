"""calculadora com while"""
while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite o operador(+-/*): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print('um dos numeros ou ambos são inválidos')
            continue
        
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('operador inválido.')
        continue
    if len(operador) > 1:
        print('digite apenas 1 operador')
        continue

    sair = input('quer sair? [s]im').lower().startswith('s')
    print (sair)
    if sair is True:
        break