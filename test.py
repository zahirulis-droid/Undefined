import ply.lex as lex

# =========================================================
# PALABRAS RESERVADAS
# =========================================================

reserved = {
    'when': 'WHEN',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'do': 'DO',
    'end': 'END',
    'every': 'EVERY',

    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    'true': 'BOOL_TOKEN',
    'false': 'BOOL_TOKEN',
    'on': 'BOOL_TOKEN',
    'off': 'BOOL_TOKEN',
}

# =========================================================
# TOKENS
# =========================================================

tokens = [

    # Identificadores
    'IDENT_SENSOR',
    'IDENT_ACTUADOR',

    # Valores
    'TEMP_TOKEN',
    'PERCENT_TOKEN',
    'TIME_TOKEN',
    'ILUM_TOKEN',
    'HORA_TOKEN',
    'EMAIL_TOKEN',
    'TEXTO_TOKEN',

    # Operadores
    'OP_COMP',
    'OP_BOOL',
    'ASIGNACION',

    # Símbolos
    'PUNTO',

] + list(set(reserved.values()))

# =========================================================
# TOKENS SIMPLES
# =========================================================

# Operadores de comparación
t_OP_COMP = r'==|!=|>=|<=|>|<'

# Operadores booleanos
t_OP_BOOL = r'==|!='

# Asignación
t_ASIGNACION = r'='

# Punto
t_PUNTO = r'\.'

# =========================================================
# TOKENS COMPLEJOS
# =========================================================

# Temperatura: 25°C
def t_TEMP_TOKEN(t):
    r'\d+°C'
    return t

# Porcentaje: 80%
def t_PERCENT_TOKEN(t):
    r'\d+%'
    return t

# Tiempo: 30m, 10s, 2h
def t_TIME_TOKEN(t):
    r'\d+[smh]'
    return t

# Iluminación: 900lux
def t_ILUM_TOKEN(t):
    r'\d+lux'
    return t

# Hora: 22:00
def t_HORA_TOKEN(t):
    r'\d{2}:\d{2}'
    return t

# Email
def t_EMAIL_TOKEN(t):
    r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return t

# Texto entre comillas
def t_TEXTO_TOKEN(t):
    r'\".*?\"'
    return t

# =========================================================
# IDENTIFICADORES
# =========================================================

# Sensores
def t_IDENT_SENSOR(t):
    r'sensor_[a-zA-Z_]+'
    return t

# Actuadores / palabras reservadas
def t_IDENT_ACTUADOR(t):
    r'[a-zA-Z_]+'

    # No distinguir mayúsculas/minúsculas
    value = t.value.lower()

    # Verificar si es palabra reservada
    if value in reserved:
        t.type = reserved[value]

    return t

# =========================================================
# IGNORAR ESPACIOS Y TABS
# =========================================================

t_ignore = ' \t'

# =========================================================
# SALTOS DE LINEA
# =========================================================

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# =========================================================
# MANEJO DE ERRORES
# =========================================================

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# =========================================================
# CREAR LEXER
# =========================================================

lexer = lex.lex()

# =========================================================
# ENTRADA DE PRUEBA
# =========================================================

data = input("Ingresar codigo: ")

# =========================================================
# ANALIZAR ENTRADA
# =========================================================

lexer.input(data)

# =========================================================
# MOSTRAR TOKENS
# =========================================================

while True:

    tok = lexer.token()

    if not tok:
        break

    print(tok)