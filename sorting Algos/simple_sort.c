#include <stdio.h>

void simple_sort(int arr[], int arrlen)
{
	int i, j, temp;

	for (i = 0; i < arrlen - 1; i++)
	{
		for (j = i + 1; j < arrlen; j++)
		{
			if (arr[j] < arr[i])
			{
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
	}

	printf("Sorted Array:\n");
	for (i = 0; i < arrlen; i++)
	{
		printf("%d\n", arr[i]);
	}
}

int main()
{
	int array[] = {2, 5, 1, 9, 3, 7, 4, 20};
	int len = 8;
	simple_sort(array, len);
}