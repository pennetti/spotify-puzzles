/*	Reversed Binary Numbers
	https://www.spotify.com/us/jobs/tech/reversed-binary/

	Solution by Travis Pennetti	*/

#define BUFFER_SIZE 1024

#include <stdlib.h>
#include <stdio.h>

unsigned int reverseBits(unsigned int n);

int main(int argc, char **argv)
{
	char buffer[BUFFER_SIZE];
	unsigned int input;

	fgets(buffer, BUFFER_SIZE, stdin);

	input = atoi(buffer);

	// Verify input number is in range
	if (input < 1 || input > 1000000000)
		return -1;

	// Reverse binary
	input = reverseBits(input);

	printf("%d\n", input);

	return 0;
}

unsigned int reverseBits(unsigned int n)
{
	// Total bits is sum of 8 bits per byte
	unsigned int 	bitCount = sizeof(n) * 8;
	unsigned int 	reverseBits = 0, i = 0, maskBit = 1, shiftCount = 0;

	for (; i < bitCount; ++i)
	{
		// Get next bit
		maskBit = (n & 1);
		if (maskBit) // '1'
		{
			// Shift here because the remaining bits may all be '0'
			reverseBits <<= shiftCount;
			reverseBits |= maskBit;
			shiftCount = 1;
		} else {	// '0'
			shiftCount++;
		}
		n >>= 1;
	}

	return reverseBits;
}