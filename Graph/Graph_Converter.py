from read_xml import graphUser, userPost
NULL_EDGE = 0


class GraphOfUsers:
    def __init__(self,max:int, path:str) -> None:
        #lsit of users token from xml
        users:list[graphUser] = self.read_XML(path)
        #max number of users can graph contain
        self.max = max
        #number of existing users now in graph
        self.numUsers = 0
        #list of users
        self.vertices:list[graphUser] = [graphUser]*self.max
        #2d list of edges between users
        self.edges = [[0]*max for _ in range(max)]
        # list of boolean that tell if certain user visited or no
        self.marks = [False]*self.max
        #function that add list of user token from xml
        self.convertToGraph(users)
        pass

    #add list of user to graph
    def convertToGraph(self,users):
        startindex:int = self.numUsers
        for i in range(startindex,len(users)):
            self.addUser(users[i])
            pass
        for i in range(startindex,len(users)):
            currentUser:graphUser = users[i]
            for follower in currentUser.followers:
                self.addEdge(currentUser, self.getUserFromId(follower),1)
                pass
            pass
        pass

    # get certainly user from its ID
    def getUserFromId(self, id:int) -> graphUser:
        for i in range(0,self.numUsers):
            if self.vertices[i].id == id:
                return self.vertices[i]
            pass
        pass

    # add user to the graph
    def addUser(self, user:graphUser):
        self.vertices[self.numUsers] = user
        for i in range(0,self.numUsers+1):
            self.edges[self.numUsers][i] = NULL_EDGE
            self.edges[i][self.numUsers] = NULL_EDGE
            pass
        self.numUsers = self.numUsers +1
        pass

    # add edge from user to another
    def addEdge(self,fromUser: graphUser, toUser: graphUser, weight: int):

        self.edges[self.index(fromUser)][self.index(toUser)] = weight
        pass

    # get index of user in vertices list
    def index(self,user: graphUser) -> int:

        for i in range(0,self.numUsers+1):
            if self.vertices[i] == user:
                return i
            pass
        pass

    # get weight of edge between 2 vertex
    def weight(self,fromUser: graphUser, toUser: graphUser) -> int:
        row = self.index(fromUser)
        col = self.index(toUser)
        return self.edges[row][col]

    #check if this vertex visited in traversal or not
    def isMarked(self,user: graphUser) -> bool:
        return self.marks[self.index(user)]
    
    #mark vertex as visited in traversal or not
    def markUser(self,user: graphUser):
        self.marks[self.index(user)] = True
        pass

    #clear all marks after traversal
    def clearMarks(self):
        for i in range(0,self.numUsers):
            self.marks[i] = False
        pass

    #check if graph is full
    def isFull(self) -> bool:
        return self.numUsers == self.max
        pass
    
    #check if graph is empty
    def isEmpty(self) -> bool:
        return self.numUsers == 0
        pass

    # get user using its index in vertices list
    def getUserByIndex(self, index: int) -> graphUser:
        return self.vertices[index]

    #return list of users that followed by certain user
    def getUserFollowerList(self, user: graphUser)-> list[graphUser]:
        following = []
        for i in range(0,self.numUsers):
            if self.edges[self.index(user)][i] != 0:
                following.append(self.vertices[i])
                pass
            pass
        return following
        pass

    #return list of user whos followering certain user
    def getUserFollowedList (self, user: graphUser) -> list:
        followers = []
        for i in range (0,self.numUsers):
            if self.edges[i][self.index(user)] != 0:
                followers.append(self.vertices[i])
                pass
            pass
        return followers
        pass
    
    #Breadth First Traverse through the graph
    def BFT(self, start:graphUser):
        queueOfUser = []
        self.clearMarks()
        currentUser:graphUser
        queueOfUser.append(start)
        while queueOfUser:
            currentUser = queueOfUser.pop(0)
            if not self.isMarked(currentUser):
                #make function
                #
                #
                print(currentUser.name)
                self.markUser(currentUser)
                followers = self.getUserFollowerList(currentUser)
                for user in followers:
                    if not self.isMarked(user):
                        queueOfUser.append(user)
                        pass
                    pass
                pass
        pass


    @staticmethod
    def read_XML(path: str):
        file = open(path, 'r')

        comment = False
        userName = ""
        userID:int
        userFollowed = []
        userPosts = []
        postBody = ""
        postTopics = []
        tagValue:str = ""
        tagStack = []
        startValue:int
        endValue:int
        lines = ""
        users = []
        for line in file:
            lines += line.strip()
            pass

        for ind in range(0,len(lines)):
            if lines[ind] == '<' and not comment:
                #check if there is unclosed tag before
                if len(lines) > (ind + 3) and  lines[ind+1:ind+4] == '!--': 
                    comment = True
                    continue
                #clear tagName
                tagName = ""
                pass


            elif lines[ind] == '>':
                #check end of comment
                if ind > 3 and lines[ind-2:ind] == '--': 
                    comment = False
                    continue
                if comment: continue

                #end of openning tag
                if tagName[0] != '/':
                    startValue = ind+1
                    tagStack.append(tagName)

                #end of closing tag
                else:
                    #get the begin and end of value to use it in body, name, id, and topic tags  
                    endValue = ind - len(tagName)-1
                    tagValue = lines[startValue:endValue]
                    if tagStack[-1] == tagName[1:]: tagStack.pop()

                    if tagName == "/id":
                        if tagStack[-1] == "user":
                            userID = int(tagValue)
                        elif tagStack[-1] == "follower":
                            userFollowed.append(int(tagValue))
                    elif tagName == "/name":
                        userName = tagValue
                    elif tagName == "/body":
                        postBody = tagValue
                    elif tagName == "/topic":
                        postTopics.append(tagValue)
                    elif tagName == "/post":
                        userPosts.append(userPost(postBody,postTopics))
                        postTopics = []
                        postBody = ""
                    elif tagName == "/user":
                        users.append(graphUser(userID,userName,userPosts,userFollowed))
                        userPosts = []
                        userFollowed = []
                tagName = ""                
                
            # take the name of tag 
            else:
                if not comment:
                    tagName = tagName + lines[ind] 
            pass
        return users

    pass