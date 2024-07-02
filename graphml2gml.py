#!/usr/bin/env python
import networkx as nx
import sys
import re

# Read the graph from a GraphML file
G = nx.read_graphml(sys.argv[1])

(name,suffix) = re.split("\.", sys.argv[1])

nx.write_gml(G,name + ".gml")
