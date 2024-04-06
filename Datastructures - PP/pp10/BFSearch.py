from GraphType import *

def breadth_first_search(graph, startVertex, endVertex):
    queue = QueType()
    vertexQ = QueType()
    found = False

    
    '''[10]'''
    graph.clear_marks()
    queue.enqueue(startVertex)

    while True:
        vertex = queue.dequeue()
        if vertex == endVertex:
            print(vertex)
            found = True
        else:
            if not graph.is_marked(vertex):
                graph.mark_vertex(vertex)
                print(vertex)
                graph.get_to_vertices(vertex, vertexQ)

                while not vertexQ.is_empty():
                    item = vertexQ.dequeue()
                    if not graph.is_marked(item):
                        queue.enqueue(item)

        if not queue.is_empty() and not found:
            continue
        else:
            break

    if not found:
        print("Path not found")
