from state import REGISTERS
import re

def execute(opcode, operands):
    if opcode == 'MOV':
        mov(operands[0], operands[1])

def mov(dest, src):
    if dest in REGISTERS:
        if src.startswith('#'):
            value = src[1:].upper()
            # Handle common formats: 10H, 0x10, or raw hex (e.g., 10)
            if value.endswith('H'):
                value = value[:-1]
            elif value.startswith('0X'):
                value = value[2:]
            if not re.match(r'^[0-9A-F]{1,2}$', value):
                raise ValueError(f"Invalid immediate value: '{src}'. Must be a 1-2 digit hexadecimal (e.g., #10, #1AH, #0x10).")
            # Pad to 2 digits if single digit
            value = value.zfill(2)
            REGISTERS[dest] = value
        elif src in REGISTERS:
            REGISTERS[dest] = REGISTERS[src]
        else:
            raise ValueError(f"Invalid source for MOV: '{src}'. Must be a register or immediate value.")
    else:
        raise ValueError(f"Invalid destination for MOV: '{dest}'. Must be a valid register.")