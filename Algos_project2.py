# Name: Sridhar Ramesh Babu
# ID: 801021040


import sys
import os
from decimal import Decimal
import fileinput
class HeapSort:
    def __init__(self):
        self.heap = []
        self.verteces = []
        self.last_index = 0
        pass


    def insert(self, new_name, new_val):
        self.heap.insert(self.last_index, new_val)
        self.verteces.insert(self.last_index, new_name)
        self.last_index += 1
        i = self.last_index
        while (i > 1):
            if (i <= 0):
                break
            else:
                if (self.heap[int((i)/2) - 1] <= self.heap[i - 1]):
                    break
                else:
                    temp = self.heap[i - 1]
                    temp_name = self.verteces[i - 1]
                    self.heap[i - 1] = self.heap[int(i/2 - 1)]
                    self.verteces[i - 1] = self.verteces[int(i / 2 - 1)]
                    self.heap[int(i/2) - 1] = temp
                    self.verteces[int(i / 2) - 1] = temp_name
                    i = int(i/2)

    def remove_min(self):
        if(len(self.heap) > 0 ):
            if(len(self.heap) == 1):
                self.last_index = self.last_index - 1
                return self.heap.pop(self.last_index) , self.verteces.pop(self.last_index)
            else:
                min_element = self.heap[0]
                min_name = self.verteces[0]
                self.heap[0] = self.heap.pop(self.last_index - 1)
                self.verteces[0] = self.verteces.pop(self.last_index - 1)
                self.last_index = self.last_index - 1
                i = 1
                min_ind = i
                while (i <= self.last_index):
                    if (((2 * i) <= self.last_index) and (self.heap[(2 * i) - 1] < self.heap[min_ind - 1])):
                        min_ind = 2 * i
                    if ((((i * 2) + 1) <= self.last_index) and (self.heap[i * 2] < self.heap[min_ind - 1])):
                        min_ind = (i * 2) + 1
                    if (min_ind != i):
                        temp = self.heap[i - 1]
                        temp_name = self.verteces[i - 1]
                        self.heap[i - 1] = self.heap[min_ind - 1]
                        self.verteces[i - 1] = self.verteces[min_ind - 1]
                        self.heap[min_ind - 1] = temp
                        self.verteces[min_ind - 1] = temp_name
                        i = min_ind
                    else:
                        break
                return min_element, min_name
        else:
            return None, None

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex1, vertex2, weight):
        if (vertex2 in self.vertices):
            pass
        else:
            cls_vertex2 = Vertex()
            self.vertices[vertex2] = cls_vertex2
        if(vertex1 in self.vertices):
            cls_vertex1 = self.vertices[vertex1]
            if cls_vertex1.check_edge(vertex2):
                cls_vertex1.update_weight(vertex2, weight)
            else:
                cls_vertex1.add_edges(vertex2, weight)
        else:
            cls_vertex1 = Vertex()
            cls_vertex1.add_edges(vertex2, weight)
            self.vertices[vertex1] = cls_vertex1
    def shortest_path(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            visited_vertex = {}
            total_time = 0
            visited_vertex[vertex1] = vertex1
            priority_queue = HeapSort()
            for edge in list(self.vertices[vertex1].edges.keys()):
                li = []
                li.append(vertex1)
                li.append(edge)
                if self.vertices[vertex1].edges[edge].edge_nature and self.vertices[edge].vertex_nature:
                    priority_queue.insert(li, float(self.vertices[vertex1].edges[edge].get_weight()))
            min_value, min_vertex = priority_queue.remove_min()
            while(min_vertex != None):
                if(min_vertex[len(min_vertex) - 1] == vertex2):
                    break
                elif (min_vertex[len(min_vertex) - 1] in visited_vertex):
                    pass
                else:
                    visited_vertex[min_vertex[len(min_vertex) - 1]] = min_vertex[len(min_vertex) - 1]
                    total_time = total_time + float(min_value)
                    vertex1 = min_vertex[len(min_vertex) - 1]
                    for edge in list(self.vertices[vertex1].edges.keys()):
                        if edge in visited_vertex:
                            pass
                        else:
                            if self.vertices[vertex1].edges[edge].edge_nature and self.vertices[edge].vertex_nature:
                                l = min_vertex[:]
                                l.append(edge)
                                priority_queue.insert(l, float(self.vertices[vertex1].edges[edge].get_weight()) + float(min_value))
                min_value, min_vertex = priority_queue.remove_min()
            if(len(visited_vertex) > 1):
                return min_vertex, min_value
            else:
                return None, None
        else:
            print("Tail Vertex is not in Graph")
            return None, None

    def reachable(self):
        k = list(self.vertices.keys())
        print_list = []
        for vertex in sorted(k):
            reachable_list = []
            vertex_reachable = []
            if self.vertices[vertex].vertex_nature:
                print(vertex)
                vertex_reachable.append(vertex)
                vertex1 = vertex
                # reachable_list.append(vertex)
                while (len(vertex_reachable) > 0):
                    vertex = vertex_reachable.pop(0)
                    e = list(self.vertices[vertex].edges.keys())
                    for edge in sorted(e):
                        if self.vertices[vertex].edges[edge].edge_nature and self.vertices[edge].vertex_nature:
                            if edge in reachable_list or edge == vertex1:
                                pass
                            else:
                                reachable_list.append(edge)
                                vertex_reachable.append(edge)
                for edge in sorted(reachable_list):
                    print("\t" + str(edge))
    def print_graph(self):
        k = list(self.vertices.keys())
        print_list = []
        for vertex in sorted(k):
            if self.vertices[vertex].vertex_nature:
                e = list(self.vertices[vertex].edges.keys())
                print(vertex)
                for edge in sorted(e):
                    if self.vertices[vertex].edges[edge].edge_nature:
                        print("\t" + str(edge) + " " + str(self.vertices[vertex].edges[edge].get_weight()))
                    else:
                        print("\t" + str(edge) + " " + str(self.vertices[vertex].edges[edge].get_weight()) + " DOWN")
            else:
                e = list(self.vertices[vertex].edges.keys())
                print(vertex + " DOWN")
                for edge in sorted(e):
                    if self.vertices[vertex].edges[edge].edge_nature:
                        print("\t" + str(edge) + " " + str(self.vertices[vertex].edges[edge].get_weight()))
                    else:
                        print("\t" + str(edge) + " " + str(self.vertices[vertex].edges[edge].get_weight()) + " DOWN")
class Vertex:
    def __init__(self):
        self.edges = {}
        self.vertex_nature = True

    def add_edges(self, edge_name, weight):
        edge = Edges(weight)
        self.edges[edge_name] = edge

    def check_edge(self, edge_name):
        if edge_name in self.edges:
            return True
        else:
            return False

    def update_weight(self, edge_name, new_weight):
        edge = self.edges[edge_name]
        edge.update_weight(new_weight)

class Edges:
    def __init__(self, weight):
        self.weight = weight
        self.edge_nature = True

    def update_weight(self, new_weight):
        self.weight = new_weight

    def get_weight(self):
        return self.weight

if __name__ == "__main__":
    network_lines = open(sys.argv[1])
    contents = network_lines.read()
    network_as_list = contents.splitlines()
    graph = Graph()
    for line in network_as_list:
        vertex1, vertex2, weight = line.split(" ")
        graph.add_vertex(vertex1, vertex2, weight)
        graph.add_vertex(vertex2, vertex1, weight)

    q = True
    while (q):
        print ()
        query = sys.stdin.readline()
        conditions = list(query.split())
        if (str(conditions[0]) == "print"):
            graph.print_graph()
        elif (str(conditions[0]) == "path"):
            paths, distance = graph.shortest_path(conditions[1], conditions[2])
            final_path = ""
            if paths != None:
                for path in paths:
                    print(path + " ", end='')
                x = Decimal(distance)
                print("%.2f" % distance)
        elif (str(conditions[0]) == "addedge"):
            graph.add_vertex(conditions[1], conditions[2], conditions[3])
        elif (str(conditions[0]) == "edgeup"):
            graph.vertices[conditions[1]].edges[conditions[2]].edge_nature = True
        elif (str(conditions[0]) == "edgedown"):
            graph.vertices[conditions[1]].edges[conditions[2]].edge_nature = False
        elif (str(conditions[0]) == "vertexdown"):
            graph.vertices[conditions[1]].vertex_nature = False
        elif (str(conditions[0]) == "reachable"):
            graph.reachable()
        elif (str(conditions[0]) == "vertexup"):
            graph.vertices[conditions[1]].vertex_nature = True
        elif (str(conditions[0]) == "deleteedge"):
            del graph.vertices[conditions[1]].edges[conditions[2]]
        elif (str(conditions[0]) == "quit"):
            q = False
        else:
            print("Give proper input")
