import re
from state import REGISTERS, FLAGS
from utils import hex_to_binary, binary_to_hex

def execute(opcode, operands):
    print(f"Executing {opcode} with operands {operands}")  # Debug
    if opcode == 'ANL':
        anl(operands[0], operands[1])
    elif opcode == 'ORL':
        orl(operands[0], operands[1])
    elif opcode == 'XRL':
        xrl(operands[0], operands[1])
    elif opcode == 'CPL':
        cpl(operands[0])

def anl(dest, src):
    print(f"ANL: dest={dest}, src={src}")  # Debug
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if value.endswith('H'):
                value = value[:-1]
            elif value.startswith('0X'):
                value = value[2:]
            if not re.match(r'^[0-9A-F]{1,2}$', value):
                raise ValueError(f"Invalid immediate value: '{src}'. Must be a 1-2 digit hexadecimal (e.g., #10, #1AH, #0x10).")
            value = value.zfill(2)
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError(f"Invalid source for ANL: '{src}'. Must be a register or immediate value.")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('1' if bin_a[i] == '1' and bin_b[i] == '1' else '0' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def orl(dest, src):
    print(f"ORL: dest={dest}, src={src}")  # Debug
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if value.endswith('H'):
                value = value[:-1]
            elif value.startswith('0X'):
                value = value[2:]
            if not re.match(r'^[0-9A-F]{1,2}$', value):
                raise ValueError(f"Invalid immediate value: '{src}'. Must be a 1-2 digit hexadecimal (e.g., #10, #1AH, #0x10).")
            value = value.zfill(2)
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError(f"Invalid source for ORL: '{src}'. Must be a register or immediate value.")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('1' if bin_a[i] == '1' or bin_b[i] == '1' else '0' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def xrl(dest, src):
    print(f"XRL: dest={dest}, src={src}")  # Debug
    if dest == 'A':
        a = REGISTERS['A']
        if src.startswith('#'):
            value = src[1:].upper()
            if value.endswith('H'):
                value = value[:-1]
            elif value.startswith('0X'):
                value = value[2:]
            if not re.match(r'^[0-9A-F]{1,2}$', value):
                raise ValueError(f"Invalid immediate value: '{src}'. Must be a 1-2 digit hexadecimal (e.g., #10, #1AH, #0x10).")
            value = value.zfill(2)
        elif src in REGISTERS:
            value = REGISTERS[src]
        else:
            raise ValueError(f"Invalid source for XRL: '{src}'. Must be a register or immediate value.")
        bin_a = hex_to_binary(a, 8)
        bin_b = hex_to_binary(value, 8)
        result = ''.join('0' if bin_a[i] == bin_b[i] else '1' for i in range(8))
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'

def cpl(reg):
    print(f"CPL: reg={reg}")  # Debug
    if reg == 'A':
        a = REGISTERS['A']
        bin_a = hex_to_binary(a, 8)
        result = ''.join('0' if bit == '1' else '1' for bit in bin_a)
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['P'] = '1' if result.count('1') % 2 == 0 else '0'
    else:
        raise ValueError("CPL only supports A")