from state import FLAGS
from utils import hex_to_binary

def set_flags_after_add(a, b, result):
    int_a = int(a, 16)
    int_b = int(b, 16)
    sum_int = int_a + int_b
    carry_out = '1' if sum_int > 0xFF else '0'
    carry_bit3 = '1' if (int_a & 0x0F) + (int_b & 0x0F) > 0x0F else '0'
    sign_a = (int_a & 0x80) >> 7
    sign_b = (int_b & 0x80) >> 7
    sign_result = (sum_int & 0x80) >> 7
    overflow = '1' if (sign_a == sign_b and sign_a != sign_result) else '0'
    parity = '1' if bin(sum_int & 0xFF).count('1') % 2 == 0 else '0'
    FLAGS['CY'] = carry_out
    FLAGS['AC'] = carry_bit3
    FLAGS['OV'] = overflow
    FLAGS['P'] = parity

def set_flags_after_subb(a, b, result, carry_in):
    int_a = int(a, 16)
    int_b = int(b, 16)
    int_c = int(carry_in)
    diff_int = int_a - int_b - int_c
    carry_out = '1' if diff_int < 0 else '0'
    carry_bit3 = '1' if (int_a & 0x0F) - (int_b & 0x0F) - int_c < 0 else '0'
    sign_a = (int_a & 0x80) >> 7
    sign_b = (int_b & 0x80) >> 7
    sign_result = (diff_int & 0x80) >> 7
    overflow = '1' if (sign_a != sign_b and sign_a != sign_result) else '0'
    parity = '1' if bin(diff_int & 0xFF).count('1') % 2 == 0 else '0'
    FLAGS['CY'] = carry_out
    FLAGS['AC'] = carry_bit3
    FLAGS['OV'] = overflow
    FLAGS['P'] = parity