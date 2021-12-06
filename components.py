#!/usr/bin/env python3
import networkx as nx
import pandas as pd

#read the edge list
G = nx.read_edgelist('edge_list.txt')

#find the components of the graph
components = nx.connected_components(G)

#register id's in order of appearance in the components
indid = []

#register component size
sizes = []

for component in components:
    indid.extend(component)
    sizes.append(len(component))

#register famid's according to component size
famid = []

for i in range(len(sizes)):
    famid.extend([i+1]*sizes[i])

ids = pd.DataFrame({'famid':famid, 'indid':indid})

export_csv = ids.to_csv(r'ids.csv.gz', compression = 'gzip', sep=' ', index=None, header=True)
