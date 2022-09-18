#include<stdio.h>
int convert_to_binary(int num)
{   int rem=0,binary=0,place=1;
    while(num!=0){
        rem=num%2;
        num=num/2;
        binary=binary+rem*place;
        place=place*10;
    }
    return binary;
}

int main()
{
int q=2,m=2,Q,M;

Q=convert_to_binary(q);
printf("binary of %d is %d",q,Q);



return 0;
}