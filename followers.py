from Graph.read_xml import read_XML, graphUser, userPost

# function to get the mutual followers between 2 users
def getMutualFollowers(user1:graphUser, user2:graphUser) -> list[int]:
    mutualFollowers = []
    for follower in user1.followers:
        if follower in user2.followers:
            mutualFollowers.append(follower)
            pass
        pass
    return mutualFollowers
    pass

# suggesting a list of users to follow for each user (the followers of his followers)
def suggestFollowers(users:list[graphUser]) -> list[list[int]]:
    suggestions = []
    for user in users:
        suggestedFollowers = []
        for follower in user.followers:
            for followerFollower in users[follower].followers:
                if followerFollower not in user.followers and followerFollower != user.id:
                    suggestedFollowers.append(followerFollower)
                    pass
                pass
            pass
        suggestions.append(suggestedFollowers)
        pass
    return suggestions
    pass

