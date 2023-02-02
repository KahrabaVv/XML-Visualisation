import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
from Graph.Graph_Converter import GraphOfUsers

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
        for node in annot:
            annot[node].pos = (annot[node].get_position()[0] + 0.1, annot[node].get_position()[1] + 0.1)
            annot[node].set_fontsize(8)
            annot[node].set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7))
            annot[node].set_path_effects([patheffects.Stroke(linewidth=2, foreground='w'), patheffects.Normal()])

        plt.gca().get_yaxis().set_visible(False)
        plt.gca().get_xaxis().set_visible(False)
        plt.tight_layout()
        plt.show()

def visualizeGraph(path:str):
    graph = GraphOfUsers(5, path)
    G = GraphVisualization()
    for i in range(0, graph.numUsers):
        for user in graph.getUserFollowedList(graph.vertices[i]):
            G.addEdge("#" + str(user.id) + " " + user.name,
                      "#" + str(graph.vertices[i].id) + " " + graph.vertices[i].name)

        for user in graph.getUserFollowerList(graph.vertices[i]):
            G.addEdge("#" + str(graph.vertices[i].id) + " " + graph.vertices[i].name,
                      "#" + str(user.id) + " " + user.name)

    G.drawGraph()
