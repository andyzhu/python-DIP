import datetime
from pathlib import Path
from unittest.mock import MagicMock
import matplotlib.pyplot


from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent

def test_read():
    app = App()
    for key, value in app.read(filename = BASE_DIR / 'Weather_Data_2009.csv').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value
# print(BASE_DIR / 'Weather_Data_2009.csv')

def test_draw(monkeypatch):
    plot_date_mock = MagicMock()
    show_mock = MagicMock()
    monkeypatch.setattr(matplotlib.pyplot, 'plot_date', plot_date_mock)
    monkeypatch.setattr(matplotlib.pyplot, 'show', show_mock)

    app = App()
    hour = datetime.datetime.now().isoformat()
    temperatue = 14.52
    app.draw({hour: temperatue})

    _, called_temperatue = plot_date_mock.call_args[0]
    assert called_temperatue == [temperatue] # check that plot_date was called with temperatue as second arg
    show_mock.assert_called() # check that show is called