"""
Example to grade a Matplotlib figure.
"""

import numpy
from matplotlib import pyplot
from gradefigure import grade_figure


# Create the data.
x1 = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
y1 = numpy.sin(x1)
x2 = numpy.linspace(1.0, 5.0, num=61)
y2 = 1.0 + 1.0 * numpy.random.random_sample(x2.shape)

# Plot the data using `pyplot.subplots()`.
fig, ax = pyplot.subplots(figsize=(6.0, 6.0))
ax.grid()
ax.set_title('Example', fontsize=16)
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)
ax.plot(x1, y1, label=r'$y = \sin{x}$')
ax.scatter(x2, y2, label='random')
ax.legend(loc='best', prop={'size': 14})

# Grade the figure.
grade, log = grade_figure(fig, ax_items=['title', 'xlabel', 'ylabel'],
                          ax_data=[(x1, y1), (x2, y2)])
print(grade)
print(log)

# Plot the data using `pyplot.figure()`.
pyplot.figure(figsize=(6.0, 6.0))
pyplot.grid()
pyplot.title('Example', fontsize=16)
pyplot.xlabel('x', fontsize=16)
pyplot.ylabel('y', fontsize=16)
pyplot.plot(x1, y1, label=r'$y = \sin{x}$')
pyplot.scatter(x2, y2, label='random')
pyplot.legend(loc='best', prop={'size': 14})

# Grade the figure.
fig = list(map(pyplot.figure, pyplot.get_fignums()))[-1]
grade, log = grade_figure(fig, ax_items=['title', 'xlabel', 'ylabel'],
                          ax_data=[(x1, y1), (x2, y2)])
print(grade)
print(log)

# pyplot.show()
