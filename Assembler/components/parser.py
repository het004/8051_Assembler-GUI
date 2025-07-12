import re

SUPPORTED_INSTRUCTIONS = {'MOV', 'ADD', 'SUBB', 'INC', 'DEC', 'ANL', 'ORL', 'XRL', 'CPL', 'RL', 'RR', 'RLC', 'RRC', 'SWAP'}

def parse_code(code):
    instructions = []
    errors = []
    lines = code.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        if line.endswith(':'):
            # Label detected, store if jumps are added later
            continue
        tokens = re.split(r'[,\s]+', line)
        tokens = [t for t in tokens if t]
        if not tokens:
            continue
        opcode = tokens[0].upper()
        operands = tokens[1:]
        if opcode not in SUPPORTED_INSTRUCTIONS:
            errors.append(f"Error in line {i+1}: Unknown instruction {opcode}")
            continue
        instructions.append({'opcode': opcode, 'operands': operands})
    return instructions, errors