from bokeh.plotting import figure, show, output_file

output_file('vbar.html')

x =  [1, 2, 3, 4, 5]
y =  [6, 7, 2, 4, 5]
y1 = [2, 2, 6, 4, 2]
p = figure(plot_width=400, plot_height=400)
p.vbar(x=x, width=0.5, bottom=0, top=y, color="firebrick")
p.vbar(x=x, width=0.5, bottom=0, top=y1, color="Blue")
show(p)