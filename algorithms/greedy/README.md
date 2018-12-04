Welsh Powell Algorithm
=======================

The Welsh Powell Algorithm is a suitable algortihm for the four-colour problem, which is comparable to the Radio Russia Problem.
The Welsh Powell Algorithm is a greedy algorithm that lists all the nodes based on hwo many nodes they are connected with.
The algorithm is based on the following steps:

1. Find the valence of each vertex (number of edges that are meeting at that vertex)
2. List the vertices in order of descending valence (you can break ties any way you wish)
3. Color the vertex in the list (the vertex with the highest valence) with color 1
4. Go down the list and color every vertex not connected to the colored vertices above the same colour. Then cross out alle coloured vertices in the list
5. Repeat the process on the uncoloured vertices with a new colour - always working in descending order of valence until all vertices have been coloured
(http://mrsleblancsmath.pbworks.com/w/file/fetch/46119304/vertex%20coloring%20algorithm.pdf)
