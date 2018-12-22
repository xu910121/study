.section .bss
    .lcomm buffer,1000
    .comm tes, 200
.section .text
.globl _start
#.globl $buffer
.globl $tes
_start:
    nop
