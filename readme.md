
# Graph MST Visualization Tool (v2)

This tool provides a visual representation of a graph and its Minimum Spanning Tree (MST) using Prim's or Kruskal's algorithm. It is built using Python with Tkinter for the GUI and NetworkX along with Matplotlib for graph management and visualization.
You can check the [version1](https://github.com/omarlengliz/prim-kruskal) on github 

## Features

- Interactive GUI to input graph edges and their weights
- Buttons to execute Prim's or Kruskal's algorithm
- Visualization of the graph's Minimum Spanning Tree
- Display of each edge's weight in the MST
- Calculation and display of the total cost of the MST

## Prerequisites

Ensure you have Python installed on your system. The recommended version is Python 3.8 or higher. You can download it from the official Python website: https://www.python.org/

Additionally, the following Python libraries are required:
- Tkinter (usually included with Python)
- NetworkX
- Matplotlib

You can install NetworkX and Matplotlib using pip:

```bash
pip install networkx matplotlib
```

## Usage

Run the `graph_mst_app.py` script in your Python environment:

```bash
python graph_mst_app.py
```

Once the application starts:
1. Enter your graph edges in the format `A,B,weight` into the text area, with each edge on a new line.
2. Click on the 'Run Prim's Algorithm' or 'Run Kruskal's Algorithm' button to visualize the MST.
3. The GUI will display the graph's MST and the total cost after the algorithm completes.

## Contributing

Contributions to this project are welcome. Please fork the project, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- The Python community for providing extensive resources and libraries
- Creators of NetworkX and Matplotlib for their excellent tools
