from kruskal import show_graph


v = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
e = [('a', 'b', 4), ('a', 'c', 8), ('b', 'c', 11), ('c', 'd', 7), ('c', 'f', 1), ('f', 'd', 6),
     ('f', 'g', 2), ('g', 'e', 4), ('g', 'i', 10), ('g', 'h', 14), ('h', 'e', 7),
     ('e', 'd', 2), ('e', 'b', 8), ('h', 'i', 9)]
show_graph(v,e)