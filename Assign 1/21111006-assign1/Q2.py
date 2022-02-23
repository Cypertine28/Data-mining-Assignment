import json
import numpy as np
import pandas as pd

f=open("neighbor-districts-modified.json")
dn=json.load(f)

with open("neighbor-districts-modified.json", "w") as outfile:
    json.dump(dn, outfile, indent = 2, sort_keys=True)
    outfile.close()
    
list1=[]
for i in dn:
    list1.append(i)

node = []
adj = []
for i in range(len(list1)):
    for j in range(len(dn[list1[i]])):
        node.append(list1[i])
        adj.append(dn[list1[i]][j])

edge_list = {'District': node, 'Neighbor District': adj}
edge_list = pd.DataFrame(edge_list)
edge_list.to_csv('edge-graph.csv',index=False)