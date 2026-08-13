# ============================================================
# FUNCTION 1: ADD AN EDGE
# ============================================================

def addEdge(adj, u, v, w):

    # adj is our adjacency list.
    #
    # u = starting vertex
    # v = ending vertex
    # w = weight/cost of the edge
    #
    # For example:
    # addEdge(adj, 1, 0, 4)
    #
    # means:
    # Connect vertex 1 and vertex 0
    # and give this connection a weight of 4.


    # Add vertex 'v' and its weight 'w'
    # to the list of vertex 'u'.
    #
    # So if we do:
    # addEdge(adj, 1, 0, 4)
    #
    # we put (0, 4) inside adj[1].

    adj[u].append((v, w))


    # Our graph is UNDIRECTED.
    #
    # That means we can travel in BOTH directions.
    #
    # If 1 is connected to 0,
    # then 0 is also connected to 1.
    #
    # Therefore, we also put (u, w)
    # inside the list of vertex v.

    adj[v].append((u, w))


# ============================================================
# FUNCTION 2: DISPLAY THE ADJACENCY LIST
# ============================================================

def displayAdjList(adj):

    # len(adj) tells us how many vertices we have.
    #
    # For example, if:
    # adj = [[], [], []]
    #
    # len(adj) = 3
    #
    # So range(3) gives:
    # 0, 1, 2

    for i in range(len(adj)):

        # Print the vertex number.
        #
        # end="" means:
        # "Don't go to the next line yet."
        #
        # So instead of:
        #
        # 0:
        #
        # we can continue printing the connections
        # on the same line.

        print(f"{i}: ", end="")


        # adj[i] contains all the vertices connected
        # to vertex i.
        #
        # For example:
        #
        # adj[0] = [(1, 4), (2, 1)]
        #
        # means vertex 0 is connected to:
        #
        # vertex 1 with weight 4
        # vertex 2 with weight 1

        for j in adj[i]:

            # j is a tuple containing two things:
            #
            # j[0] = connected vertex
            # j[1] = weight of the connection
            #
            # For example:
            #
            # j = (1, 4)
            #
            # j[0] = 1
            # j[1] = 4

            print(f"{{{j[0]}, {j[1]}}} ", end="")


        # After printing all connections of one vertex,
        # move to the next line.

        print()


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    # We are creating a graph with 3 vertices.
    #
    # The vertices will be:
    #
    # 0
    # 1
    # 2

    V = 3


    # Create an EMPTY adjacency list.
    #
    # We need one empty list for each vertex.
    #
    # Since V = 3:
    #
    # [[] for _ in range(V)]
    #
    # creates:
    #
    # [[], [], []]
    #
    # Think of it as:
    #
    # Vertex 0 -> has an empty box
    # Vertex 1 -> has an empty box
    # Vertex 2 -> has an empty box

    adj = [[] for _ in range(V)]


    # ========================================================
    # ADDING EDGES
    # ========================================================

    # Connect vertex 1 and vertex 0.
    #
    # Weight = 4
    #
    # So:
    #
    # 1 -------- 0
    #      4
    #
    # Because the graph is undirected,
    # this connection will be stored in BOTH places:
    #
    # adj[1] -> (0, 4)
    # adj[0] -> (1, 4)

    addEdge(adj, 1, 0, 4)


    # Connect vertex 1 and vertex 2.
    #
    # Weight = 3
    #
    # So:
    #
    # 1 -------- 2
    #      3
    #
    # Again, because the graph is undirected:
    #
    # adj[1] -> (2, 3)
    # adj[2] -> (1, 3)

    addEdge(adj, 1, 2, 3)


    # Connect vertex 2 and vertex 0.
    #
    # Weight = 1
    #
    # So:
    #
    # 2 -------- 0
    #      1
    #
    # This is also stored in both directions:
    #
    # adj[2] -> (0, 1)
    # adj[0] -> (2, 1)

    addEdge(adj, 2, 0, 1)


    # Print a heading before displaying our graph.

    print("Adjacency List Representation:")


    # Call our display function.
    #
    # This will print the graph
    # in adjacency-list form.

    displayAdjList(adj)


# ============================================================
# PROGRAM START
# ============================================================

# Python automatically stores the name of the current file
# in a special variable called __name__.
#
# When we directly run this file:
#
# __name__ == "__main__"
#
# Therefore, main() will be called.
#
# This basically means:
#
# "Start the program from main()."

if __name__ == "__main__":
    main()