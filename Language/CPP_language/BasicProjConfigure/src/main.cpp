#include <stdio.h>

int add(int a, int b);

int main(int argc,char* argv[])
{
    int count = 0;
    printf("The command line has %d arguments :\n", argc);
    for (count = 0; count < argc; ++count) {
        printf("%d: %s\n",count,argv[count]);
    }
    printf("call func: %d\n", add(5, 6));
    return 0;
}
