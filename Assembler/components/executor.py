from Instructions import arithmetic, logic, data_transfer, shift_rotate

def execute_instructions(instructions):
    for instr in instructions:
        opcode = instr['opcode']
        operands = instr['operands']
        if opcode in {'ADD', 'SUBB', 'INC', 'DEC'}:
            arithmetic.execute(opcode, operands)
        elif opcode in {'ANL', 'ORL', 'XRL', 'CPL'}:
            logic.execute(opcode, operands)
        elif opcode == 'MOV':
            data_transfer.execute(opcode, operands)
        elif opcode in {'RL', 'RR', 'RLC', 'RRC', 'SWAP'}:
            shift_rotate.execute(opcode, operands)