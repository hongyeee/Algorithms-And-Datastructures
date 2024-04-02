#include <iostream>
#include "QueType.h"
using namespace std;

#define QUEUE_SIZE 10
#define MAX_BIT 32

void radix_sort(int*);

int main()
{
	int data[] = {95, 672, 15068, 65, 984, 124, 5012, 13, 16, 4};
	radix_sort(data);
	return 0;
}

void radix_sort(int* data)
{
	QueType bucket_for_bit_0(QUEUE_SIZE);
	QueType bucket_for_bit_1(QUEUE_SIZE);
	
	int mask = 1;
	for (int i = 0; i < MAX_BIT; i++)
	{
		for (int j = 0; j < QUEUE_SIZE; j++)
		{
			int item = data[j] / mask % 2;
			if (item == 0)
				bucket_for_bit_0.Enqueue(data[j]);
			else
				bucket_for_bit_1.Enqueue(data[j]);
		};
		mask *= 2;

		int index = 0;
		int temp_item = 0;
		while (bucket_for_bit_0.IsEmpty() == 0)
		{	
			bucket_for_bit_0.Dequeue(temp_item);
			data[index] = temp_item;
			index++;
		}
		while (bucket_for_bit_1.IsEmpty() == 0)
		{
			bucket_for_bit_1.Dequeue(temp_item);
			data[index] = temp_item;
			index++;
		}
	}
}

