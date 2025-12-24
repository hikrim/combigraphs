from combigraphs.graph.builder import create_graph, add_edge
from combigraphs.graph.visualize import plot_graph
from combigraphs.combfuncs.place import placement
from combigraphs.graph.cnt_routes_of_lenght_k_infull_graph import count_routes_of_lenght_k_infull_graph

# k = count_routes_of_lenght_k_infull_graph(5)

# print(k)

graph = create_graph(5)
add_edge(graph, 1, 2)
add_edge(graph, 3, 1)
add_edge(graph, 2, 3)
add_edge(graph, 4, 3)
add_edge(graph, 5, 1)

print(plot_graph(graph))

