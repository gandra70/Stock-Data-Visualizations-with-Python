import datetime
import pandas as pd
from bokeh.plotting import figure, output_file, show
from pandas_datareader import data
from pandas_datareader.tests import yahoo

# Ticker is used from yahoo finance. S&P 500 (^GSPC)
startDate = datetime.datetime(2018, 1, 1)
endDate = pd.datetime.now()
df = data.DataReader(name="^GSPC", data_source="yahoo", start=startDate , end=endDate )

plot = figure(x_axis_type='datetime', width=1000, height=300)

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
          fill_color = "#e01414",
          line_color = "black"
          )

plot.rect(df.index[df.Status == "Decrease"],
          df.Middle[df.Status == "Decrease"],
          hours12,
          df.Height[df.Status == "Decrease"],
          fill_color = "#142be0",
          line_color = "black"
          )

output_file('gspcGraph.html')
show(plot)