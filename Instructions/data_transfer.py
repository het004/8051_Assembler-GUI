from state import REGISTERS

def execute(opcode, operands):
    if opcode == 'MOV':
        mov(operands[0], operands[1])

def mov(dest, src):
    if dest in REGISTERS:
        if src.startswith('#'):
            value = src[1:].upper()
            if len(value) != 2 or not all(c in '0123456789ABCDEF' for c in value):
                raise ValueError("Invalid immediate value")
            REGISTERS[dest] = value
        elif src in REGISTERS:
            REGISTERS[dest] = REGISTERS[src]
        else:
            raise ValueError("Invalid source for MOV")
    else:
        raise ValueError("Invalid destination for MOV")