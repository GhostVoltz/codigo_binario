# Autor: Ghost Voltz 👻⚡
# Data: 02/10/2023
# Linguagem: Python 3.6

from cmd import Cmd

class TextoBinarioApp(Cmd):
    def __init__(mi):
        super().__init__()
        mi.codigo = 'utf8'
    
    def do_codigo(mi, argumento):
        'Defina o codigo (ascii, utf8, etc.) para '\
        'codificar/decodificar.'
        codigo = argumento.strip()
        try:
            bytearray('', codigo)
        except LookupError:
            print('**Código desconhecido.')
        else: mi.codigo = codigo

    def do_codificar(mi, argumento):
        'Codifica um texto em binario.'
        try:
            octetos = bytearray(argumento, mi.codigo)
        except:
            print(f'**Não pode codificar em {mi.codigo}.')
        else: print(' '.join(f'{x:b}'.rjust(8, '0') for x in octetos))

    def do_decodificar(mi, argumento):
        'Decodifica um texto em binario.'
        try:
            octetos = bytearray(int(x, 2) for x in argumento.split())
        except:
            print('**Não é uma corrente binaria.')
            return None
        try:
            print(octetos.decode(encoding=mi.codigo))
        except: print(f'**Não é uma corrente codificada em {mi.codigo}')

    def do_salir(mi, arg):
        'Sair do programa.'
        return True

app = TextoBinarioApp()
app.cmdloop()
