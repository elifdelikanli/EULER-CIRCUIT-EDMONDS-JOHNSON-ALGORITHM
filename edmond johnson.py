# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:11:49 2022

@author: LENOVO
"""

#QUESTION 1#

def dfs(Edge, graph, visited_edge, path=[]):
    path = path + [Edge]             #.In the first part of the code, I add the current path + the corners to be added to the path.#

    for vertex in graph[Edge]:

        if visited_edge[Edge][vertex] == False:      #to only operate on impermeable edges, it looks at them false#
            visited_edge[Edge][vertex], visited_edge[vertex][Edge] = True, True   #In this section, under the condition of not passing, the newcomers are marked as true, that is, passed.#
            path = dfs(vertex, graph, visited_edge, path)



    return path




def Edmonds_Jhonson(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]   #Initially all visited vertices are set to false#
    start_node =5                   #Selecting the starting node#
    path = dfs(start_node, graph, visited_edge)     #Returning bfs algorithm to create Path I#

    for i in path:

        if (i == start_node):       #It shows how many different ways the initially selected node in the path is entered (n-1).#
                                       #So if there are 3 numbers, there are 2 different ways#
            print(i)

    print(path)





def main():                         #the graph created in the problem is defined#




    G1 = {
        1: [2, 6],
        2: [1, 3, 5, 8],
        3: [2, 4],
        4: [3, 5],
        5: [2, 6, 8],
        6: [1, 5, 7],
        7: [6, 8],
        8: [2, 5, 7],

    }



    max_node = 10       #Default number of nodes determined#

    Edmonds_Jhonson(G1, max_node)       #G1 graph and default Max mode number are sent to Edmond function 3

if __name__ == "__main__":              #Main function of the system#
    main()