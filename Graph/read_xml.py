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
    pass