import json
import datetime
from pathlib import Path
import matplotlib.dates
import matplotlib.pyplot

BASE_DIR = Path(__file__).resolve(strict=True).parent

class App():
    def __init__(self, data_source, plot):
        self.data_source = data_source
        self.plot = plot

    def read(self, **kwargs):
        return self.data_source.read(**kwargs)

    def draw(self, temperature_by_hour):
        dates = []
        temperatures = []
        for date, temperatue in temperature_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temperatue)
        self.plot.draw(dates, temperatures)
    
    @classmethod
    def Config(cls, filename):
        with open(filename, 'r') as file:
            config = json.load(file)
        data_source = __import__(config['data_source']['name']).DataSource()
        plot = __import__(config['plot']['name']).Plot()
        return cls(data_source, plot)



if __name__ == '__main__':
    import sys
    # from urban_climate_csv import DataSource
    config_file = sys.argv[1]
    file_name = sys.argv[2]
    app = App.Config(config_file)
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)