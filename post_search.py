import re
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


                  

