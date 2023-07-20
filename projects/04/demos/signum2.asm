// Program: signum.asm
// Computes: if R0 > 0
//		R1 = 1
//	     else
//		R1 = 0

@R0
D=M // D = RAM[0]
@POS
D;JGT // If R0>0 goto POS

@R1 // else R0<=0
M=0 // R1=0
@END
0;JMP

(POS)
 @R1
 M=1 // R1=1

(END)
 @END
 0;JMP

