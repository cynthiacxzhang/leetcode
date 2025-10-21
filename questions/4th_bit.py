# Find the 4th bit of a decimal number

def find_4th_bit(n):

    bin_num = bin(n)  # convert to binary
    bin_num = bin_num[2:]  # remove '0b' prefix

    return int(bin_num[-4]) if len(bin_num) >= 4 else 0

