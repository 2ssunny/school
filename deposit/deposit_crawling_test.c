#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* �� ��ġ �� ����� �޴� �ݾ� ���
Input: ��ġ��, ��ġ�Ⱓ, ���ڱ���(��/����), ������
Output: �ҵ濡 ���� ������ �ֹμ� ���� �ݾ� ����.

+��ġ�ݰ� ��ġ�Ⱓ ���� ���� ������ ������ �ڷ��� ������ ���� ����*/

float capital, tax_out; //����, ����
int out_money;          //����+����

int deposit()
{
    float inter_perc, inter; //����, ����
    int duration, interest;  //��ġ�Ⱓ, ���� ����(��/����)

    printf("Capital of deposit?(won)\n:"); //��ġ��
    scanf("%f", &capital);
    printf("------------------\nInterest percent of deposit?(percent/year)\n:"); //������
    scanf("%f", &inter_perc);
    printf("------------------\nduration of deposit?(month)\n:"); //��ġ�Ⱓ
    scanf("%d", &duration);
    printf("------------------\nsimple interest->1\ncompound interest->2\n:"); //���ڱ���
    scanf("%d", &interest);

    inter = inter_perc / 100 / 12; //���� ����

    if (interest == 1) //�ܸ� ���
    {
        out_money = capital + (capital * inter * duration);
    }
    else if (interest == 2) //���� ���
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
    float inter_out;                  //���� ���� ����
    inter_out = out_money - capital;  //���� ���� ����(����+����-����)
    tax_out = inter_out * 15.4 / 100; //����(���� ���� ������ 15.4%. ������ ���̹� ���ݰ��� �������� ����)
}

int calculate()
{
    printf("------------------\nOutcome of deposit without tax is %d(won)\n", out_money); //�������� �ҵ�
    printf("Outcome of deposit with tax is %d(won)\n", out_money - (int)tax_out);         //�������� �ҵ�
    printf("Tax of the deposit is %d(won)\n", (int)tax_out);                              //����
}

int main()
{
    deposit();
    tax();
    calculate();
}