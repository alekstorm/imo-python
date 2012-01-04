from imo import *

def Eq(a, b):
    return BinaryOperator('=', a, b)

def Neq(a, b):
    return BinaryOperator('<>', a, b)

def Gt(a, b):
    return BinaryOperator('>', a, b)

def Lt(a, b):
    return BinaryOperator('<', a, b)

def Gte(a, b):
    return BinaryOperator('>=', a, b)

def Lte(a, b):
    return BinaryOperator('<=', a, b)

def Not(a):
    return UnaryOperator('!', a)

def Or(a, b):
    return BinaryOperator('|', a, b)

def And(a, b):
    return BinaryOperator('&', a, b)

def In(a, elems):
    return ListOperator('in', a, elems)

def Lower(value):
    return Function('lower', value)

def Nvl(param1, param2):
    return Function('nvl', param1, param2)

def To_Boolean(value):
    return Function('to_boolean', value)

def To_Date(value, format=None):
    return Function('to_date', *[value, format] if format else value)

def To_Float(value):
    return Function('to_float', value)

def To_Integer(value):
    return Function('to_integer', value)

def To_String(value, format=None):
    return Function('to_string', *[value, format] if format else value)

def Trunc(value):
    return Function('trunc', value)
