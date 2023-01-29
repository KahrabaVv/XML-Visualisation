class graphUser:
    def __init__(self,id,name,posts,followers) -> None:
        self.id:int = id
        self.name:str = name
        self.posts = posts
        self.followers = followers
        pass
    pass

class userPost:
    def __init__(self,body:str,topics:list) -> None:
        self.body = body
        self.topics = topics
        pass

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