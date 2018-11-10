import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show

doc = pd.read_csv('../../resources/general.csv')
df = pd.DataFrame(doc)

start_date = '01/01/2018'
end_date = '01/20/2018'
date = df['date'].astype('datetime64[D]')
mask = (date >= start_date) & (date <= end_date)
frame = date.loc[mask]
# listado = frame.values.tolist()
# print(listado)
# s = df['date'].tolist()
# print(s)
#x = ['01/01/2018', '01/02/2018/', '01/03/2018']
y = [6, 7, 2, 4, 5, 8, 6]

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

p.line(frame, y, legend="Temp.", line_width=2)


show(p)