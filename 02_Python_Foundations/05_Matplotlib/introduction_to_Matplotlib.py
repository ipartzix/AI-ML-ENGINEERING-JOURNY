import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Generate sample data
t = np.linspace(0, 2 * np.pi, 100)
s1 = np.sin(t)
s2 = np.sin(2 * t)
s3 = np.sin(4 * t)

# Create the main plot
fig, ax = plt.subplots()
l1, = ax.plot(t, s1, visible=True, lw=2, label='1 Hz')
l2, = ax.plot(t, s2, visible=True, lw=2, label='2 Hz')
l3, = ax.plot(t, s3, visible=True, lw=2, label='4 Hz')

ax.set_title("Toggle Lines with CheckButtons")
plt.subplots_adjust(left=0.25)  # Leave space for check buttons

# Define position for CheckButtons [left, bottom, width, height]
check_ax = plt.axes([0.05, 0.4, 0.15, 0.15])
labels = ('1 Hz', '2 Hz', '4 Hz')
visibility = [l1.get_visible(), l2.get_visible(), l3.get_visible()]

# Create CheckButtons
check = CheckButtons(check_ax, labels, visibility)

# Define callback function for toggling
def toggle_visibility(label):
    if label == '1 Hz':
        l1.set_visible(not l1.get_visible())
    elif label == '2 Hz':
        l2.set_visible(not l2.get_visible())
    elif label == '4 Hz':
        l3.set_visible(not l3.get_visible())
    plt.draw()  # Redraw the plot

# Connect the callback
check.on_clicked(toggle_visibility)

plt.show()