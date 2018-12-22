# paramtest1.s - Listing command line parameters

.section .data
output1:
    .asciz "There are %d parameters:\n"
output2:
    .asciz "%s\n"
.section .text
.global _start

_start:
    nop
    movl (%esp), %ecx
    pushl %ecx
    push $output1
    call printf
    addl $4, %esp
    popl %ecx
    movl %esp, %ebp
    add $4, %ebp

loop1:
    pushl %ecx
    pushl (%ebp)
    pushl $output2
    call printf
    addl $8, %esp
    popl %ecx
    addl $4, %ebp
    loop loop1
    pushl $0
    call exit
