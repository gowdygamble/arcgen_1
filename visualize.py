import matplotlib.pyplot as plt
import matplotlib as mpl

colors = [
            (0,0,0), # black
            (1,0,0), # red
            (0,1,0), # green
            (0,0,1), # blue
        ]


cmap = mpl.colors.LinearSegmentedColormap.from_list(
    'Custom cmap', colors, len(colors))


def visualize_canvas(c):
    plt.figure()
    plt.imshow(c, cmap=cmap, vmax=len(colors))
    plt.show()