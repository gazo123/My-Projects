#include<stdio.h>
struct _7segments{
        int a,b,c,d,e,f,g;
    };

void BCD_to_7segmentDecoder(int A,int B,int C,int D){
    struct _7segments s;
    
    if(A==0 && B==0 && C==0 && D==0){
        printf("0");                                            // 0
        s.a=1, s.b=1, s.c=1, s.d=1, s.e=1, s.f=1, s.g=0;    
    }
    else if(A==0 && B==0 && C==0 && D==1){
        printf("1");                                            // 1
        s.a=0, s.b=1, s.c=1, s.d=0, s.e=0, s.f=0, s.g=0;    
    }
    else if(A==0 && B==0 && C==1 && D==0){
        printf("2");
        s.a=1, s.b=1, s.c=0, s.d=1, s.e=1, s.f=0, s.g=1;        //2
    }
    else if(A==0 && B==0 && C==1 && D==1){
        printf("3");
        s.a=1, s.b=1, s.c=1, s.d=0, s.e=0, s.f=1, s.g=1;        //3
    }
    else if(A==0 && B==1 && C==0 && D==0){
        printf("4");
        s.a=0, s.b=1, s.c=1, s.d=0, s.e=0, s.f=1, s.g=1;        //4
    }
    else if(A==0 && B==1 && C==0 && D==1){
        printf("5");
        s.a=1, s.b=0, s.c=1, s.d=1, s.e=0, s.f=1, s.g=1;        //5
    }
    else if(A==0 && B==1 && C==1 && D==0){
        printf("6");
        s.a=1, s.b=0, s.c=1, s.d=1, s.e=1, s.f=1, s.g=1;        //6
    }
    else if(A==0 && B==1 && C==1 && D==1){
        printf("7");
        s.a=1, s.b=1, s.c=1, s.d=0, s.e=0, s.f=0, s.g=0;        //7
    }
    else if(A==1 && B==0 && C==0 && D==0){
        printf("8");
        s.a=1, s.b=1, s.c=1, s.d=1, s.e=1, s.f=1, s.g=1;        //8
    }
    else if(A==1 && B==0 && C==0 && D==1){
        printf("9");
        s.a=1, s.b=1, s.c=1, s.d=1, s.e=0, s.f=1, s.g=1;        //9
    }

    printf("\n%d %d %d %d %d %d %d ",s.a, s.b, s.c, s.d, s.e, s.f, s.g);

}

int main()
{
    int A,B,C,D;
    

    printf("Enter the BCD code in order of left to right(msb to lsb): "); //taking in BCD input from user;
    scanf("%d%d%d%d",&A,&B,&C,&D);
    printf("%d%d%d%d\n",A,B,C,D);

    BCD_to_7segmentDecoder(A,B,C,D);

 
    return 0;
}