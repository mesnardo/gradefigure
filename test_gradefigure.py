"""
Tests for module gradefigure.
"""

import unittest
import numpy
from matplotlib import pyplot
import gradefigure


class TestGradeFigure(unittest.TestCase):
  def setUp(self):
    self.x = numpy.linspace(0.0, 1.0, 11)
    self.y1 = numpy.exp(self.x**2)
    self.y2 = numpy.sin(self.x)

  def _figure_vanilla(self, title=None, xlabel=None, ylabel=None, data=[]):
    pyplot.figure()
    if title:
      pyplot.title(title)
    if xlabel:
      pyplot.xlabel(xlabel)
    if ylabel:
      pyplot.ylabel(ylabel)
    for (x, y) in data:
      pyplot.plot(x, y)
    fig = list(map(pyplot.figure, pyplot.get_fignums()))[-1]
    return fig

  def _figure_complex(self, title=None, xlabel=None, ylabel=None, data=[]):
    fig = pyplot.figure(figsize=(6.0, 6.0))
    ax = fig.add_axes((0.0, 0.1, 0.8, 0.8))
    if xlabel:
      ax.set_xlabel(xlabel, fontsize=16)
    if ylabel:
      ax.set_ylabel(ylabel, fontsize=16)
    for i, (x, y) in enumerate(data):
      ax.plot(x, y, label=f'data {i}', linewidth=1, linestyle='-')
    ax.legend(loc='upper left', prop={'size': 16})
    if title:
      fig.text(0.0, 0.0, title,
               horizontalalignment='left', multialignment='left', fontsize=14)
    return fig

  def test_ax_has_title(self):
    fig = self._figure_vanilla(title='title', data=[(self.x, self.y1)])
    self.assertTrue(gradefigure.ax_has_title(fig.get_axes()[0]))
    fig = self._figure_vanilla(data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_title(fig.get_axes()[0]))
    fig = self._figure_vanilla(title='', data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_title(fig.get_axes()[0]))

  def test_ax_has_xlabel(self):
    fig = self._figure_vanilla(xlabel='x', data=[(self.x, self.y1)])
    self.assertTrue(gradefigure.ax_has_xlabel(fig.get_axes()[0]))
    fig = self._figure_vanilla(data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_xlabel(fig.get_axes()[0]))
    fig = self._figure_vanilla(xlabel='', data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_xlabel(fig.get_axes()[0]))

  def test_ax_has_ylabel(self):
    fig = self._figure_vanilla(ylabel='y', data=[(self.x, self.y1)])
    self.assertTrue(gradefigure.ax_has_ylabel(fig.get_axes()[0]))
    fig = self._figure_vanilla(data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_ylabel(fig.get_axes()[0]))
    fig = self._figure_vanilla(ylabel='', data=[(self.x, self.y1)])
    self.assertFalse(gradefigure.ax_has_ylabel(fig.get_axes()[0]))

  def test_ax_has_data(self):
    fig = self._figure_vanilla(data=[(self.x, self.y1)])
    self.assertTrue(gradefigure.ax_has_data(fig.get_axes()[0],
                                            self.x, self.y1))
    self.assertFalse(gradefigure.ax_has_data(fig.get_axes()[0],
                                             self.x, self.y2))
    fig = self._figure_vanilla(data=[(self.x, self.y1), (self.x, self.y2)])
    self.assertTrue(gradefigure.ax_has_data(fig.get_axes()[0],
                                            self.x, self.y1))
    self.assertTrue(gradefigure.ax_has_data(fig.get_axes()[0],
                                            self.x, self.y2))

  def test_gradefigure_vanilla(self):
    fig = self._figure_vanilla(title='title', xlabel='x', ylabel='y',
                               data=[(self.x, self.y1), (self.x, self.y2)])
    ax_items, ax_data = [], []
    ans, _ = gradefigure.grade_figure(fig, ax_items=ax_items, ax_data=ax_data)
    self.assertIsNone(ans)
    for item in ['title', 'xlabel', 'ylabel']:
      ax_items.append(item)
      ans, _ = gradefigure.grade_figure(fig,
                                        ax_items=ax_items, ax_data=ax_data)
      self.assertEqual(ans, 100.0)
    for data in [(self.x, self.y1), (self.x, self.y2)]:
      ax_data.append(data)
      ans, _ = gradefigure.grade_figure(fig,
                                        ax_items=ax_items, ax_data=ax_data)
      self.assertEqual(ans, 100.0)

  def test_gradefigure_complex(self):
    fig = self._figure_complex(title='title', xlabel='x', ylabel='y',
                               data=[(self.x, self.y1), (self.x, self.y2)])
    ax_items, ax_data = [], []
    ans, _ = gradefigure.grade_figure(fig, ax_items=ax_items, ax_data=ax_data)
    self.assertIsNone(ans)
    for item in ['title', 'xlabel', 'ylabel']:
      ax_items.append(item)
      ans, _ = gradefigure.grade_figure(fig,
                                        ax_items=ax_items, ax_data=ax_data,
                                        title_or_text=True)
      self.assertEqual(ans, 100.0)
      if item == 'title':
        ans, log = gradefigure.grade_figure(fig,
                                            ax_items=ax_items, ax_data=ax_data)
        self.assertFalse(log['items']['title'])
        self.assertEqual(ans, 100.0 * (1.0 - 1 / len(ax_items)))
    for data in [(self.x, self.y1), (self.x, self.y2)]:
      ax_data.append(data)
      ans, _ = gradefigure.grade_figure(fig,
                                        ax_items=ax_items, ax_data=ax_data,
                                        title_or_text=True)
      self.assertEqual(ans, 100.0)


if __name__ == '__main__':
  unittest.main()
