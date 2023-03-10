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

def visualize_io_pair(input, output):
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.imshow(input, cmap=cmap, vmax=len(colors))
    ax2.imshow(output, cmap=cmap, vmax=len(colors))
    ax1.axis('off')
    ax2.axis('off')
    plt.show()
