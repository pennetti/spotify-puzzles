/*	Reversed Binary Numbers
	https://www.spotify.com/us/jobs/tech/reversed-binary/

	Solution by Travis Pennetti	*/
	
#define BITS 	32

#include <string>
#include <bitset>
#include <sstream>
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	// Input number text
	std::string inputLine;
	// Count to remove trailing zeroes from reversed bitset
	unsigned int shiftCount;
	// Parsed input number
	unsigned int inputNumber;

	// Read input from stdin
	std::getline(std::cin, inputLine);
	std::stringstream(inputLine) >> inputNumber;	

	// Verify that number is in range
	if (inputNumber < 1 || inputNumber > 1000000000)
		return -1;

	// Create bitset for original 
	std::bitset<BITS> inputBits(inputNumber);
	// Bitset to hold reverse of 'inputBits'
	std::bitset<BITS> outputBits(0);

	for (unsigned int i = 0; i < BITS; i++)
	{
		// If the bit is set, then set the opposite bit in outputBits
		if (inputBits[i])
		{
			outputBits.set(BITS - 1 - i);
			// 'shiftCount' is the last '1' that appears in inputBits
			shiftCount = BITS - 1 - i;
		}
	}
	
	// Remove the trailing zeroes from the reversed number
	outputBits >>= shiftCount;

	std::cout << outputBits.to_ulong() << std::endl;

	return 0;
}