""" Zipf's song
    https://www.spotify.com/us/jobs/tech/zipfsong/

    Solution by Travis Pennetti """

import sys

class Song(object):
  """Hold the name, number of plays, and track number"""

  def __init__(self, name, plays, number):
    """Name for identification, plays and number for quality calculation"""
    self.name   = name
    self.plays  = plays
    self.number = number

  def __str__(self):
    return str(self.name)

  def quality(self):
    """Quliaty calculation simplifies to plays * track number"""
    return self.plays * self.number

def main():
  """Handle input from stdin"""
  songs = []
  first_line = sys.stdin.readline().split(' ', 1)
  songs_on_album, songs_to_select = int(first_line[0]), int(first_line[1])
  for i in range(songs_on_album):
    line = sys.stdin.readline().split(' ', 1)
    song = Song(line[1], int(line[0]), i+1)
    songs.append(song)

  print_quality_songs(songs, songs_to_select)

def print_quality_songs(songs, songs_to_select):
  """Sort songs in ascending order of quality, print the number requested"""
  songs.sort(key=lambda song: -int(song.quality()))
  for i in range(songs_to_select):
    print songs[i]

if __name__ == "__main__": main()