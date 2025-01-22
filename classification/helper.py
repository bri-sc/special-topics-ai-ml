import matplotlib.pyplot as plt

def plot_tree(tree):
    fig, ax = plt.subplots(figsize=(12, 8))
    _plot_node(ax, tree, x=0.5, y=1, level=0, dx=0.25)
    ax.axis("off")
    plt.show()

def _plot_node(ax, tree, x, y, level, dx):
    if not isinstance(tree, dict):
        ax.text(x, y, f"Class: {tree}", ha="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))
        return
    feature = tree["feature"]
    threshold = tree["threshold"]

    ax.text(x, y, f"X[{feature}] <= {threshold:.2f}", ha="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"))

    y_shift = 10
    left_x = x - dx
    right_x = x + dx

    # Plot left subtree
    ax.plot([x, left_x], [y - y_shift / 10, y - y_shift], color="black")
    _plot_node(ax, tree["left"], left_x, y - y_shift, level + 1, dx * 0.6)

    # Plot right subtree
    ax.plot([x, right_x], [y - y_shift / 10, y - y_shift], color="black")
    _plot_node(ax, tree["right"], right_x, y - y_shift, level + 1, dx * 0.6)