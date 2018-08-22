Programming Project 2: Shortest Paths in a Network


Program Design:
---------------------------------------------------------------------------------------------------------------------------------
Class HeapSort:
This class is used for creating priority queue and it follows min heap algorithm. In this class, i am trying to use both vertices 
and edge weight for having better control over the program flow.Two functions are designed for HeapSort apart from constructors

1. Insert:
This function takes two input, vertices list and total weight. Vertices list is nothing but the list of parent vertices required to
reach a particular vertices and total weight is the time taken to reach particular vertex. 
Steps:
* Add element to the list. 
* Compare the value to its parent. If the parent value is greater then swap the parent value with its child
* Repeat step 2 until conditions fail or it index reaches the root node.

2. Remove Min:
This function takes no argument and returns minimum element from the tree. 
Steps:
* Remove element in the index 0 and bring the last element in the list to index 0
* Compare the parent element with it child and swap the values if the child who has lower value compared to its parent and other child.
* repeat above step until conditions fail

Class Graph:
This class has information about the entire graph. All the vertices list are stored in the HashMap. HashMap contains key as vertices and 
value is the hashmap of edge objects. The Class object contain following functions

1. add_vertex
This function takes 3 arguments. First argument is name of parent vertex, child vertex and its weight. This function helps in adding vertices to the graph. Vertices are added to list if the vertics was not already listed in the Hashmap or
HashMpa list of edges are updated if the veriex is already present.

2. shortest_path:
This function takes 2 arguments as input. First argument contain Parent vertex and the second argument contain destination vertix.
Steps:
* Start the Dijkstra Algorithm with the parent vertex given in the argument. 
* Load the child verteces in the priority queue.
* Pop verteces and check whether the poped vertex is vertex 2. If not perform step above step considering popped vertex as parent vertex.
* print the path which is present list of vertices returned by the priority queue.

3. reachable
This displays all the vertices and edges which are reachable. BFS was implemented for performing reachable query. 
Steps:
* The vertices are sorted and vertices are read one by one.
* For each vertices read the list of vertices reachable from that vertices. Add the vertices list and add the vertex to the visited vertex list
* Fetch the vertices from the list and check whether the vertex is in listed list.
* Perform above step until it list is empty. 

Time Complexity : 

4. print_graph
This fuction will display all the vertices and edges along with weight.

Class Vertex
This function contains HashMap of Edge class objects to save edges. The functions used are
1. add_edge:
This fucntions add edges to the list of vertices.

2. check_edge:
This function is used for checking whether vertex is up or down

3. update_weight:
This function is used for updating weight for already created edge

Class Edge:
This function is for created edges.

1. update_weight:
This function is used for updating weight for already created weight

2. get_weight:
This function is used for getting updated wright for a given edge

Main Function:

This fucntion first reads network.txt and then reads given by the user one by one or through a text file and output are printed in 
the console or in a output file. 

Data Structure Design:
---------------------------------------------------------------------------------------------------------------------------------
Data Structure used are list and HashMap. List are used for saving visited vertices and HashMap is used for created graph with 
vertices and edges.

Breakdown of files:
---------------------------------------------------------------------------------------------------------------------------------
This program has single process.
1. Read network.txt file
2. Read queries one by one and print the result in the console.
3. If the query is quit, process stops.

Programming Language:
---------------------------------------------------------------------------------------------------------------------------------
Python.
Compiler Version  3.6.3

Instruction to run the program:
---------------------------------------------------------------------------------------------------------------------------------
program can be executed in 2 places. 
1. command "python Algos_project2.py network.txt < queries.txt > output.txt"

In this command, network are read from the txt file and querries are read from file instead of standrad input and output are writtened
in the output file instead of printing in the console. 

2. command is python Algos_project2.py network.txt

In this command, after network.txt program will prompt for input from user. The program will prompt input from user until quit is entered.

Summary of things on how should be given to the program:
---------------------------------------------------------------------------------------------------------------------------------
1. The vertexes name are sorted. Both capital and small letters are considered seperately. 
2. For path, total time is mentioned in 2 decimal places
3. Always, enter query a path that existis
4. Input query and output files should exists whiling entering command
5. Only query mentioned in the list should be given as input. 
6. Query should always end with quit commands
