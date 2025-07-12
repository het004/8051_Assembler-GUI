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
            continue
        tokens = re.split(r'[,;\s]+', line)  # Updated to handle commas and semicolons
        tokens = [t for t in tokens if t]
        if not tokens:
            continue
        opcode = tokens[0].upper()
        operands = tokens[1:]
        print(f"Parsed line {i+1}: opcode={opcode}, operands={operands}")  # Debug
        if opcode not in SUPPORTED_INSTRUCTIONS:
            errors.append(f"Error in line {i+1}: Unknown instruction {opcode}")
            continue
        if len(operands) != 2 and opcode in {'SUBB', 'ANL', 'ORL', 'XRL'}:
            errors.append(f"Error in line {i+1}: {opcode} requires exactly 2 operands")
            continue
        if len(operands) != 1 and opcode in {'CPL'}:
            errors.append(f"Error in line {i+1}: {opcode} requires exactly 1 operand")
            continue
        instructions.append({'opcode': opcode, 'operands': operands})
    return instructions, errors