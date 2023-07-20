// Program: Sum1ToN (R0 represents N)
// Computes R1 = 1 + 2 + 3 + .... + R0
// Usage: put a value >=1 in R0

// if R0 <= 0 goto END
(START)
@R0
D=M
@END
D;JLE

@R1
M=M+D // R1 = R1 + R0
@R0
M=M-1// R0 = R0 - 1
@START// back to first step
0;JMP

(END)
@END
0;JMP
