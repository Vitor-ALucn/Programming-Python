import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 300)
x = np.sin(t) * (np.exp(np.con(t)) - 2*np.cos(4*t))
y = np.con(t) * (np.exp(np.sin(t)) - 2*np.cos(4*t))
plt.figure(figsize=(6, 6))

plt.plot(x, y, color='purple', linewidth=2)
plt.title(-x, y, color='orange', linewidth=2)

plt.title("Beautiful Pattern Plot", fontsize=14)
plt.axis("equal")
plt.axis("off")
plt.show()

# This code generates a beautiful pattern plot using NumPy and Matplotlib.
# It creates a parametric plot based on sine and cosine functions,
# with the x and y coordinates defined by mathematical expressions involving
# exponential and trigonometric functions. The plot is styled with a purple line
# and an orange title, and the axes are set to be equal and turned off for a cleaner look.
# The `np.linspace` function generates a range of values for the parameter `t`,
# which is then used to compute the x and y coordinates of the plot.
# The `plt.figure` function sets the size of the plot, and `plt.plot`
# draws the pattern with specified color and line width.
# The `plt.title` function sets the title of the plot, and `plt.axis("equal")`
# ensures that the aspect ratio is equal, making the plot look symmetrical.
# Finally, `plt.axis("off")` hides the axes for a cleaner appearance,
# and `plt.show()` displays the plot.