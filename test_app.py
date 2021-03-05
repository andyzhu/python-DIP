import datetime
from pathlib import Path
from unittest.mock import MagicMock
import matplotlib.pyplot


from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent

def test_read():
    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    temperature_by_hour = {hour: temperature}

    data_source = MagicMock()
    data_source.read.return_value = temperature_by_hour
    app = App(data_source = data_source, plot = MagicMock())
    assert app.read(file_name = 'something.csv') == temperature_by_hour

def test_draw(monkeypatch):
    plot_mock = MagicMock()
    app = App(
        data_source=MagicMock(),
        plot=plot_mock
    )
    hour = datetime.datetime.now()
    iso_hour = hour.isoformat()
    temperature = 14.52
    temperature_by_hour = {iso_hour: temperature}

    app.draw(temperature_by_hour)
    plot_mock.draw.assert_called_with([hour], [temperature])

def test_configure():
    app = App.Config(
        'config.json'
    )

    assert isinstance(app, App)