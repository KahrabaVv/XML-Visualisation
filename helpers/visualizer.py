import networkx as nx
import matplotlib.pyplot as plt
from helpers.graph import GraphOfUsers


class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, fromUser, toUser):
        self.visual.append((fromUser, toUser))

    def drawGraph(self):
        plt.title("Graph of Users")
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = nx.spring_layout(G)
        nx.draw_networkx_edges(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        annot = nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()})

        plt.gca().get_yaxis().set_visible(False)
        plt.gca().get_xaxis().set_visible(False)
        plt.tight_layout()
        plt.show()


@staticmethod
def visualizeGraph(graph: GraphOfUsers):
    G = GraphVisualization()
    # G.visual = []
    edges = graph.edges
    print("Edges: " + str(edges))
    for i in range(0, graph.numUsers):
        for j in range(0, graph.numUsers):
            if edges[i][j] != 0:
                G.addEdge("#" + str(graph.vertices[i].id) + " " + graph.vertices[i].name,
                          "#" + str(graph.vertices[j].id) + " " + graph.vertices[j].name)

    G.drawGraph()
