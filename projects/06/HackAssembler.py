import re

comp = {'0': '0101010', '1': '0111111', '-1':'0111010', 'D':'0001100', 'A': '0110000', '!D': '0001101',
        '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111',
        'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D':'0000111',
        'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011',
        'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
        'D&M': '1000000', 'D|M': '1010101'}

dest = {"null": "000","M": "001","D": "010","A": "100",
        "DM": "011", "MD": "011", 
        "AM": "101", "MA": "101",
        "AD": "110", "DA": "110",
        "AMD": "111", "ADM": "111"}

jump = {"null": "000","JGT": "001","JEQ": "010",
        "JGE": "011","JLT": "100","JNE": "101",
        "JLE": "110","JMP": "111"}

symbolTable = {'R0':0, 'R1':1, 'R2':2, 'R3':3,
               'R4':4, 'R5':5, 'R6':6, 'R7':7,
               'R8':8, 'R9':9, 'R10':10, 'R11':11,
               'R12':12, 'R13':13, 'R14':14, 'R15':15, "SP": 0,
               "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
               "SCREEN": 16384, "KBD": 24576}

def first_pass(f):
    """Reads the program lines, one by one, focusing only on (label) declarations. 
       Adds the found labels to the symbol table"""
    
    n = 0 #start line numbers
    for line in f:
        pat = r'\(\w+\)' # find label declarations using regex
        m = re.findall(pat, line)
        
        if (line.startswith('//') or line==""):
            continue
        elif m: #add labels to symbol table. Don't count it (but give it count of next n)
            symbolTable[m[0].strip('()')] = n           
        else:
            n+=1 #increment line by 1




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
    last_added = 16 #last variable added to table

    first_pass(f) # run first pass to get numbers for labels
    
    def is_label(line):
        pat = r'\(\w+\)' # find label declarations using regex
        m = re.findall(pat, line)
        if m:
            return True
        return False
    
    # second pass
    for line in f:
        line = line.strip() # remove empty spaces that cause a bug for startswith()
        # remove comments from line
        pat2 = r'//.*'
        line = re.sub(pat2,'', line)
        line = line.strip()
        
        if (line.startswith('//') or line=="" or is_label(line)): # skip comments, empty lines and labels
            continue
        
        elif line.startswith('@'): # symbol or A instruction
            l = line[1:] # remove the @

            if l.isnumeric(): # this will be A instruction
                o = decToBin(int(l))

            else: # this is a symbol we need to handle
                #print(f'{line} : This is a Symbol')
                if l not in symbolTable:
                    symbolTable[l] = last_added
                    last_added += 1
                
                o = decToBin(symbolTable[l])

                    
        else: # C-inst: 3 cases: 1- dest=comp;jump 2- dest=comp 3- comp;jump
            #print(f'{line} : This is a C instruction')
            if ("=" in line and ";" in line):
                dst, cmp, jmp = mult_split(line)
            elif "=" in line:
                dst, cmp = mult_split(line)
                jmp = "null"
            else:
                cmp, jmp = mult_split(line)
                dst = "null"
            o = f'111{comp[cmp] + dest[dst] + jump[jmp]}'

        #print(f'{line} : {o}')
        out.write(o)
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


