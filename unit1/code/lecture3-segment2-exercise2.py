#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:59:49 2016

@author: ronaldo
"""

from lecture3Segment2 import Graph, Node, Edge

"""

  Vertices represent permutations of the students in line. 
  Edges connect two permutations if one can be made into the other
  by swapping two adjacent students.

"""

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB")))  # 0 <-> 1
g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC")))  # 0 <-> 2
g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))  # 1 <-> 4
g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))  # 2 <-> 3
g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))  # 3 <-> 5
g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA")))  # 4 <-> 5
