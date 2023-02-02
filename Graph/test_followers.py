from followers import SNA_Helper
from Graph_Converter import GraphOfUsers

path = "sample2.xml"
graph = GraphOfUsers(6,path)
sna = SNA_Helper()
tusers  = graph.vertices
ss = sna.getMutualFollowers(tusers[3],tusers[2])
sug = sna.suggestFollowers(tusers[4], graph)
mostInf = sna.mostInfluencerUser(graph).name
mostAct = sna.mostActiveUser(graph).name

print(mostInf)
print(mostAct)
print (sna.post_search(graph,"Lorem"))
