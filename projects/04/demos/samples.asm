// RAM[3] = RAM[3] - 15
@15
D=A // put the content of A (15) in D
@3 // select address 3 making M = RAM[3]
M=M-D // subtract the stored D (15) from RAM[3] 

// RAM[3] = RAM[4] + 1
@4 // select RAM[4]
D=M // store content of RAM[4] in D
@3 // select RAM[3] -> M
M=D+1 // put RAM[4] + 1 in it

// Alternative:  
// RAM[3] = RAM[4] + 1
@4 // select RAM[4] -> M
D=M+1 // Add content of RAM[4]/M + 1 and store in D
@3 // select RAM[3] -> M
M=D // put result above in it

// Compute: RAM[2] = RAM[0] + RAM[1] + 17
@17 // make A = 17
D=A // store 17 in D
@1 // select RAM[1] -> M
D=D+M // add it to D
@0 // same
D=D+M
@2 // put everything in RAM[2]
M=D

// if (D = 0) goto 300
//@0
//D=A
@300
D;JEQ

// if (RAM[3] < 100) goto 12
// RAM[3] < 100 iff RAM[3] - 100 < 0
@3
D=M
@100
D=D-A
@12
//D;JLT

// sum = 0
@sum
M=0

// Explained: @sum selects a memory address to bind to sum. Selected memory addressed go into M so we can set it

// x = 512
@512 
D=A
@x 
M=D

// n = n -1
@n
M=M-1

// sum = sum + x
@sum //sum selects arbitrary address with content M
D=M // save the content of sum in D
@x
D=D+M // add the content of x (in M) to the content of sum (stored in D)
@sum
M=D // set the new content of sum to the sum of old sum + x



