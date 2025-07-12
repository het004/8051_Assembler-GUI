from state import REGISTERS, FLAGS
from utils import hex_to_binary, binary_to_hex

def execute(opcode, operands):
    if opcode == 'RL':
        rl(operands[0])
    elif opcode == 'RR':
        rr(operands[0])
    elif opcode == 'RLC':
        rlc(operands[0])
    elif opcode == 'RRC':
        rrc(operands[0])
    elif opcode == 'SWAP':
        swap(operands[0])

def rl(reg):
    if reg == 'A':
        a = hex_to_binary(REGISTERS['A'], 8)
        result = a[1:] + a[0]
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['CY'] = a[0]
    else:
        raise ValueError("RL only supports A")

def rr(reg):
    if reg == 'A':
        a = hex_to_binary(REGISTERS['A'], 8)
        result = a[-1] + a[:-1]
        REGISTERS['A'] = binary_to_hex(result, 1)
        FLAGS['CY'] = a[-1]
    else:
        raise ValueError("RR only supports A")

def rlc(reg):
    if reg == 'A':
        a = hex_to_binary(REGISTERS['A'], 8)
        result = a[1:] + FLAGS['CY']
        FLAGS['CY'] = a[0]
        REGISTERS['A'] = binary_to_hex(result, 1)
    else:
        raise ValueError("RLC only supports A")

def rrc(reg):
    if reg == 'A':
        a = hex_to_binary(REGISTERS['A'], 8)
        result = FLAGS['CY'] + a[:-1]
        FLAGS['CY'] = a[-1]
        REGISTERS['A'] = binary_to_hex(result, 1)
    else:
        raise ValueError("RRC only supports A")

def swap(reg):
    if reg == 'A':
        a = hex_to_binary(REGISTERS['A'], 8)
        result = a[4:] + a[:4]
        REGISTERS['A'] = binary_to_hex(result, 1)
    else:
        raise ValueError("SWAP only supports A")