import numpy
from matplotlib import pyplot
from gradefigure import grade_figure


x = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
y = numpy.sin(x)

fig, ax = pyplot.subplots()
ax.set_title(r'$y = \sin{x}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
grade, log = grade_figure(fig, ax_items=['title', 'xlabel', 'ylabel'],
                          ax_data=[(x, y)])
print(grade)
print(log)

pyplot.show()
