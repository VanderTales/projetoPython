'''
iteravel -> str, range, etc(_iter_)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''
''''''
#for letra in texto
texto = 'luiz' # iteravel
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break