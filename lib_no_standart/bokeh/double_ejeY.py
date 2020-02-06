from bokeh.models import LinearAxis
from bokeh.models import Range1d
from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show

x = [1, 2, 3, 4, 5]

y = [6, 7, 2, 4, 5]

y2 = [2, 2, 6, 2, 2]

output_file("twin_axis.html")

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, color="red")

p.extra_y_ranges = {"foo": Range1d(start=0, end=100)}

p.line(x, y2, color="blue")

p.add_layout(LinearAxis(y_range_name="foo"), 'right')

show(p)