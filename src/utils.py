from matplotlib import pyplot as plt
from datetime import datetime


"""

    ##############################
    # GRAPHING AND VISUALIZATION #
    ############################## 
    
"""


def graph(inputs, outputs, name=None):
    plot_name = name if name is not None else datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    plt.plot(inputs, outputs, label=plot_name)
    plt.grid(True)
    plt.savefig(f"images/{plot_name}.png")


def graph_fn(function, f, t, name=None):
    current = f
    inputs = []
    outputs = []
    while current <= t:
        inputs.append(current)
        outputs.append(function(current))
        current += 0.01

    graph(inputs, outputs, name)
