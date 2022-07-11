#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* 목돈 예치 후 만기시 받는 금액 계산
Input: 예치액, 예치기간, 이자구분(단/복리), 이자율
Output: 소득에 대한 과세와 주민세 제외 금액 산출.

+예치금과 예치기간 이자 등의 변수에 적합한 자료형 결정후 이유 설명*/

float capital, tax_out; //원금, 세금
int out_money;          //원금+이자

int deposit()
{
    float inter_perc, inter; //이율, 이자
    int duration, interest;  //예치기간, 이자 구분(단/복리)

    printf("Capital of deposit?(won)\n:"); //예치금
    scanf("%f", &capital);
    printf("------------------\nInterest percent of deposit?(percent/year)\n:"); //이자율
    scanf("%f", &inter_perc);
    printf("------------------\nduration of deposit?(month)\n:"); //예치기간
    scanf("%d", &duration);
    printf("------------------\nsimple interest->1\ncompound interest->2\n:"); //이자구분
    scanf("%d", &interest);

    inter = inter_perc / 100 / 12; //월당 이율

    if (interest == 1) //단리 계산
    {
        out_money = capital + (capital * inter * duration);
    }
    else if (interest == 2) //복리 계산
    {
        out_money = capital * pow((1 + inter), duration);
    }
    else
    {
        printf("Wrong input\n");
    }
}

int tax()
{
    float inter_out;                  //원금 제외 이자
    inter_out = out_money - capital;  //원금 제외 이자(원금+이자-원금)
    tax_out = inter_out * 15.4 / 100; //세금(원금 제외 이자의 15.4%. 세금은 네이버 예금계산기 기준으로 적용)
}

int calculate()
{
    printf("------------------\nOutcome of deposit without tax is %d(won)\n", out_money); //세금제외 소득
    printf("Outcome of deposit with tax is %d(won)\n", out_money - (int)tax_out);         //세금포함 소득
    printf("Tax of the deposit is %d(won)\n", (int)tax_out);                              //세금
}

int main()
{
    deposit();
    tax();
    calculate();
}