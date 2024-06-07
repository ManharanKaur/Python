#String Formatting
def print_formatted(number):
    for decimal in range(1,number+1):
        octal = oct(decimal)[2:]
        hexa = hex(decimal)[2:]
        binary = bin(decimal)[2:]
        width = len(bin(number)[2:])
        print(str(decimal).rjust(width,' '), str(octal).rjust(width,' '), str(hexa).rjust(width,' ').upper(), str(binary).rjust(width,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)