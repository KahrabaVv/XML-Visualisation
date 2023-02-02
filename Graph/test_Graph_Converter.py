from Graph_Converter import GraphOfUsers
path = "sample.xml"
graph = GraphOfUsers(5,path)
followed = graph.getUserFollowedList(graph.getUserFromId(1))
followers = graph.getUserFollowerList(graph.getUserFromId(1))
# graph.BFT(graph.getUserFromId(5))
for i in range (0,graph.numUsers):
    print(graph.vertices[i].name)
    print("Followed by:")
    for user in graph.getUserFollowedList(graph.vertices[i]):
        print(user.name + " " + str(user.id))
    print("Follows:")
    for user in graph.getUserFollowerList(graph.vertices[i]):
        print(user.name + " " + str(user.id))
    print("")


print("Finish !")