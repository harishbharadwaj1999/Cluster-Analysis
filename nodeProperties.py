import networkx as nx
%matplotlib inline
import matplotlib.pyplot as plt

def getnodeproperty():
    x=input('enter the name of file with format\t')
    fb=nx.read_edgelist(str(x),create_using=nx.Graph(),nodetype=int)
    y=int(input('enter the node\t'))
    print('degree of ',y,'\n')
    list(fb.neighbors(y))
    print(fb.degree(y))
    print('neighbours of ',y,'\n',end='')
    for i in list(fb.neighbors(y)):
        print(i,' ',end='') 
    print('\n')
    print('clustering of',y,'\n',end='')
    a=nx.clustering(fb)
    print(a[y])
    
    print('degree centrality of',y,'\n',end='')
    a=nx.degree_centrality(fb)
    print(a[y])
    print('betweeness centrality of',y,'\n',end='')
    b=nx.betweenness_centrality(fb,normalized=True)
    print(b[y])
    print('eigen vector centrality of',y,'\n',end='')
    e = nx.eigenvector_centrality(fb)
    print(e[y])
