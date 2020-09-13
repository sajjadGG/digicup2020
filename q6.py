from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import numpy as np
inf = 100000000
n = int(input())
l = list(map(int , input().split())) # plus one is the index
e = int(input())
m = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(e):
    q1 , q2 , c = tuple(map(int ,input().split()))
    m[q1][q2] = c
for i in range(n):
    if l[i]==1:
        m[0][i+1]=inf

graph = csr_matrix(m)

print(maximum_flow(graph, 0, l.index(2)+1).flow_value)
##connect all source with one source before them with edge capacity of infinte
#index zero is the base source
#source : 1 , node : 0  , sink : 2
