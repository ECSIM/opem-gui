"""GOPEM plotter."""
from __future__ import unicode_literals
import matplotlib
matplotlib.use('Qt5Agg')  # Make sure that we are using QT5
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import gopem.helper



class MplCanvas(FigureCanvas):
    """MplCanvas class."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Initialize of MatPlotLib canvas for plotter.

        :param parent: the QWidget parent
        :param width: the initial width of canvas
        :param height: the initial height of canvas
        :param dpi: the dpi of the canvas
        """
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_plot(self, data, x_axis, y_axis):
        """
        Update the data and axis range of the canvas.

        :param data: a dictionary that contains the data points
        :param x_axis: the ticks on X axis
        :param y_axis: the ticks on Y axis
        :return: None
        """
        self.axes.cla()
        self.axes.grid(True, linestyle='-.', which='both')
        if x_axis in data.keys() and y_axis in data.keys():
            x_unit = ""
            y_unit = ""
            title = ""
            self.axes.plot(data[x_axis], data[y_axis], 'r')
            if y_axis in gopem.helper.UnitTable.keys():
                title += gopem.helper.UnitTable[y_axis][0] + "~"
                if gopem.helper.UnitTable[y_axis][1] is not None :
                    y_unit = "({0})".format(gopem.helper.UnitTable[y_axis][1])
            if x_axis in gopem.helper.UnitTable.keys():
                if len(title)!=0:
                    title += gopem.helper.UnitTable[x_axis][0]
                    self.axes.set_title(title)
                if gopem.helper.UnitTable[x_axis][1] is not None :
                    x_unit = "({0})".format(gopem.helper.UnitTable[x_axis][1])
            self.axes.set_xlabel(x_axis+x_unit)
            self.axes.set_ylabel(y_axis+y_unit)

        self.draw()

    def save_fig(self,filename):
        """
        Save figure.

        :param filename: file name
        :return: None
        """
        self.fig.savefig(filename, transparent=True);


class ApplicationWindow(QtWidgets.QWidget):
    """ApplicationWindow class."""

    def __init__(self, *args, **kwargs):
        """
        Application widget for MPLCanvas class.

        :param args: the list of arguments
        :param kwargs: the dictionary of keywords
        """
        super().__init__(*args, **kwargs)
        self.setMinimumSize(400, 400)
        l = QtWidgets.QVBoxLayout(self)
        self.sc = MplCanvas(self, width=20, height=20, dpi=100)

        l.addWidget(self.sc)

    def update_plotter_data(self, data, x_axis, y_axis):
        """
        Update the plotter data and axis.

        :param data: the dictionary of data
        :param x_axis: the Ticks on X axis
        :param y_axis:  the Ticks on Y axis
        :return: None
        """
        self.sc.update_plot(data, x_axis, y_axis)

    def file_quit(self):
        """
        Close the application.

        :return: None
        """
        self.close()

    def close_event(self, ce):
        """
        Slot for close event trigger.

        :param ce: close event
        :return: None
        """
        self.file_quit()

    def clear_plot(self):
        """
        Clear plot.

        :return: None
        """
        self.sc.axes.cla()
