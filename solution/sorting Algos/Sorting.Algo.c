/** Psuedocode for some sorting algo

Simple Sort

Array of values
loop: initialize i = 0 and loop condition i < array length - 1
    inner loop: initialize j = i + 1 loop condition j < array length
        if item at index j in array < item at index i in array
            swap item at j with item at i
        increment j by 1 and back to inner loop
    increment i by 1 and back to loop

to change from assending sort to descending sort, switch the comparison operator from > to <

Selection Sort

Array of values
loop: initialize i = 0 and loop condition i < array length - 1
    -inner loop through the array from i to the end to find index of the smallest item
    -swap item at index i with item at returned index
    increment i by 1 and back to loop

to change from assending to descending sort, change inner loop to find the index of the largest item


Bubble Sort
Array of values
loop: initalize i = 0 and loop condition i < array length - 1
    inner loop: initialize j = array length - 1 condition j > 0
        if array item at index j < array item at index k[j - 1]
            swap item at j with that at k[j - 1]
        decrement j by 1 and back to loop
    increment i by 1 and back to loop

to change from assending to sdescending sort, switch comparison in the if statement of the inner loop from < to >.
This sorting can also be created to sort bottom up instead of top to bottom.


Insertion Sort
Array of values
loop: initialize i = 1 and loop condition i < array length
    store value of array at i in a variable key
    variable to hold index j of i - 1
    inner loop: condition j >= 0 and item at j > key
        array[j + 1] = array[j]
        decrement j by 1
    array[j + 1] = key

To convert from ascending to descending order, make the comparison of j and key in the inner loop < instead of >


Merge Sort
We solve this recursively
function to split our arr
function arrsplit(array, start, end)
{
    if start
        == end return middle = start + end / 2 arrsplit(array, start, middle)
                                                 arrsplit(array, middle + 1, end)
                                                     combineArray(array, start, middle, end)
}

function combineArray(array, start, middle, end)
{
    create copy of array, arrCopy
                                      index holder i as start
                                          index holder j as middle +
                                  1 index counter k as start
                                      loop : condition i <=
                              middle and j <= end if arrCopy[i] <= arrCopy[j] array[k] = buffer[i] increment i by 1 else array[k] = buffer[j] increment j by 1 increment k by 1

                                                                                                                                    loop : condition i <= middle
                                                                                                                                                              array[k] = buffer[i] increment i by 1 increment k by 1

                                                                                                                                                                         loop : condition k <= end
                                                                                                                                                                                                   array[k] = buffer[i] increment i by 1 increment k by 1

                          delete copy to free memory
}

temp_n = temp->next;
temp_nn = temp_n->next;
curr_prev = current->prev;
temp->next = current;
current->prev = temp;
temp_n->prev = curr_prev;
curr_prev->next = temp_n;
temp_n->next = next;
next->prev = temp_n;
temp_nn->prev = current;
current->next = temp_nn;
**/