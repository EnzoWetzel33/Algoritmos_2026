from typing import Any, Optional
from list_ import List



class Graph(List):


    class _nodeVertex():

        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = List()

            def _sort_by_destination(item):
                return item.destination

            self.edges.add_criterion('destination', _sort_by_destination)

        def __str__(self):
            return f"{self.value}"

    class _nodeEdge():

        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"weight: {self.weight} -> destination: {self.destination}"

    def __init__(self, is_dir=True):
        self.is_dir = is_dir

        def sort_by_value(item):
            return item.value

        self.add_criterion('value', sort_by_value)


    def add_vertex(self, value: Any, other_values: Any = None) -> None:
        node_vertex = self._nodeVertex(value, other_values)
        self.append(node_vertex)

    def add_edge(self, weight: Any, origin: Any, destination: Any) -> None:

        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        pos_destination = self.search(destination, 'value')
        if pos_destination is None:
            print('no existe el destino')
            return

        node_edge = self._nodeEdge(weight, destination)
        self[pos_origin].edges.append(node_edge)

        if origin != destination and not self.is_dir:
            node_edge = self._nodeEdge(weight, origin)
            self[pos_destination].edges.append(node_edge)

    def delete_vertex(self, value):
        result = self.delete_value(value, 'value')
        
        #limpiar aristas
        for vertex in self:
            # self.delete_edge(vertex.value, value)
            vertex.edges.delete_value(value, 'destination')
        
        return result

    def delete_edge(self, origin, destination) -> Optional[Any]:
        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        result  = self[pos_origin].edges.delete_value(destination, 'destination')

        return result

    def show(self):
        for vertex in self:
            print(vertex)
            if len(vertex.edges) > 0:
                print('aristas ->')
                for edge in vertex.edges:
                    print(edge)

g = Graph(is_dir=False)



g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(1)
g.add_vertex(10)


g.add_edge(23, 4, 10)
g.add_edge(10, 3, 1)
g.add_edge(2, 10, 10)
g.add_edge(7, 4, 1)


# g.show()
# print()
# print(g.delete_edge(4, 10))
# print()
# g.show()

# print()
# print(g.delete_vertex(1))
# print()

g.show()