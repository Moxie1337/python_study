#include<iostream>

#define N 10000
#define ADD(a, b) ((a) + (b));

int main()
{
    int c;

    c = ADD(1, 2);

    std::cout << N  << c << std::endl;

    #if M
     printf("N is defined");
    #endif

    return 0;
}