// Write a program that demonstrates for-loops such as:
// for (i=0; i<n; i++)
//	arr[i] = -1

// As we know, an array is just a pointer to the first cell in a block of memory 
// So we Set the first n entries of the memory block beginning in address base to –1

// Program: PointerDemo.asm
// Starting at the address stored in R0, 
// sets the first R1 words to –1
// Inputs: R0: base, R1: n


// Pseudocode:
// arr -> base address
// n -> length
// i -> 0
// Start Loop
//	Stop when i = n
//	Else
//        GoTo arr[base + i] 
//	  put -1 there
// 	  i++
//	  Go back to start of loop

// declare arr
@R0
D=M
@arr
M=D

// declare n
@R1
D=M
@n
M=D

// declare i
@i
M=0

(LOOP)
// Termination condition: if i = n, goto END
@i
D=M
@n
D=D-M
@END
D;JEQ

// Else go to RAM[arr+i] and set to -1
@arr
D=M
@i
A=D+M // this is the new capability we learn about. We can directly put addresses in register A and the selected register then becomes the new address we put
M=-1

// i++
@i
M=M+1

// back to start of loop
@LOOP
0;JMP

// Termination
(END)
@END
0;JMP


