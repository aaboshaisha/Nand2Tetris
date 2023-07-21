// Write a program that draws a rectangle of height n (stored at R0) and width 16 that begins at upper left corner of the screen. 
// for (i=0; i<n; i++)
//	draw 16 pixels at beginning of row i

// addr = SCREEN //we begin at Screen corner. Put that in addr (address) variable since it will need to change
// n = RAM[0] get height from RAM[0]
// i = 0 (start of Loop)
// LOOP:
// 	if i > n goto END
//	RAM[addr] = -1 //1111111111111111 (-1 translates to 16 1s in binary). Setting a pixel to -1 makes it black
//	Advance to next row
//	addr = addr + 32 (remeber each row is 32 words)
//	i = i + 1
//	goto LOOP
// END:
// goto END

// Beginning of code

// declare addr = SCREEN
@SCREEN
D=A
@addr
M=D

// declare n
@R0
D=M
@n
M=D

// declare i
@i
M=0

// start loop
(LOOP)
// if i > n; goto END
@i
D=M
@n
D=D-M
@END
D;JGT

// set RAM[addr] = -1
@addr // addr's M contains SCREEN address
A=M // goto address M == SCREEN
M=-1

// advance to next row: addr = addr + 32
@addr
D=M
@32
D=D+A // addr = addr + 32
@addr
M=D

// i++
@i
M=M+1

// back to loop
@LOOP
0;JMP

(END)
@END
0;JMP
