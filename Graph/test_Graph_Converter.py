from Graph_Converter import GraphOfUsers
path = "Graph\sample.xml"
graph = GraphOfUsers(5,path)
followed = graph.getUserFollowedList(graph.getUserFromId(1))
followers = graph.getUserFollowerList(graph.getUserFromId(1))
graph.BFT(graph.getUserFromId(5))
print("Finish !")