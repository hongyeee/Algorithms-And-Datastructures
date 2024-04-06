from QueType import *
from StackType import *

NULL_EDGE = 0

def index_is(vertices, vertex):
    index = 0

    while index < len(vertices) and vertex != vertices[index]:
        index += 1

    if not index < len(vertices):
        return -1
    else:
        return index

class GraphType:
    def __init__(self, maxV=50):
        self.numVertices = 0
        self.maxVertices = maxV
        self.vertices = [None] * maxV
        self.edges = [[NULL_EDGE] * maxV for _ in range(maxV)]
        self.marks = [None] * maxV

    def add_vertex(self, vertex):
        '''[1]'''
        self.vertices[self.numVertices] = vertex
        for i in range(0,self.numVertices):
            self.edges[self.numVertices][i] = NULL_EDGE
            self.edges[i][self.numVertices] = NULL_EDGE
        self.numVertices += 1

    def add_edge(self, fromVertex, toVertex, weight):
        '''[2]'''
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        self.edges[row][col] = weight


    def weight_is(self, fromVertex, toVertex):
        '''[3]'''
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        return self.edges[row][col]


    def get_to_vertices(self, vertex, adjVertices):
        '''[4]'''
        fromIndex = index_is(self.vertices, vertex)
        for i in range(0, self.numVertices):
            if self.edges[fromIndex][i] != NULL_EDGE:
                adjVertices.enqueue(self.vertices[i])


    def clear_marks(self):
        '''[5]'''
        self.marks = [None] * self.maxVertices


    def is_marked(self, vertex):
        '''[6]'''
        idx = index_is(self.vertices, vertex)
        return self.marks[idx] != None

    def mark_vertex(self, vertex):
        '''[7]'''
        idx = index_is(self.vertices, None)
        self.marks[idx] = vertex


    def delete_edge(self, fromVertex, toVertex):
        '''[8]'''
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        self.edges[row][col] = 0
