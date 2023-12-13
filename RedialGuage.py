import matplotlib.pyplot as plt
import numpy as np

def draw_gauge(value, max_value, title):
    # Create a figure and axis with polar projection
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Plot a colored sector representing the gauge value
    theta = np.linspace(0, 2*np.pi, 100)
    radii = np.linspace(0, 1, 100)
    ax.fill_between(theta, 0, radii, color='lightgray')

    angle = 2 * np.pi * (value / max_value)
    ax.fill_between(theta[:int(angle*50)], 0, radii[:int(angle*50)], color='green')

    # Draw the needle
    ax.plot([0, angle], [0, 1], color='red', linewidth=2)

    # Set the direction of the polar plot clockwise
    ax.set_theta_direction(-1)

    # Set the start angle at the top of the plot
    ax.set_theta_offset(np.pi/2.0)

    # Set aspect ratio to be equal
    ax.set_aspect('equal')

    # Remove grid and labels
    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Set title
    ax.set_title(title, va='bottom')

    plt.show()

# Example usage:
draw_gauge(value=75, max_value=100, title='Example Radial Gauge')
