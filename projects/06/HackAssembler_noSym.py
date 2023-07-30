import re

comp = {'0': '0101010', '1': '0111111', '-1':'0111010', 'D':'0001100', 'A': '0110000', '!D': '0001101',
        '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111',
        'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D':'0000111',
        'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011',
        'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
        'D&M': '1000000', 'D|M': '1010101'}

dest = {"null": "000","M": "001","D": "010","A": "100",
        "DM": "011","MD": "011", "AM": "101","AD": "110","AMD": "111", "ADM" : "111"}


jump = {"null": "000","JGT": "001","JEQ": "010",
        "JGE": "011","JLT": "100","JNE": "101",
        "JLE": "110","JMP": "111"}

def decToBin(n):
    "Converts decimal input n to its binary representation as 16-bit string"
    num = bin(n).replace("0b", "")
    nzeros = 16 - len(num) # how many zeros to fill on left
    zeros = nzeros*'0'
    return zeros + num

def mult_split(s):
    "Splits the C-instruction line at = and ; "
    delimiters = ["=",";"]
    for d in delimiters:
        s = " ".join(s.split(d))
    return s.split()


def compile(filename):
    f = open(filename, "r").read().splitlines() #input .asm file
    outname = filename.split('.')[0] + ".hack"
    out = open(outname, "w")

    for line in f:
        # skip comments and empty lines
        if (line.startswith('//') or line==""):
            continue
        else: #this is then an A or C instruction
            if line.startswith('@'):
                l = re.findall(r'\w+', line)
                out.write(decToBin(int(l[0])))
                out.write("\n")
            else: # C-inst: 3 cases: 1- dest=comp;jump 2- dest=comp 3- comp;jump
                if ("=" in line and ";" in line):
                    dst, cmp, jmp = mult_split(line)
                elif "=" in line:
                    dst, cmp = mult_split(line)
                    jmp = "null"
                else:
                    cmp, jmp = mult_split(line)
                    dst = "null"

                out.write(f'111{comp[cmp] + dest[dst] + jump[jmp]}')
                out.write("\n")
    out.close()



def main(args):
    # Usage: python HackAssembler Prog.asm
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' 'Prog.asm')
    filename = sys.argv[1]
    compile(filename)

if __name__ == '__main__':
    import sys
    main(sys.argv)


