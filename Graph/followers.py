from read_xml import graphUser, userPost
from Graph_Converter import GraphOfUsers
import re
class SNA_Helper:
    def __int__(self):
        pass

    # function to get the mutual followers between 2 users
    @staticmethod
    def getMutualFollowers(user1:graphUser, user2:graphUser) -> list:
        mutualFollowers = []
        for follower in user1.followers:
            if follower in user2.followers:
                mutualFollowers.append(follower)
                pass
            pass
        return mutualFollowers
        pass


    # suggesting a list of users to follow for each user (the followers of his followers)
    @staticmethod
    def suggestFollowers(user:graphUser, graph: GraphOfUsers) -> list:
        suggestedFollowers = []
        for follower in user.followers:
            for followerFollower in graph.getUserFromId(follower).followers:
                if followerFollower not in user.followers and followerFollower != user.id and followerFollower not in suggestedFollowers:
                    suggestedFollowers.append(followerFollower)
                    pass
                pass
            pass
        return suggestedFollowers
        pass


    # A function that returns the most influencer user in the network who has most followers
    @staticmethod
    def mostInfluencerUser(graph: GraphOfUsers) -> graphUser:
        users = graph.vertices
        most_influencer = users[0]
        for i in range(1, graph.numUsers):
            if len(graph.getUserFollowerList(users[i])) > len(graph.getUserFollowerList(most_influencer)) :
                most_influencer = users[i]

        return most_influencer


    # A function that returns the most active user in the network who is the most connected user to other users
    @staticmethod
    def mostActiveUser(graph: GraphOfUsers) -> graphUser:
        users = graph.vertices
        most_active = users[0]
        for i in range(1, graph.numUsers):
            if len(graph.getUserFollowedList(users[i])) > len(graph.getUserFollowedList(most_active)):
                most_active = users[i]

        return most_active
    @staticmethod           
    def post_search(graph,string):
          users=graph.vertices
          numUsers=graph.numUsers
          Dict={}
          for i in range (0,numUsers):
                postsnum=len(users[i].posts)
                for post in range(0,postsnum):
                  result2=False
                  postbody=(users[i].posts[post].body)
                  topicbody=(users[i].posts[post].topics)
                  result=(re.search(string, postbody))
                  if string in topicbody:
                        result2=True      
                  if(result!=None or result2):
                            Dict [users[i].name]=users[i].posts[post].body
          if Dict == {}:
                return "The keyword didn't match any post or topic"                  

          return Dict
    
    visited = set() # Set to keep track of visited nodes of graph.

    def dfs(visited, graph, node):  #function for dfs 
        if node not in visited:
            print (node)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)

class Dictionary:  # I didn't use it when you say --> use hash mab normally without making implemention.

    def __init__(self):
            self.keys = []
            self.values = []

    def add(self, key, value):
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
            if key in self.keys:
                  return self.values[self.keys.index(key)]


                  


