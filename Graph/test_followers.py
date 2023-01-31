from followers import SNA_Helper
from Graph_Converter import GraphOfUsers

path = "sample2.xml"
graph = GraphOfUsers(6,path)
sna = SNA_Helper()
tusers  = graph.vertices

mostInf = sna.mostInfluencerUser(graph).name
mostAct = sna.mostActiveUser(graph).name

print(mostInf)
print(mostAct)

