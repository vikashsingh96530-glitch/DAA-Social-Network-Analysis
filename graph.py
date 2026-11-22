
import networkx as nx

G = nx.Graph()

def add_user(name):
    G.add_node(name)

def add_friend(user1, user2):
    if user1 in G and user2 in G:
        G.add_edge(user1, user2)

def bfs(start):
    return list(nx.bfs_tree(G, start).nodes())

def dfs(start):
    return list(nx.dfs_preorder_nodes(G, start))

def shortest_path(user1, user2):
    try:
        return nx.shortest_path(G, user1, user2)
    except nx.NetworkXNoPath:
        return None

def mutual_friends(user1, user2):
    return list(nx.common_neighbors(G, user1, user2))
