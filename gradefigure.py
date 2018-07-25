"""
Module to grade a matplotlib.figure.Figure object.
"""

import numpy
from matplotlib import text


def ax_has_xlabel(ax):
  """
  Checks the presence of a xlabel in an matplotlib.axes.Axes object.
  Returns True if there is a non-empty string value for the xlabel.

  Parameters
  ----------
  ax: matplotlib.axes.Axes
    The Axes object to inspect.

  Returns
  -------
  ans: boolean
    True if the xlabel is a non-empty string; otherwise False.

  Examples
  --------
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_xlabel(ax)
  False
  >>> ax.set_xlabel('')
  >>> ax_has_xlabel(ax)
  False
  >>> ax.set_xlabel('x')
  >>> ax_has_xlabel(ax)
  True
  """
  return len(ax.get_xlabel()) > 0


def ax_has_ylabel(ax):
  """
  Checks the presence of a ylabel in an matplotlib.axes.Axes object.
  Returns True if there is a non-empty string value for the ylabel.

  Parameters
  ----------
  ax: matplotlib.axes.Axes
    The Axes object to inspect.

  Returns
  -------
  ans: boolean
    True if the ylabel a non-empty string; otherwise False.

  Examples
  --------
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_ylabel(ax)
  False
  >>> ax.set_ylabel('')
  >>> ax_has_ylabel(ax)
  False
  >>> ax.set_ylabel('y')
  >>> ax_has_ylabel(ax)
  True
  """
  return len(ax.get_ylabel()) > 0


def ax_has_title(ax):
  """
  Checks the presence of a title in an matplotlib.axes.Axes object.
  Returns True if there is a non-empty string value for the title.

  Parameters
  ----------
  ax: matplotlib.axes.Axes
    The Axes object to inspect.

  Returns
  -------
  ans: boolean
    True if the title is a non-empty string; otherwise False.

  Examples
  --------
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_title(ax)
  False
  >>> ax.set_title('')
  >>> ax_has_title(ax)
  False
  >>> ax.set_title('title')
  >>> ax_has_title(ax)
  True
  """
  return len(ax.get_title()) > 0

def ax_has_legend(ax):
  """
  Checks the presence of a labeles and Legend instance in a
  matplotlib.axes.Axes object.
  Returns True if there are labels and Legend instances exist.

  Parameters
  ----------
  ax: matplotlib.axes.Axes
  The Axes object to inspect.

  Returns
  -------
  ans: boolean
  True if there are labels and Legend instances exist; otherwise False.

  Examples
  --------
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_legend(ax)
  False
  >>> fig, ax = pyplot.subplots()
  >>> ax.plot([0, 1, 2], label='a')
  >>> ax_has_legend(ax)
  False
  >>> fig, ax = pyplot.subplots()
  >>> ax.plot([0, 1, 2], label='a')
  >>> ax.legend();
  >>> ax_has_legend(ax)
  True
  """
      
  len_list_lab = len(ax.get_legend_handles_labels()[1])
  val = ax.get_legend()

  if ((len_list_lab > 0) and (val != None)):        
      return True
  return False


def ax_has_data(ax, xref, yref):
  """
  Checks for the presence of the data (xref, yref)
  in an matplotlib.axes.Axes object.

  Parameters
  ----------
  ax: matplotlib.axes.Axes
    The Axes object to inspect.
  xref: list or numpy.ndarray of floats
    The x-data to use as reference.
  yref: list or numpy.ndarray of floats
    The y-data to use as reference.

  Returns
  -------
  ans: boolean
    True if data (xref, yref) are present in the Axes object; other False.

  Examples
  --------
  >>> x = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
  >>> y = numpy.sin(x)
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_data(ax, x, y)
  False
  >>> ax.plot(x, y)
  >>> ax_has_data(ax, x, y)
  True
  >>> fig, ax = pyplot.subplots()
  >>> ax_has_data(ax, x, y)
  False
  >>> ax.scatter(x, y)
  >>> ax_has_data(ax, x, y)
  True
  """
  # Check in matplotlib.lines.Line2D objects.
  for line in ax.get_lines():
    x, y = line.get_data()
    if len(x) == len(xref) and len(y) == len(yref):
      if numpy.allclose(x, xref) and numpy.allclose(y, yref):
        return True
  # Check in matplotlib.collection.PathCollection objects.
  for collection in ax.collections:
    offsets = collection.get_offsets()
    x, y = offsets[:, 0], offsets[:, 1]
    if len(x) == len(xref) and len(y) == len(yref):
      if numpy.allclose(x, xref) and numpy.allclose(y, yref):
        return True
  return False


def fig_has_text(fig):
  """
  Checks for the presence of at least one matplotlib.text.Text object
  in a matplotlib.figure.Figure object that is not in the
  matplotlib.text.Text objects of the matplotlib.axes.Axes of the Figure.
  The function will return True if the string used in one of the
  matplotlib.text.Text objects is not empty.

  Parameters
  ----------
  fig: matplotlib.figure.Figure
    The Figure object to inspect.

  Returns
  -------
  ans: boolean
    True if at least one of the Text objects of the Figure object
    has a non-empty string value; otherwise False.

  Examples
  --------
  >>> fig, ax = pyplot.subplots()
  >>> fig_has_text(fig)
  False
  >>> fig.text(0.0, 0.0, "my text")
  >>> fig_has_text(fig)
  True
  """
  # Find all Text objects present in the Figure.
  fig_texts = set(fig.findobj(text.Text))
  # Exclude Text objects that belongs to Axes objects.
  for ax in fig.get_axes():
    fig_texts -= set(ax.findobj(text.Text))
  # Return False if no Text objects at the Figure level.
  if len(fig_texts) == 0:
    return False
  # Check at least one Text object has a non-empty string.
  for fig_text in fig_texts:
    if len(fig_text.get_text()) > 0:
      return True
  # Otherwise return False.
  return False


def check_figure(fig, ax_items=[], ax_data=[], title_or_text=False):
  """
  Looks for the presence of certain items and numerical data in the
  matplotlib.axes.Axes object of a matplotlib.figure.Figure object.

  Parameters
  ----------
  fig: matplotlib.figure.Figure
    The Figure object to inspect.
  ax_items: list of strings
    The list of items to look for in the Axes objects of the Figure.
    Currently supported: 'title', 'xlabel', and 'ylabel'.
  ax_data: list of 2-tuples of arrays
    The numerical data to look for in the Axes objects of the Figure.
    Example: [(x1, y1), (x2, y2)].
  title_or_text: boolean, optional
    Check for the presence of a Text object with a non-empty string value in
    the Figure object if no title was found;
    default: False.

  Returns
  -------
  log: dict
    Dictionary with the Boolean result for each Axes items and data checked.

  Examples
  --------
  >>> x = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
  >>> y1, y2 = numpy.cos(x), numpy.sin(x)
  >>> fig, ax = pyplot.subplots()
  >>> ax.set_title('my title')
  >>> ax.plot(x, y1)
  >>> check_figure(fig, \
  ...              ax_items=['title', 'xlabel', 'ylabel'], \
  ...              ax_data=[(x, y1), (x, y2)])
  {'items': {'title': True, 'xlabel': False, 'ylabel': False},
  'data': {0: True, 1: False}}
  >>> ax.set_xlabel('x')
  >>> ax.set_ylabel('y')
  >>> ax.scatter(x, y2)
  >>> check_figure(fig, \
  ...              ax_items=['title', 'xlabel', 'ylabel'], \
  ...              ax_data=[(x, y1), (x, y2)])
  {'items': {'title': True, 'xlabel': True, 'ylabel': True},
  'data': {0: True, 1: True}}
  """
  # Check provided items are supported.
  supported_ax_items = {'xlabel', 'ylabel', 'title'}
  if len(set(ax_items) - supported_ax_items) > 0:
    raise ValueError(f'Supported ax_items are {supported_ax_items}')
  # Create a functions dispatcher for Axes items.
  ax_items_dispatcher = {'xlabel': ax_has_xlabel, 'ylabel': ax_has_ylabel,
                         'title': ax_has_title}
  log = {'items': {}, 'data': {}}
  # Loop over the Axes objects of the Figure.
  for ax in fig.get_axes():
    # Check for the presence of items in the Axes (such as labels and title).
    for item in ax_items:
      log['items'][item] = ax_items_dispatcher[item](ax)
    # Check for the presence of a text caption if no title was found.
    if title_or_text and not log['items']['title']:
      log['items']['title'] = fig_has_text(fig)
    # Check for the presence of numerical data in the Axes.
    for i, (x, y) in enumerate(ax_data):
      log['data'][i] = ax_has_data(ax, x, y)
  return log


def grade_figure(fig, ax_items=[], ax_data=[], title_or_text=False,
                 item_points=1.0, data_points=1.0):
  """
  Grades a matplotlib.figure.Figure object,
  looking for the presence of provided items and numerical data
  in the matplotlib.axes.Axes objects.

  Parameters
  ----------
  fig: matplotlib.figure.Figure
    The Figure object to inspect.
  ax_items: list of strings
    The list of items to look for in the Axes objects of the Figure.
    Currently supported: 'title', 'xlabel', and 'ylabel'.
  ax_data: list of 2-tuples of arrays
    The numerical data to look for in the Axes objects of the Figure.
    Example: [(x1, y1), (x2, y2)].
  title_or_text: boolean, optional
    Check for the presence of a Text object with a non-empty string value in
    the Figure object if no title was found;
    default: False.
  item_points: float, optional
    Number of points to add to the grade when an item is found;
    default: 1.0.
  data_points: float, optional
    Number of points to add to the grade when numerical data are found;
    default: 1.0.

  Returns
  -------
  grade: float
    The grade in percent.
  log: dict
    Boolean result for each items and numerical data.

  Examples
  --------
  >>> x = numpy.linspace(0.0, 2.0 * numpy.pi, num=51)
  >>> y = numpy.sin(x)
  >>> fig, ax = pyplot.subplots()
  >>> ax.set_title('my title')
  >>> ax.set_xlabel('x')
  >>> ax.set_ylabel('y')
  >>> ax.plot(x, y)
  >>> grade_figure(fig, \
  ...              ax_items=['title', 'xlabel', 'ylabel'], \
  ...              ax_data=[(x, y)])
  (100.0, {'items': {'title': True, 'xlabel': True, 'ylabel': True},
  'data': {0: True}})
  """
  log = check_figure(fig, ax_items=ax_items, ax_data=ax_data,
                     title_or_text=title_or_text)
  # Grade the Figure.
  max_points = item_points * len(ax_items) + data_points * len(ax_data)
  num_points = (item_points * sum(log['items'].values()) +
                data_points * sum(log['data'].values()))
  if abs(max_points) <= 1.0E-06:
    return None, log
  grade = num_points / max_points * 100.0
  return grade, log
