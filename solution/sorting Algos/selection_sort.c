#include <stdio.h>

void selection_sort(int arr[], int arrlen)
{
	int i, j, min_idx, temp, n;
	for (i = 0; i < arrlen - 1; i++)
	{
		min_idx = i;
		for (j = i + 1; j < arrlen; j++)
		{
			if (arr[j] < arr[min_idx])
			{
				min_idx = j;
			}
		}

		if (arr[min_idx] != arr[i])
		{
			temp = arr[min_idx];
			arr[min_idx] = arr[i];
			arr[i] = temp;
		}
	}

	printf("Sorted Array:\n");
	for (i = 0; i < arrlen; i++)
	{
		printf("%d\n", arr[i]);
	}
}
