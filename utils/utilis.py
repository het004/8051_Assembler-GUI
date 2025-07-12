def hex_to_binary(hex_str, bits):
    return bin(int(hex_str, 16))[2:].zfill(bits)

def binary_to_hex(binary_str, bytes):
    hex_str = hex(int(binary_str, 2))[2:].upper()
    return hex_str.zfill(bytes * 2)

def add_8bit(a, b):
    int_a = int(a, 16)
    int_b = int(b, 16)
    sum_int = (int_a + int_b) & 0xFF
    return f'{sum_int:02X}'

def sub_8bit(a, b, carry):
    int_a = int(a, 16)
    int_b = int(b, 16)
    int_c = int(carry)
    diff_int = (int_a - int_b - int_c) & 0xFF
    return f'{diff_int:02X}'