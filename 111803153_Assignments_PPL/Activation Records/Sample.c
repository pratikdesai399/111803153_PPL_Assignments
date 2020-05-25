void fun1(int a, int b)
{
    int x, y;

    x = 555;
    y = a+b;
}

void fun2(void) {
    bar(111,222);
}

// Compile this program using    gcc -S  -m32 Sample.c

/*
Assembly code for te above functions:

fun1:        # --------- start of the function bar()
    pushl   %ebp        # save the incoming frame pointer
    movl    %esp, %ebp  # set the frame pointer to the current top of stack
    subl    $16, %esp   # increase the stack by 16 bytes (stacks grow down)
    movl    $555, -4(%ebp)  # x=555 a is located at [ebp-4]
    movl    12(%ebp), %eax  # 12(%ebp) is [ebp+12], which is the second parameter
    movl    8(%ebp), %edx   # 8(%ebp) is [ebo+8], which is the first parameter
    addl    %edx, %eax  # add them
    movl    %eax, -8(%ebp)  # store the result in y
    leave           #
    ret         #
fun2:        # --------- start of the function foo()
    pushl   %ebp        # save the current frame pointer
    movl    %esp, %ebp  # set the frame pointer to the current top of the stack
    subl    $8, %esp    # increase the stack by 8 bytes (stacks grow down)
    movl    $222, 4(%esp)   # this is effectively pushing 222 on the stack
    movl    $111, (%esp)    # this is effectively pushing 111 on the stack
    call    bar     # call = push the instruction pointer on the stack and branch to foo
    leave           # done
    ret         #

*/