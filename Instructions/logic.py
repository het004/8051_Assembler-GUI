from state import REGISTERS, FLAGS
from utils import hex_to_binary, binary_to_hex

def execute(opcode, operands):
    if opcode == 'ANL':
        anl(operands[0], operands[1])
    elif opcode == 'ORL':
        orl(operands[0], operands[1])
    elif opcode == 'XRL':
        xrl(operands[0], operands[1])
    elif opcode == 'CPL':
        cpl(operands[0])

def anl(dest, src):
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
                raise ValueError("Invalid immediate value")
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError("Invalid source for ANL")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('1' if bin_a[i] == '1' and bin_b[i] == '1' else '0' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def orl(dest, src):
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
                raise ValueError("Invalid immediate value")
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError("Invalid source for ORL")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('1' if bin_a[i] == '1' or bin_b[i] == '1' else '0' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def xrl(dest, src):
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
                raise ValueError("Invalid immediate value")
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError("Invalid source for XRL")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('0' if bin_a[i] == bin_b[i] else '1' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def cpl(reg):
    if reg == 'A':
        a = REGISTERS['A']
        bin_a = hex_to_binary(a, 8)
        result = ''.join('0' if bit == '1' else '1' for bit in bin_a)
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'
    else:
        raise ValueError("CPL only supports A")