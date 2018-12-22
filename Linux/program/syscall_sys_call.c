#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <errno.h>

int main(int agrc, char *argv[])
{
    int rc;
    rc = syscall(SYS_chmod, "/test",0777);
    
    if (rc == -1)
        fprintf(stderr, "chmod failed, errno = %d\n", errno);
    else
    {
        printf("chmod success!\n");
    }
    return 0;
}
