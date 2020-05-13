import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        if avg_friendships >= num_users:
            return None

        # Add users
        for nu in range(num_users):
            self.add_user("User" + str(nu))

        # for user in self.users:
        #     print(user)

        total_cons = (num_users*avg_friendships)

        # Create friendships
        while total_cons > 0:
            if self.add_friendship(random.randint(1, num_users),
                                   random.randint(1, num_users)):
                total_cons -= 2

        # self.add_friendship(1, 2)

        total_len = 0
        for user in (self.users):
            total_len += len(self.friendships[user])
            print(user, self.friendships[user])
        print()
        # print(total_len)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # BFT - Breath First Traversal
        # because we want the shortest path

        q = deque()
        q.appendleft([user_id])

        while len(q) > 0:

            path = q.pop()
            v = path[-1]

            if v not in visited:
                # avoids pointing to it self
                if v != path[0]:
                    visited[v] = path
                for friend in self.friendships[v]:
                    q.appendleft(path + [friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print()
    print(connections)
