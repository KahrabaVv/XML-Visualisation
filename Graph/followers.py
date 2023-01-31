from read_xml import graphUser, userPost
from Graph_Converter import GraphOfUsers

class SNA_Helper:
    def __int__(self):
        pass

    # function to get the mutual followers between 2 users
    @staticmethod
    def getMutualFollowers(user1:graphUser, user2:graphUser) -> list[graphUser]:
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
    def suggestFollowers(users:list[graphUser]) -> list[list[graphUser]]:
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


    # A function that returns the most influencer user in the network who has most followers
    @staticmethod
    def mostInfluencerUser(graph: GraphOfUsers) -> graphUser:
        users = graph.vertices
        most_influencer = users[0]
        for i in range(1, graph.numUsers):
            if len(graph.getUserFollowedList(users[i])) > len(graph.getUserFollowedList(most_influencer)) :
                most_influencer = users[i]

        return most_influencer


    # A function that returns the most active user in the network who is the most connected user to other users
    @staticmethod
    def mostActiveUser(graph: GraphOfUsers) -> graphUser:
        users = graph.vertices
        most_active = users[0]
        for i in range(1, graph.numUsers):
            if len(graph.getUserFollowerList(users[i])) + len(graph.getUserFollowedList(users[i])) > len(graph.getUserFollowerList(most_active)) + len(graph.getUserFollowedList(most_active)):
                most_active = users[i]

        return most_active
