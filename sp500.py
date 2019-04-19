import datetime
import pandas as pd
from bokeh.plotting import figure, output_file, show
from pandas_datareader import data
from pandas_datareader.tests import yahoo

# Ticker is used from yahoo finance. S&P 500 (^GSPC)
startDate = datetime.datetime(2018, 1, 1)
endDate = pd.datetime.now()
df = data.DataReader(name="^GSPC", data_source="yahoo",start=startDate , end=endDate )

print(df)
