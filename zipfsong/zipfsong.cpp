/*	Zipf's song
	https://www.spotify.com/us/jobs/tech/zipfsong/

	Solution by Travis Pennetti	*/

#define MAX_SONG_PLAYS 				1000000000000
#define MAX_SONGS_ON_ALBUM 		5000
#define MAX_SONG_NAME_LENGTH 	30

#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

struct SONG
{
	std::string Name;
	unsigned int Plays;		// f_i
	unsigned int Number;	// i
	unsigned int Quality;	// f_i / z_i
};

bool CompareSongsByQuality(SONG song1, SONG song2);
std::vector<std::string> splitLine(std::string line, std::string delimeter);

int main(int argc, char **argv)
{
	std::vector<SONG> songs;
	std::vector<std::string> tokens(2);
	std::string inputLine, delimeter = " ";
	unsigned int numSongsOnAlbum, numSongsToSelect, numPlays, firstSongPlays;

	// Get and tokenize the input string
	std::getline(std::cin, inputLine);
	tokens = splitLine(inputLine, delimeter);

	std::stringstream(tokens[0]) >> numSongsOnAlbum;
	// Verify numSongsOnAlbum
	if (numSongsOnAlbum < 1 || numSongsOnAlbum > MAX_SONGS_ON_ALBUM)
		return 0;

	std::stringstream(tokens[1]) >> numSongsToSelect;
	// Verify numSongsToSelect
	if (numSongsToSelect < 1 || numSongsToSelect > numSongsOnAlbum)
		return -1;

	for (unsigned int i = 0; i < numSongsOnAlbum; i++)
	{
        SONG song = {0};

		// Get input from stdin
		std::getline(std::cin, inputLine);
		tokens = splitLine(inputLine, delimeter);

		std::stringstream(tokens[0]) >> numPlays;
		// Verify number of plays
		if (numPlays < 0 || numPlays > MAX_SONG_PLAYS)
			return -1;

		// Verify song name length
		if (tokens[1].length() > MAX_SONG_NAME_LENGTH)
			return -1;

		// Special case for first song, index is '0' which is false
		if (!(i))
			firstSongPlays = numPlays;

		// Populate song struct
		song.Name = tokens[1];	// Second token is song string name, unverified
		song.Plays = numPlays;
		song.Number = i + 1;	// Add one to get actual song index
		song.Quality = song.Plays * song.Number;

		songs.push_back(song);
	}

	// Sort songs by quality from highest to lowest
	std::stable_sort(songs.begin(), songs.end(), CompareSongsByQuality);

	// Print 'numSongsToSelect' from 'songs'
	for (unsigned int j = 0; j < numSongsToSelect; j++)
	{
		std::cout << songs[j].Name << '\n';
	}

	return 0;
}

bool CompareSongsByQuality(SONG song1, SONG song2)
{
	if (song1.Quality == song2.Quality)
		return song1.Number < song2.Number;
	return song1.Quality > song2.Quality;
}

std::vector<std::string> splitLine(std::string line, std::string delimeter)
{
	size_t pos;
	std::string token;
	std::vector<std::string> tokens(2);	// Only take two tokens

	// Tokenize string and store in 'tokens'
	token = line.substr(0, pos = (line.find(delimeter)));
	tokens[0] = token;
	token = line.substr(pos + delimeter.length(), line.length());
	tokens[1] = token;

	return tokens;
}