""" Reversed Binary Numbers
    https://www.spotify.com/us/jobs/tech/reversed-binary/

    Solution by Travis Pennetti """

from sys import stdin as stdin  # stdin

def main():
  """Handle input from stdin"""
  for line in stdin:
    # Print out the base 2 int representation of the binary representation
    # the integer from the input.  [::-1] Indicates list traversal in
    # reverse.  [:-2] Indicates that after the binary represenation has
    # been reversed, do not print the '0b' string identifier.
    print int((bin(int(line))[::-1][:-2]), 2)

if __name__ == "__main__": main()