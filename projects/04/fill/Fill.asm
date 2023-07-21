// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


// set n = 8192
@8192
D=A
@n
M=D

// Check KBD 
(START)

// Re-Set i = 0
@i
M=0

// re-set addr = SCREEN
@SCREEN
D=A
@addr
M=D

// if scan-code = 0 (nothing pressed); goto WHITE
@KBD
D=M

@WHITE
D;JEQ

// if scan-code != 0 (any key pressed); goto BLACK
@BLACK
D;JNE

(WHITE)
// if i = n; goto START
@i
D=M
@n
D=D-M
@START
D;JEQ

// else: goto current addr and color it white
@addr
A=M
M=0

// addr = addr + 1
@addr
M=M+1

// i ++
@i
M=M+1

@WHITE
0;JMP

(BLACK)
// if i = n; goto START
@i
D=M
@n
D=D-M
@START
D;JEQ

// else: goto current addr and color it white
@addr
A=M
M=-1

// addr = addr + 1
@addr
M=M+1

// i ++
@i
M=M+1

@BLACK
0;JMP
