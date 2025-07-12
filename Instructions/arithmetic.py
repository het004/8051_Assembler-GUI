from state import REGISTERS, FLAGS
from utils.utilis import add_8bit, sub_8bit
from flags import set_flags_after_add, set_flags_after_subb

def execute(opcode, operands):
    if opcode == 'ADD':
        add(operands[0], operands[1])
    elif opcode == 'SUBB':
        subb(operands[0], operands[1])
    elif opcode == 'INC':
        inc(operands[0])
    elif opcode == 'DEC':
        dec(operands[0])

def add(dest, src):
    if dest == 'A' and src.startswith('#'):
        value = src[1:].upper()
        if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
            raise ValueError("Invalid immediate value")
        a = REGISTERS['A']
        result = add_8bit(a, value)
        REGISTERS['A'] = result
        set_flags_after_add(a, value, result)
    elif dest == 'A' and src in REGISTERS:
        a = REGISTERS['A']
        value = REGISTERS[src]
        result = add_8bit(a, value)
        REGISTERS['A'] = result
        set_flags_after_add(a, value, result)
    else:
        raise ValueError("Invalid operands for ADD")

def subb(dest, src):
    if dest == 'A' and src.startswith('#'):
        value = src[1:].upper()
        if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
            raise ValueError("Invalid immediate value")
        a = REGISTERS['A']
        result = sub_8bit(a, value, FLAGS['CY'])
        REGISTERS['A'] = result
        set_flags_after_subb(a, value, result, FLAGS['CY'])
    elif dest == 'A' and src in REGISTERS:
        a = REGISTERS['A']
        value = REGISTERS[src]
        result = sub_8bit(a, value, FLAGS['CY'])
        REGISTERS['A'] = result
        set_flags_after_subb(a, value, result, FLAGS['CY'])
    else:
        raise ValueError("Invalid operands for SUBB")

def inc(reg):
    if reg in REGISTERS:
        value = REGISTERS[reg]
        result = add_8bit(value, '01')
        REGISTERS[reg] = result
        set_flags_after_add(value, '01', result)
    else:
        raise ValueError("Invalid register for INC")

def dec(reg):
    if reg in REGISTERS:
        value = REGISTERS[reg]
        result = sub_8bit(value, '01', '0')
        REGISTERS[reg] = result
        set_flags_after_subb(value, '01', result, '0')
    else:
        raise ValueError("Invalid register for DEC")