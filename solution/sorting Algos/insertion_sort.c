#include <stdio.h>

void insertion_sort(int arr[], int arrlen)
{
    // array[] = {2, 1, 5, 9, 3, 7, 4, 20 };
    int i, j, key;

    for (i = 1; i < arrlen; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = key;
    }

    printf("Sorted Array:\n");
    for (i = 0; i < arrlen; i++)
    {
        printf("%d\n", arr[i]);
    }
}

int main()
{
    int array[] = {2, 1, 5, 9, 3, 7, 4, 20};
    int len = 8;
    insertion_sort(array, len);
}
