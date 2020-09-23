import networkx as nx
%matplotlib inline

import matplotlib.pyplot as plt

def displayinfo():
    x=input('enter the name of file with format')
    fb=nx.read_edgelist(str(x),create_using=nx.Graph(),nodetype=int)
    print(nx.info(fb))   
def displaygraph():
    x=input('enter the name of file with format')
    fb=nx.read_edgelist(str(x),create_using=nx.Graph(),nodetype=int)
    pos= nx.spring_layout(fb)
    plt.figure(figsize=(10,7))
    plt.axis('off')
    nx.draw_networkx(fb,pos=pos,with_label=False,node_size=35)
def getpropertiesofgraph():
    x=input('enter the name of file with format')
    fb=nx.read_edgelist(str(x),create_using=nx.Graph(),nodetype=int)
    print('Between for all the node of the graph')
    print(nx.betweenness_centrality(fb,normalized=True))
    print('degree for al the nodes of the graph')
    print(fb.degree())
    print('order')
    print(fb.order())
    print('size')
    print(fb.size())
    print('no of triangle in which this node exist')
    print(nx.triangles(fb)) #no 
    print('clustering coefficient of each node')
    print(nx.clustering(fb))
