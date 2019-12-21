import networkx as nx
import matplotlib.pyplot as plt
import time
import matplotlib.animation
import glob
import numpy as np
import imageio
import os

class Kruskal:
    def __init__(self, vertices, edges):
        self.a = []
        self.sets = []
        self.vertices = set(vertices)
        self.edges = edges

    def mst_kruskal(self):

        for vertic in self.vertices:
            self.sets.append(set(vertic))

        self.edges = sorted(self.edges, key=self.takeSecond)

        for edge in self.edges:
            set1 = set()
            set2 = set()
            for s in self.sets:
                if edge[0] in s:
                    set1 = set(s)
                if edge[1] in s:
                    set2 = set(s)
            if not (set1 & set2):
                self.a.append(edge)
                self.sets.append(set1 | set2)
                self.sets.remove(set1)
                self.sets.remove(set2)

        return self.a

    def takeSecond(self, elem):
        print(elem)
        return elem[2]

def show_graph( v, e):
    g = nx.Graph()
    for vertix in v:
        g.add_node(vertix)
    for edge in e:
        g.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(g)
    fig, ax = plt.subplots(figsize=(8, 5))
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    ax.set_title("your graph", fontweight="bold")
    plt.show()
    plt.savefig('/home/sun/Pictures/png/img{}.png'.format(0), dpi=120, bbox_inches='tight')
    k = Kruskal(v, e)
    ans = k.mst_kruskal()
    ans_vertices = []
    ans_edges = []
    for e in ans:
        if e[0] not in ans_vertices:
            ans_vertices.append(e[0])
        if e[1] not in ans_vertices:
            ans_vertices.append(e[1])
        ans_edges.append((e[0], e[1]))
    print(ans)
    nodes = []
    for i in range(0, len(ans)):
        time.sleep(2)
        nodes.append(ans[i][0])
        nodes.append(ans[i][1])
        # g.clear()
        ax.set_title("kruskal algorithm", fontweight="bold")
        nx.draw(g, pos=pos, nodelist=set(v) - set(nodes), with_labels=True)
        for j in range(0, i):
            nx.draw_networkx_edges(g, pos=pos, edgelist=[(ans_edges[j][0], ans_edges[j][1])],
                                   edge_color="yellow",
                                   with_labels=True)
        nx.draw_networkx_nodes(g, pos=pos, nodelist=nodes, node_color="red", with_labels=True)
        nx.draw_networkx_edges(g, pos=pos, edgelist=[(ans_edges[i][0], ans_edges[i][1])], edge_color="r",
                               with_labels=True)
        if i == len(ans) - 1:
            time.sleep(2)
            nx.draw_networkx_edges(g, pos=pos, edgelist=[(ans_edges[i][0], ans_edges[i][1])],
                                   edge_color="yellow",
                                   with_labels=True)
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        plt.show()
        # plt.savefig('pics/img{}.jpg'.format(i + 1), dpi=120, bbox_inches='tight')
        # plt.close()

        # filenames = glob.glob('pics' + 'img*.png')
        # filenames_sort_indices = np.argsort(
        #     [int(os.path.basename(filename).split('.')[0][3:]) for filename in filenames])
        # filenames = [filenames[i] for i in filenames_sort_indices]

        # make movie
        # with imageio.get_writer('pics/graph_animation.gif', mode='I', fps=1) as writer:
        #     for filename in filenames:
        #         image = imageio.imread(filename)
        #         writer.append_data(image)


