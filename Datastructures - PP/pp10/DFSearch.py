from GraphType import *

def depth_first_search(graph, startVertex, endVertex):
    stack = StackType()
    vertexQ = QueType()
    found = False

    '''[9]'''
    graph.clear_marks()
    stack.push(startVertex)
    
    while True:
        vertex = stack.top()
        stack.pop()
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
                        stack.push(item)
        
        if not stack.is_empty() and not found:
            continue
        else:
            break
    
    if not found:
        print("Path not found")