import re
def post_search(graph,string):
      Dict={}
      users=graph.vertices
      numUsers=graph.numUsers
      for i in range (0,numUsers):
            postsnum=len(users[i].posts)
            for post in range(0,postsnum):
                  postbody=(users[i].posts[post].body)
                  result=(re.search(string, postbody))
                  if(result!=None):
                        Dict [users[i].name]=users[i].posts[post].body
      if Dict == {}:
            return "didn't match any post"                  

      return Dict
from Graph_Converter import GraphOfUsers
path = "E:\sample.xml"
graph = GraphOfUsers(5,path)
print (post_search(graph,"Lorem"))


                  

