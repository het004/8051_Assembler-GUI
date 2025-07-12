from Instructions.arithmetic import execute as arithmetic_execute
from Instructions.logic import execute as logic_execute
from Instructions.data_transfer import execute as data_transfer_execute
from Instructions.shift_rotate import execute as shift_rotate_execute

def execute_instructions(instructions):
    print(f"Executing instructions: {instructions}")  
    for instr in instructions:
        print(f"Processing: {instr['opcode']} {instr['operands']}")  
        opcode = instr['opcode']
        operands = instr['operands']
        if opcode in {'ADD', 'SUBB', 'INC', 'DEC'}:
            print(f"Calling arithmetic_execute for {opcode}")  
            arithmetic_execute(opcode, operands)
        elif opcode in {'ANL', 'ORL', 'XRL', 'CPL'}:
            logic_execute(opcode, operands)
        elif opcode == 'MOV':
            data_transfer_execute(opcode, operands)
        elif opcode in {'RL', 'RR', 'RLC', 'RRC', 'SWAP'}:
            shift_rotate_execute(opcode, operands)