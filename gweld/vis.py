from gweld import Data, Chart, Style

class Vis:
    def __init__(self, data=None, chart=None, style=None):
        self.data = data
        self.chart = chart
        self.style = style

    def __repr__(self):
        return f'Chart(data={self.data!r}, chart={self.chart!r}, style={self.style!r})'

    def __add__(self, other):
        if isinstance(other, Data):
            return Vis(data=other, chart=self.chart, style=self.style)
        if isinstance(other, Chart):
            return Vis(data=self.data, chart=other, style=self.style)
        if isinstance(other, Style):
            return Vis(data=self.data, chart=self.chart, style=other)
        raise TypeError

    def plot(self):
        return self.chart.plot(self)
