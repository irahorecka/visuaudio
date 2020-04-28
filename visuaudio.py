"""python application to view audio equalizer*
of input sound source"""
import struct
import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import pyaudio
from scipy.fftpack import fft


class AudioStream:
    """stream audio from input source (mic) and continuously
    plot (bar) based on audio spectrum from waveform data"""

    def __init__(self):
        self.traces = set()

        # pyaudio setup
        self.FORMAT = pyaudio.paInt16  # bytes / sample
        self.CHANNELS = 1  # mono sound
        self.RATE = 44100  # samples / sec (44.1 kHz)
        self.CHUNK = 1024  # how much audio processed / frame -- set smaller for higher frame rate

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        # spectrum x points
        self.f = np.linspace(1, int(self.RATE / 2), 64)

        # pyqtgraph setup
        pg.setConfigOptions(antialias=True)
        self.app = QtGui.QApplication(sys.argv)
        self.win = pg.GraphicsWindow(title="Audio Spectrum")
        self.win.setGeometry(10, 52, 480 * 2, 200 * 2)
        # window content setup
        self.audio_plot = self.win.addPlot(row=1, col=1)
        self.audio_plot.setYRange(0.00, 0.25)
        self.audio_plot.setXRange(2000, int(self.RATE / 2))
        self.audio_plot.showGrid(x=True, y=True)
        self.audio_plot.hideAxis("bottom")
        self.audio_plot.hideAxis("left")
        # bargraph init
        self.bargraph = None

    @staticmethod
    def set_gradient_brush():
        """set color gradient, return QtGui.QBrush obj"""
        grad = QtGui.QLinearGradient(0, 0, 0, 1)
        grad.setColorAt(0.1, pg.mkColor("#FF0000"))
        grad.setColorAt(0.24, pg.mkColor("#FF7F00"))
        grad.setColorAt(0.38, pg.mkColor("#FFFF00"))
        grad.setColorAt(0.52, pg.mkColor("#00FF00"))
        grad.setColorAt(0.66, pg.mkColor("#0000FF"))
        grad.setColorAt(0.80, pg.mkColor("#4B0082"))
        grad.setColorAt(0.94, pg.mkColor("#9400D3"))
        grad.setCoordinateMode(QtGui.QGradient.ObjectMode)
        brush = QtGui.QBrush(grad)

        return brush

    def set_plotdata(self, name, data_x, data_y):
        """set plot with init and new data -- reference
        self.traces to verify init or recurring data input"""
        if name in self.traces:
            # update bar plot content
            self.bargraph.setOpts(x=data_x, height=data_y, width=350)
        else:
            self.traces.add(name)
            # initial setup of bar plot
            brush = self.set_gradient_brush()
            self.bargraph = pg.BarGraphItem(
                x=data_x, height=data_y, width=350, brush=brush, pen=(0, 0, 0)
            )
        self.audio_plot.addItem(self.bargraph)

    def update(self):
        """get sound data and manipulate for plotting using fft"""
        # get and unpack waveform data
        wf_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        wf_data = struct.unpack(
            str(2 * self.CHUNK) + "B", wf_data
        )  # 2 * self.CHUNK :: wf_data 2x len of CHUNK -- wf_data range(0, 255)
        # generate spectrum data for plotting using fft (fast fourier transform)
        sp_data = fft(
            np.array(wf_data, dtype="int8") - 128
        )  # - 128 :: any int less than 127 will wrap around to 256 down
        # np.abs (below) converts complex num in fft to real magnitude
        sp_data = (
            np.abs(sp_data[0 : int(self.CHUNK)])  # slice: slice first half of our fft
            * 2
            / (256 * self.CHUNK)
        )  # rescale: mult 2, div amp waveform and no. freq in your spectrum
        sp_data[sp_data <= 0.001] = 0
        self.set_plotdata(name="spectrum", data_x=self.f, data_y=sp_data)

    @staticmethod
    def start():
        """start application"""
        if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
            QtGui.QApplication.instance().exec_()

    def animation(self):
        """call self.start and self.update for continuous
        output application"""
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(20)
        self.start()


if __name__ == "__main__":
    AUDIO_APP = AudioStream()
    AUDIO_APP.animation()
