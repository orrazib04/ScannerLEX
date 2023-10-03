import ply.lex as lex

tokens = ['PC', 'ID', 'SIGNO', 'OPREL', 'NUMERO']
palabraClave = {'SELECT', 'FROM', 'WHERE','BY'}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in palabraClave:
        t.type = 'PC'
    return t

t_SIGNO = r'[,.]'

t_OPREL = r'[<>=]+'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f'Carácter no identificado: "{t.value[0]}"')
    t.lexer.skip(1)

lexer = lex.lex()

def analizador(cadena):
    lexer.input(cadena)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f'{token.type}: {token.value}')

print("\na)")
entrada = "Select name FroM table2 WHEre a2 >= = < 15"
analizador(entrada)
print("\nb)")
entrada = "SELECT col1, col2 from mi_Tabla wHERE col1 < 20"
analizador(entrada)
