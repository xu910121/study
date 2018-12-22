#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <stdio.h>

int main(int agrc, char *argv[])
{
    int rc;

    rc = chmod("/test",0444);
    if (rc == -1)
    {
        fprintf(stderr, "chmod failed, errno = %d\n",errno);
    }
    else
    {
        printf("chmod success!\n");
    }
    return 0;
}
