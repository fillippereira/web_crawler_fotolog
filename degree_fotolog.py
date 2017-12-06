import csv
import networkx as nx
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

print('A)Fotolog é um site de fotografias, onde seus usuários podem mandar todas suas fotografias \n'+
'e compartilhar com os amigos.Com o tempo, foi perdendo espaço para outras redes sociais,\n'+
'especialmente Facebook e Instagram.')


G = nx.read_edgelist('/home/fgpereira/Área de Trabalho/user_fotolog.csv', delimiter=',', nodetype=str)
G.edges()
#pos=nx.fruchterman_reingold_layout(G)
#plt.axis('off')
#nx.draw_networkx_nodes(G,pos,node_size=50) #plota os nodes
#nx.draw_networkx_edges(G,pos,alpha=0.4)
#plt.title('Usuarios x Grupos', size=16)
#plt.show()
numerador = 0
denominador = 0

with open('degrees.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():

        writeit.writerow([str(node)] + [G.degree(node)])
        numerador += G.degree(node)
        denominador += 1

avgGrau = numerador/denominador
print('\nB)A média do grau dos nodos é:'+str(avgGrau))

deg = nx.degree(G)
clu = nx.clustering(G)

print('\nC)O cluster coefficient é: '+str(nx.clustering(G)))
plt.figure(1, figsize=(12, 8))
pos=nx.fruchterman_reingold_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G,pos,node_size=clu)
nx.draw_networkx_edges(G,pos,alpha=0.4)
plt.title('Egonet - Neylson\nTamanho = Degree', size=16)
plt.show()



print('\nD)A distancia média dos nodos é: '+str(nx.average_shortest_path_length(G)))

#betweenness

bet = nx.betweenness_centrality(G, normalized=False)
bet.values()
print('\nE)O betwennes dos nodos e arestas é: '+str(bet))



