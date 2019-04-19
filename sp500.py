import datetime
from math import pi
import pandas as pd
from bokeh.models import BoxSelectTool
from bokeh.models.tools import HoverTool
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from pandas_datareader import data
from pandas_datareader.tests import yahoo

# Ticker is used from yahoo finance. S&P 500 (^GSPC)
startDate = datetime.datetime(2018, 1, 1)
endDate = pd.datetime.now()
df = data.DataReader(name="^GSPC", data_source="yahoo", start=startDate , end=endDate )

output_file('gspcGraph.html', title='sp500.py')
TOOLS = "pan,wheel_zoom,reset,save, hover"



plot = figure(x_axis_type='datetime', y_axis_label= 'Price', tools=TOOLS, plot_width=1000, title = "S&P500")


plot.xaxis.major_label_orientation = pi/4
plot.grid.grid_line_alpha= 0.3

plot.segment(df.index, df.High, df.index, df.Low, color="Black")

def increaseDecrease(closePrice , openPrice):
    if closePrice > openPrice:
        value = "Increase"
    elif closePrice < openPrice:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [increaseDecrease(closePrice, openPrice) for closePrice, openPrice in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Close - df.Open)

hours12 = 12 * 60 * 60 * 1000


plot.rect(df.index[df.Status == "Increase"],
          df.Middle[df.Status == "Increase"],
          hours12,
          df.Height[df.Status == "Increase"],
          fill_color = "#142be0",
          line_color = "black"
          )

plot.rect(df.index[df.Status == "Decrease"],
          df.Middle[df.Status == "Decrease"],
          hours12,
          df.Height[df.Status == "Decrease"],
          fill_color = "#e01414",
          line_color = "black"
          )


show(plot)
