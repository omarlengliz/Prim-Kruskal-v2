import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

app = tk.Tk()
app.title("Arbre couvrant minimum  (prim / kruskal )")

paned_window = tk.PanedWindow(app, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=1)

left_frame = tk.Frame(paned_window, width=400, height=400, bg='white')
left_frame.pack_propagate(False)  
paned_window.add(left_frame)

fig = Figure(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=left_frame)
canvas.get_tk_widget().pack()

G = nx.Graph()

right_frame = tk.Frame(paned_window, width=500)
right_frame.pack_propagate(False)
paned_window.add(right_frame)

edge_input_label = tk.Label(right_frame, text="Remplire par les noeuds et les arcs dans chaque ligne   (Exemple, A,B,3):")
edge_input_label.pack()

edge_input = tk.Text(right_frame, height=20, width=50)
edge_input.pack()


def animate_mst(algorithm):
    edge_data = edge_input.get("1.0", "end-1c").split('\n')
    G.clear()
    for edge in edge_data:
        if not edge:
            continue
        node1, node2, weight = map(str.strip, edge.split(','))
        G.add_edge(node1, node2, weight=int(weight))

    mst_edges = list(nx.minimum_spanning_edges(G, algorithm=algorithm, data=True))
    mst_G = nx.Graph()
    mst_G.add_edges_from(mst_edges)

    pos = nx.spring_layout(G)
    
    def update_mst_drawing():
        axes.clear()
        nx.draw_networkx_nodes(mst_G, pos, node_color='blue', ax=axes)
        nx.draw_networkx_labels(mst_G, pos, ax=axes)
        nx.draw_networkx_edges(mst_G, pos, edgelist=mst_edges, width=2, edge_color='red', ax=axes)
        edge_labels = nx.get_edge_attributes(mst_G, 'weight')
        nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=edge_labels, ax=axes)
        edge_weights = nx.get_edge_attributes(mst_G, 'weight')
        total_cost = sum(edge_weights.values())
        axes.set_title(f" (cout: {total_cost})")
        canvas.draw()

    def animate_step(i):
        if i == len(mst_edges):
            update_mst_drawing()
            return
        u, v, d = mst_edges[i]
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=2, edge_color='red', ax=axes)
        edge_labels = {(u, v): d['weight']}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=axes)
        canvas.draw()
    
    fig.clear()
    axes = fig.add_subplot(111)
    nx.draw_networkx_nodes(G, pos, node_color='blue', ax=axes)
    nx.draw_networkx_labels(G, pos, ax=axes)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black', ax=axes)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=axes)
    axes.set_title("Alogrithme :  " +algorithm)    
    canvas.draw()

    for i, edge in enumerate(mst_edges + [None]):  
        app.after(1000 * i, animate_step, i)
def prim_algorithm():
    animate_mst( 'prim')

def kruskal_algorithm():
    animate_mst( 'kruskal')

prim_button = tk.Button(right_frame, text="Prim", command=prim_algorithm)
prim_button.pack()

kruskal_button = tk.Button(right_frame, text="Kruskal", command=kruskal_algorithm)
kruskal_button.pack()

app.mainloop()