""" Cat vs. Dog
    https://www.spotify.com/us/jobs/tech/catvsdog/

    Maximum Clique Algorithm
    http://arxiv.org/pdf/1209.5818v4.pdf

    Solution by Travis Pennetti"""

import sys # stdin

class Node(object):
  """Node to hold vote values"""

  def __init__(self, _id, value_1, value_2):
    """_id is the vote number, value_1 is the up vote and value_2 is the down
    vote, neighbors is a set because enumeration is not important"""
    self._id        = _id
    self.value_1    = value_1
    self.value_2    = value_2
    self.neighbors  = set()

  def add_neighbor(self, node):
    """Add a neighbor to this node"""
    self.neighbors.add(node)

class Graph(object):
  """Collection of nodes, graph does not need to know edges in this case"""

  def __init__(self):
    """Use list because nodes will be enumerated when being connected"""
    self.nodes = []

  def add_edge(self, node_1, node_2):
    """Make 'edge' by creating bidirectional relationship between two nodes"""
    node_1.add_neighbor(node_2)
    node_2.add_neighbor(node_1)

  def add_node(self, node):
    """Add node to graph node list"""
    self.nodes.append(node)

  def create(self):
    """Connects the graph based on 'compatibility' between nodes.  Two nodes
    are said to be compatible if their up votes and down votes do no conflict"""
    for i in range(len(self.nodes)):
      for j in range(i+1, len(self.nodes)):
        if self.nodes[i].value_1 != self.nodes[j].value_2 and \
        self.nodes[i].value_2 != self.nodes[j].value_1:
          self.add_edge(self.nodes[i], self.nodes[j])

def main():
  """Handle input from sys.stdin"""
  test_cases = int(sys.stdin.readline())  # First line is number of test cases
  for i in range(test_cases):
    first_line = sys.stdin.readline().split(' ', 2)
    first_line = map(int, first_line)
    cats, dogs, voters = first_line   # First line of each test is c,d,v

    # Verify the number of cats, dogs, and voters fit the constraints
    if cats < 1 or cats > 1000 or \
    dogs < 1 or dogs > 1000 or \
    voters < 0 or voters > 500:
      return

    # Add all votes to a list to be processed
    votes = []
    for j in range(voters):
      votes.append(sys.stdin.readline())

    print find_max_clique(votes) # Process input

def find_max_clique(votes):
  """Create a graph from the given votes, nodes are connected if their votes
  do not conflict, then find the max clique size"""
  graph = Graph()
  node_id = 1   # Track node _id for enumeration
  for vote in votes:  # 'votes' is a set of strings
    value_1, value_2 = vote.split(' ', 1)
    value_2 = value_2.rstrip()  # Get rid of newline
    node = Node(node_id, value_1, value_2)
    node_id += 1
    graph.add_node(node)
  graph.create()  # Connect the graph
  return max_clique(graph)

def max_clique(graph):
  """Find the maximum clique by finding the largest clique containing each
  node and find the largest among them"""
  _max = 0
  for node in graph.nodes:
    if len(node.neighbors) >= _max: # Pruning, if the current node has fewer
                                    # neighbors than the max clique, it cannot
                                    # be part of a larger clique
      neighbor_list = []
      for neighbor in node.neighbors:
        if neighbor._id > node._id: # Don't repeat nodes already seen
          if len(neighbor.neighbors) > _max:  # Pruning, same as above
            neighbor_list.append(neighbor)
      _max = clique(graph, neighbor_list, _max, 1) # 1 is the smallest clique
  return _max

def clique(graph, neighbor_list, max_size, clique_size):
  """Recursive subroutine for max_clique, find the largest of all cliques
  containing a node in neighbor_list"""
  if len(neighbor_list) == 0: # Base case
    if clique_size > max_size:
      max_size = clique_size
    return max_size
  while len(neighbor_list) > 0:
    if (clique_size + len(neighbor_list)) <= max_size: #Pruning, if all nodes in
                                    # neighbor_list were added to the clique,
                                    # would it be bigger than the max found?
      return max_size

    # Remove a node from the neighbor list
    temp_node = neighbor_list[0]
    neighbor_list.remove(neighbor_list[0])

    # Pruning, all remaining nodes with neighbor lists larger than max and share
    # neighbors with the removed node
    new_neighbors = []
    for node in temp_node.neighbors:
      if node in temp_node.neighbors and \
      node in neighbor_list and \
      len(node.neighbors) >= max_size:
        new_neighbors.append(node)
    max_size = clique(graph, new_neighbors, max_size, clique_size+1)
  return max_size

if __name__ == "__main__": main()