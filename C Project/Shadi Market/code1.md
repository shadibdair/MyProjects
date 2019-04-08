```
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
	int market = 0;
	int one = 1, two = 2, zero = 0, price = 0, sale = 0, total = 0;
	int cnt1 = 0, cnt2 = 0;
	printf("\t\tHello to Shadi Market :) \n");
	printf("press 5 To Start :\n");
	scanf_s("%d", &market);
	while (market != 0)
	{
		printf("\t\tEnter computer code: 1-stationary,2-laptop,0-EXIT\n");
		scanf_s("%d", &market);
		{
			if (market == one)
			{
				printf("Enter computer Price?\n");
				scanf_s("%d", &price);
				sale = price - (price*0.20);
				printf("After sales: %d\n", sale);
				cnt1++;
			}
			else
				if (market == two)
				{
					printf("Enter computer Price?\n");
					scanf_s("%d", &price);
					if (price >= 4000)
					{
						sale = price - (price*0.15);
						sale = sale - (sale * 0.10);
						printf("After sales: %d\n", sale);
						cnt2++;
					}
					else
					{
						sale = price - (price*0.15);
						printf("After sales: %d\n", sale);
						cnt2++;

					}

				}
				else
					if (market == 0)
					{
						break;
					}
			total += sale;
		}
	}
	printf("\t\t\ttotal Who Buy Stationary computer :%d\n", cnt1);
	printf("\t\t\ttotal Who Buy Notebook computer :%d\n", cnt2);
	printf("\t\t\ttotal comprare :%d", total);
	getchar();
	getchar();
}
```