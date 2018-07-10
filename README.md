# `gradefigure`

Python module to grade a `matplotlib.figure.Figure` object based on the presence of certain items and numerical data in the `matplotlib.axes.Axes` objects of the `Figure`.

### Example

```
>>> import numpy
>>> from matplotlib import pyplot
>>> from gradefigure import grade_figure
>>> x = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
>>> y = numpy.sin(x)
>>> fig, ax = pyplot.subplots()
>>> ax.set_title('my title')
>>> ax.set_xlabel('x')
>>> ax.set_ylabel('y')
>>> ax.plot(x, y)
>>> grade_figure(fig, ax_items=['title', 'xlabel', 'ylabel'], ax_data=[(x, y)])
(100.0, {'items': {'title': True, 'xlabel': True, 'ylabel': True}, 'data': {0: True}})
```
