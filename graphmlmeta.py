#!/usr/bin/env python
import networkx as nx
import sys

# Read the graph from a GraphML file
G = nx.read_graphml(sys.argv[1])

# Print information about the graph
# info is long gone as of NetworkX 3.3
#print(nx.info(G))

print("nodes:", G.number_of_nodes())
print("edges:", G.number_of_edges())
