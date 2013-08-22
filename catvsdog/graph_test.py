import sys

class Node(object):
	def __init__(self, _id, value1, value2):
		self._id = _id
		self.value1 = value1
		self.value2 = value2
		self.neighbors = set()

	def __str__(self):
		return "%s:value1=%s, value2=%s" % (self._id, self.value1, self.value2)

	def add_neighbor(self, node):
		self.neighbors.add(node)

	def get_neighbors(self):
		for neighbor in self.neighbors:
			print neighbor

class Graph(object):
	def __init__(self):
		self.nodes = []

	def add_edge(self, node1, node2):
		node1.add_neighbor(node2)
		node2.add_neighbor(node1)

	def add_node(self, node):
		self.nodes.append(node)

	def create(self):
		for i in range(len(self.nodes)):
			for j in range(i+1, len(self.nodes)):
				if self.nodes[i].value1 != self.nodes[j].value2 and \
				self.nodes[i].value2 != self.nodes[j].value1:
					self.add_edge(self.nodes[i], self.nodes[j])
		for node in self.nodes:
			print node._id, node.value1, node.value2
			node.get_neighbors()

def main():
	test_cases = int(sys.stdin.readline())
	for i in range(test_cases):
		first_line = sys.stdin.readline()
		first_line = first_line.split(' ', 2)
		first_line = map(int, first_line)
		cats, dogs, voters = first_line
# TODO: Verify cats, dogs, and voters
		votes = []
		for j in range(voters):
			votes.append(sys.stdin.readline())
		process_input(cats, dogs, votes)

def process_input(cats, dogs, votes):
	graph = Graph()
	node_id = 1
	for vote in votes:
		value1, value2 = vote.split(' ', 1)
		value2 = value2.rstrip()	# Hack to get rid of newline
		node = Node(node_id, value1, value2)
		node_id += 1
		graph.add_node(node)
	graph.create()

if __name__ == "__main__": main()