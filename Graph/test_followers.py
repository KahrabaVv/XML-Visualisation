from followers import SNA_Helper
from Graph_Converter import GraphOfUsers

path = "sample2.xml"
graph = GraphOfUsers(6, path)
sna = SNA_Helper()
tusers  = graph.vertices
ss = sna.getMutualFollowers(tusers[3],tusers[2])
sug = sna.suggestFollowers(tusers[4], graph)

mostInf = SNA_Helper().mostInfluencerUser(graph).name
mostAct = SNA_Helper().mostActiveUser(graph).name

print(mostInf)
print(mostAct)
print(SNA_Helper().post_search(graph, "test"))
