# Matplotlib Library Knowledge Checkpoints 

## 1. Line Chart
A line chart, also known as a line graph, is a type of chart used to visualize data points connected by straight lines. It is commonly used to track changes over time or to show trends in a continuous data set. The x-axis typically represents the time intervals or categories, while the y-axis represents the values associated with each interval or category.

### matplotlib.pyplot.plot() 
The `matplotlib.pyplot.plot()` function in Matplotlib is used to create a 2D line plot. It takes arrays of x and y coordinates as input and plots points in a Cartesian plane. By default, the plot() function draws a line from point to point.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates of the data points.
- **`y`**: Array-like, the y-coordinates of the data points.

While creating coordinate arrays, ensure that both arrays have the same size because plt.plot will map the x and y values based on their corresponding positions.

### Additional Parameters in matplotlib.pyplot.plot()
| Argument                  | Description                                      |Default vaue        |
|---------------------------|--------------------------------------------------|--------------------|
| **color (c)**             | Defines the color of the line.                   |'b'(blue)           |
| **linewidth (lw)**        | Specifies the thickness of the line.             |1.5                 |
| **linestyle (ls)**        | Sets the style of the line (solid, dashed, etc.).|'-' (solid line)    |
| **marker**                | Adds a marker at each data point on the line.    |`None`              |
| **markersize (ms)**       | Determines the size of the markers.              |6                   | 
| **markeredgecolor (mec)** | Sets the color of the marker's edge.             |`None`              |
| **markerfacecolor (mfc)** | Fills the marker with a specified color.         |`None`              |
| **label**                 | Assigns a label to the line for use in a legend. |`None`              |
| **alpha**                 | Adjusts the transparency of the line.            |1.0 (fully opaque)  |
| **xlim and ylim**         | Sets the limits for the x-axis and y-axis.       |Determined by data  |

Different Line Styles used:

'solid' 	:`'-'`	

'dotted'	:`':'`	

'dashed'	:`'--'`	

'dashdot'	:`'-.'`	

'None'	    :`''` or `' '`






## 2. Pie Chart 
A pie chart is a circular statistical graphic that is divided into slices to illustrate numerical proportions. Each slice of the pie represents a category's contribution to the whole, with the size of the slice being proportional to the category's value. Pie charts are commonly used to visualize the composition of a dataset, showing how different parts make up a whole.

### matplotlib.pyplot.pie()
The `matplotlib.pyplot.pie()` function in matplotlib is used to create a pie chart: where each slice is proportional to the values in data. Each value in the data array or list corresponds to a slice of the pie, and the size of the slice is proportional to the value it represents.
**Note:** Data should be *numeric*.

### Additional Arguments matplotlib.pyplot.pie()
| Argument         | Description                                                                    | Default values|
|------------------|--------------------------------------------------------------------------------|---------------|
| **labels**       | Labels for each slice in the pie chart.                                        |`None`         |
| **autopct**      | Format string or function to display percentage of each slice.                 |`None`         |
| **colors**       | Colors for each slice of the pie chart.                                        |`None`         |
| **explode**      | Fractional offset for each slice to highlight specific slices.                 |`None`         |
| **shadow**       | If `True`, draws a shadow beneath the pie chart.                               |`False`        |
| **startangle**   | Rotates the start of the pie chart by the specified angle.                     |0              |
| **radius**       | Radius of the pie chart.                                                       |1              |
| **pctdistance**  | Distance from the center of the pie to the center of the percentage labels.    |0.6            |
| **wedgeprops**   | Dictionary of properties for the wedge objects (e.g., line width, edge color). |`None`         |
| **textprops**    | Dictionary of properties for the text labels (e.g., font size, color).         |`None`         |
| **normalize**    | If `True`, normalizes the data so that the pie chart adds up to 1.             |`None`         |





## 3. Bar Chart 
A bar chart, also known as a bar graph, is a type of chart that uses rectangular bars to represent data. The length or height of each bar corresponds to the value it represents, making it easy to compare different categories or groups. Bar charts are particularly effective for displaying discrete data, such as counts or frequencies, and are widely used in various fields for presenting and comparing information.

### matplotlib.pyplot.bar() 
The `matplotlib.pyplot.bar()` function in matplotlib is used to create a bar chart. Atleast 2 arguments are necessary to determine the 'x' and the 'y' axis. 

It takes the following arguments:
- **`x`**: Array-like, the categories for the x-axis.
- **`height`**: Array-like, the heights of the bars (values for the y-axis).

**NOTE** use `.barh()` function to create horizontal bar chart

| Argument              | Description                                                    | Default Value     |
|-----------------------|----------------------------------------------------------------|-------------------|
| **width**             | Width of the bars.                                             | 0.8               |
| **color**             | Color of the bars.                                             | 'blue'            |
| **edgecolor**         | Color of the edge of the bars.                                 | `None`            |
| **linewidth**         | Width of the edge of the bars.                                 | 1.0               |
| **align**             | Alignment of the bars ('center' or 'edge').                    | 'center'          |
| **alpha**             | Adjusts the transparency of the bars.                          | 1.0 (fully opaque)|
| **label**             | Label for the dataset, useful when plotting multiple datasets. | `None`            |
| **tick_label**        | Labels for the x-axis ticks.                                   | `None`            |
| **bottom**            | Position of the bottom of the bars (useful for stacked bars).  | 0                 |







## 4. Histogram

A histogram is a type of chart that represents the distribution of a dataset by grouping data points into bins or intervals. It is useful for understanding the frequency distribution and spread of data values. The x-axis represents the bins or intervals, while the y-axis shows the frequency or count of data points within each bin.

### matplotlib.pyplot.hist()

The `matplotlib.pyplot.hist()` function is used to create a histogram in Matplotlib. It takes an array of data values and divides it into bins to show the frequency distribution. The function provides a visual representation of the data distribution and can be customized with various parameters.

It takes the following arguments:
- **`x`**: The data values to be plotted as a histogram.

### Additional Parameters in matplotlib.pyplot.hist()

| Argument              | Description                                                           | Default Value     |
|-----------------------|-----------------------------------------------------------------------|-------------------|
| **bins**              | Number of bins or intervals for the histogram.                        | 10                |
| **range**             | The lower and upper range of the bins.                                | `None`            |
| **density**           | If `True`, the histogram is normalized to form a probability density. | `False`           |
| **histtype**          | Type of histogram to draw (e.g., 'bar', 'step').                      | 'bar'             |
| **color**             | Color of the bars in the histogram.                                   | `None`            |
| **edgecolor**         | Color of the edges of the bars.                                       | `None`            |
| **alpha**             | Adjusts the transparency of the bars.                                 | 1.0 (fully opaque)|
| **label**             | Label for the histogram, useful when plotting multiple histograms.    | `None`            |
| **orientation**       | Orientation of the bars ('vertical' or 'horizontal').                 | 'vertical'        |
| **align**             | Alignment of the bars ('left', 'mid', 'right').                       | 'mid'             |







## 5. Scatter Plot

A scatter plot is a type of chart used to display values for two different variables. Each point on the scatter plot represents an observation in the dataset with coordinates corresponding to the values of the two variables. Scatter plots are useful for identifying relationships, correlations, or patterns between the two variables.

### matplotlib.pyplot.scatter()

The `matplotlib.pyplot.scatter()` function is used to create a scatter plot in Matplotlib. It takes arrays of x and y coordinates as input and plots individual points in a Cartesian plane. This function allows for various customizations, such as point size and color.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates of the data points.
- **`y`**: Array-like, the y-coordinates of the data points.

While creating coordinate arrays, ensure that both arrays have the same size because plt.plot will map the x and y values based on their corresponding positions.

### Additional Parameters in matplotlib.pyplot.scatter()

| Argument              | Description                                                       | Default Value     |
|-----------------------|-------------------------------------------------------------------|-------------------|
| **s**                 | Size of the points in the scatter plot.                           | 20                |
| **c** or **color**    | Color of the points. Can be a single color or an array of colors. | 'b' (blue)        |
| **marker**            | Marker style for the points (e.g., 'o', 'x', '^').                | 'o' (circle)      |
| **alpha**             | Adjusts the transparency of the points.                           | 1.0 (fully opaque)|
| **edgecolor**         | Color of the edge of the points.                                  | `None`            |
| **linewidths**        | Width of the edge of the points.                                  | 1.0               |
| **cmap**              | Colormap for mapping the color array.                             | `None`            |
| **vmin**              | Minimum value for colormap normalization.                         | `None`            |
| **vmax**              | Maximum value for colormap normalization.                         | `None`            |
| **label**             | Label for the dataset, useful when plotting multiple datasets.    | `None`            |







## 6. Box Plot

A box plot, also known as a box-and-whisker plot, is a type of chart used to display the distribution of a dataset. It shows the median, quartiles, and outliers of the data. The box represents the interquartile range (IQR), while the "whiskers" extend to the minimum and maximum values within 1.5 times the IQR. Outliers are plotted as individual points.

### matplotlib.pyplot.boxplot()

The `matplotlib.pyplot.boxplot()` function is used to create a box plot in Matplotlib. It visualizes the distribution of data through quartiles and outliers. The function can be customized to include various statistical details and visual enhancements.

It takes the following arguments:
- **`x`**: Array-like or a list of arrays, where each array represents a dataset for which to create a box plot.

### Additional Parameters in matplotlib.pyplot.boxplot()

| Argument              | Description                                                                       | Default Value |
|-----------------------|-----------------------------------------------------------------------------------|---------------|
| **notch**             | If `True`, creates a notch in the box to represent confidence intervals.          | `False`       |
| **vert**              | If `True`, creates vertical boxes; if `False`, horizontal boxes.                  | `True`        |
| **patch_artist**      | If `True`, fills the boxes with color.                                            | `False`       |
| **showfliers**        | If `True`, displays the outliers as individual points.                            | `True`        |
| **showmeans**         | If `True`, displays the mean of each dataset.                                     | `False`       |
| **meanline**          | If `True`, draws a line at the mean of each dataset (requires `showmeans=True`).  | `False`       |
| **boxprops**          | Dictionary of properties for the box (e.g., color, line width).                   | `None`        |
| **whiskerprops**      | Dictionary of properties for the whiskers (e.g., color, line width).              | `None`        |
| **capprops**          | Dictionary of properties for the caps (e.g., color, line width).                  | `None`        |
| **flierprops**        | Dictionary of properties for the fliers (outliers, e.g., marker size, color).     | `None`        |
| **medianprops**       | Dictionary of properties for the median line (e.g., color, line width).           | `None`        |







## 7. Area Plot

An area plot, also known as an area chart, is a type of chart that displays quantitative data graphically. It is similar to a line plot but fills the area below the line with color. Area plots are useful for showing changes in data over time and for comparing different datasets. The x-axis typically represents time intervals or categories, while the y-axis represents the values.

### matplotlib.pyplot.fill_between()

The `matplotlib.pyplot.fill_between()` function is used to create area plots by filling the area between two horizontal curves. It can be used to create shaded regions under a line plot, which visually represents the magnitude of change.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates of the data points.
- **`y1`**: Array-like, the y-coordinates of the lower curve.
- **`y2`**: Array-like, the y-coordinates of the upper curve (optional). By default y2 will be taken as **'y2 = 0'**

### Additional Parameters in matplotlib.pyplot.fill_between()

| Argument              | Description                                                    | Default Value     |
|-----------------------|----------------------------------------------------------------|-------------------|
| **color**             | Color of the shaded area.                                      | `None`            |
| **alpha**             | Adjusts the transparency of the shaded area.                   | 1.0 (fully opaque)|
| **where**             | Condition for filling between curves (e.g., `y1 > y2`).        | `None`            |
| **interpolate**       | If `True`, interpolates between the values of `y1` and `y2`.    | `False`           |
| **hatch**             | Pattern of hatching for the shaded area.                       | `None`            |
| **linewidth**         | Width of the line boundary of the shaded area.                 | 1.0               |
| **edgecolor**         | Color of the edge of the shaded area.                          | `None`            |
| **label**             | Label for the shaded area, useful when plotting multiple datasets. | `None`        |








## 8. Heatmap

A heatmap is a type of chart that represents data in a matrix format using colors to indicate values. It is useful for visualizing data density or intensity, where colors represent the magnitude of values. Heatmaps are often used for correlation matrices, data patterns, and to highlight areas of interest in a dataset.

### matplotlib.pyplot.imshow()

The `matplotlib.pyplot.imshow()` function is used to display data as an image, i.e., on a 2D regular raster. This function is commonly used to create heatmaps, where each cell in the matrix is colored according to its value.

It takes the following arguments:
- **`X`**: Array-like, the data matrix to be displayed as an image.

### Additional Parameters in matplotlib.pyplot.imshow()

| Argument              | Description                                                       | Default Value     |
|-----------------------|-------------------------------------------------------------------|-------------------|
| **cmap**              | Colormap for mapping the data values to colors.                   | 'viridis'         |
| **interpolation**     | Specifies the interpolation method used when rescaling the image. | 'nearest'         |
| **aspect**            | Aspect ratio of the axes. Can be 'auto', 'equal', or a float.     | 'equal'           |
| **vmin**              | Minimum value for colormap normalization.                         | `None`            |
| **vmax**              | Maximum value for colormap normalization.                         | `None`            |
| **origin**            | Placement of the [0,0] index in the upper left or lower left.     | 'upper'           |
| **extent**            | Bounding box in data coordinates for the image.                   | `None`            |
| **alpha**             | Adjusts the transparency of the image.                            | 1.0 (fully opaque)|
| **norm**              | Normalize instance for colormap normalization.                    | `None`            |



#### Argument list for `interpolation`:
* `nearest`: Assigns the nearest color without interpolation. Best for discrete data.
* `bilinear`: Smooth interpolation between points, useful for continuous data.
* `bicubic`: More complex interpolation, producing smoother results than bilinear.
* `spline16`: Uses spline interpolation for a high-quality smooth gradient.

#### Argument list for `cmap`:

##### Sequential Colormaps (for ordered data)
- **`'viridis'`**: A perceptually uniform colormap transitioning from dark purple to yellow.
- **`'plasma'`**: Transitions from dark purple to bright yellow.
- **`'inferno'`**: Transitions from black to red and yellow.
- **`'magma'`**: Transitions from black to red and white.
- **`'cividis'`**: A perceptually uniform colormap from blue to yellow, suitable for colorblind individuals.
- **`'Greys'`**: Shades of grey from black to white.
- **`'Blues'`**: Shades of blue from light to dark.
- **`'Greens'`**: Shades of green from light to dark.
- **`'Reds'`**: Shades of red from light to dark.
- **`'Oranges'`**: Shades of orange from light to dark.
- **`'Purples'`**: Shades of purple from light to dark.
- **`'BuPu'`**: Blue to purple gradient.
- **`'BuGn'`**: Blue to green gradient.
- **`'YlOrRd'`**: Yellow to red gradient.

##### Diverging Colormaps (for data with a central midpoint)
- **`'coolwarm'`**: Blue to red gradient with white in the middle.
- **`'bwr'`**: Blue to white to red gradient.
- **`'seismic'`**: Similar to `'bwr'` but with more intense color extremes.
- **`'RdBu'`**: Red to blue gradient.
- **`'PiYG'`**: Pink to green gradient.
- **`'PRGn'`**: Purple to green gradient.

##### Cyclic Colormaps (for data that wraps around)
- **`'twilight'`**: Smooth gradient from purple to green.
- **`'twilight_shifted'`**: A shifted version of `'twilight'`.
- **`'hsv'`**: Hue-Saturation-Value colormap with a full spectrum of colors.

##### Qualitative Colormaps (for categorical data)
- **`'Set1'`**: Bright, distinct colors for categories.
- **`'Set2'`**: Another set of distinct colors.
- **`'Set3'`**: Another set with more colors.
- **`'Paired'`**: Pairs of distinct colors.
- **`'tab10'`**: 10 distinct colors for categories.
- **`'tab20'`**: 20 distinct colors.
- **`'tab20b'`**: Another set of 20 distinct colors.
- **`'tab20c'`**: Another variant of 20 distinct colors.
- **`'Pastel1'`**: Soft pastel colors.
- **`'Pastel2'`**: Another set of pastel colors.
- **`'Dark2'`**: Dark, distinct colors.

##### Miscellaneous Colormaps
- **`'rainbow'`**: Full spectrum of rainbow colors.
- **`'flag'`**: Alternating red, white, blue, and black.
- **`'prism'`**: Full spectrum of colors in a prism-like effect.
- **`'ocean'`**: Shades of blue and green, like the ocean.
- **`'gist_rainbow'`**: Similar to `'rainbow'` but with more vibrant colors.
- **`'hot'`**: Transitions from black to red, orange, and yellow, simulating heat.
- **`'cool'`**: Transitions from cyan to magenta, providing a cool color gradient.






## 9. Contour Plot

A contour plot is a type of chart that displays the level curves of a function of two variables. It is used to represent three-dimensional data in two dimensions, where contour lines connect points of equal value. Contour plots are useful for visualizing the shape of a surface or the distribution of values across a grid.

### matplotlib.pyplot.contour()

The `matplotlib.pyplot.contour()` function is used to create contour plots. It takes arrays of x and y coordinates, and an array of values, and plots the contour lines corresponding to different levels of the function.

It takes the following arguments:
- **`X`**: 2D array of x-coordinates.
- **`Y`**: 2D array of y-coordinates.
- **`Z`**: 2D array of values corresponding to the coordinates in `X` and `Y`.

**NOTE:** `.contourf()` for filled countor plot

### Additional Parameters in matplotlib.pyplot.contour()

| Argument              | Description                                                    | Default Value            |
|-----------------------|----------------------------------------------------------------|--------------------------|
| **levels**            | Number of levels or a list of specific contour levels to plot. | Automatically determined |
| **cmap**              | Colormap for mapping the levels to colors.                     | 'viridis'                |
| **colors**            | Colors to use for the contour lines.                           | `None`                   |
| **linestyles**        | Line styles for the contour lines (e.g., 'solid', 'dashed').   | 'solid'                  |
| **linewidths**        | Widths of the contour lines.                                   | 1.0                      |
| **alpha**             | Adjusts the transparency of the contour lines.                 | 1.0 (fully opaque)       |
| **extend**            | Whether to extend the contour lines to the edge of the plot.   | `None`                   |
| **norm**              | Normalize instance for colormap normalization.                 | `None`                   |









## 10. Stack Plot

A stack plot, also known as a stacked area plot, is a type of chart used to display the cumulative data of multiple series. It shows the distribution of each series stacked on top of each other, highlighting the contribution of each series to the total. Stack plots are useful for visualizing how different categories contribute to a total over time or across categories.

### matplotlib.pyplot.stackplot()

The `matplotlib.pyplot.stackplot()` function is used to create stack plots. It takes arrays of x-coordinates and multiple arrays of y-coordinates, where each array represents a different data series. The function stacks the areas under each series on top of each other.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates for the data points.
- **`y`**: Sequence of arrays, where each array represents the y-coordinates of a different data series.

### Additional Parameters in matplotlib.pyplot.stackplot()

| Argument              | Description                                                                 | Default Value     |
|-----------------------|-----------------------------------------------------------------------------|-------------------|
| **colors**            | Colors for each series in the stack plot.                                   | `None`            |
| **labels**            | Labels for each series, useful for the legend.                              | `None`            |
| **alpha**             | Adjusts the transparency of the areas.                                      | 1.0 (fully opaque)|
| **baseline**          | Defines the baseline for stacking (e.g., 'zero', 'weighted').               | 'zero'            |
| **stacked**           | If `True`, the areas are stacked; if `False`, areas are plotted separately. | `True`            |
| **linewidth**         | Width of the line boundaries of the stacks.                                 | 1.0               |
| **edgecolor**         | Color of the edge of the stacks.                                            | `None`            |





 ## 11. Date Time Plot

A Date-Time plot is used to represent data points over time, often visualizing trends, patterns, or fluctuations over a period of time. This type of plot is essential for time series data analysis, such as tracking stock prices, sensor readings, or daily temperature changes.

### `matplotlib.pyplot.plot_date()`

The `matplotlib.pyplot.plot_date()` function is specifically designed to handle date and time data on the x-axis. It allows for easy plotting of time series data where the x-coordinates are date or datetime objects.

It takes the following arguments:
- **`x`**: Array-like, typically datetime objects representing time points.
- **`y`**: Array-like, the values corresponding to each time point.

### Additional Parameters in `matplotlib.pyplot.plot_date()`

| Argument              | Description                                                                 | Default Value     |
|-----------------------|-----------------------------------------------------------------------------|-------------------|
| **fmt**               | A format string for line and marker style (e.g., 'o', '-', '--').            | `'o'`             |
| **tz**                | The time zone for the x-axis if the dates are naive.                         | `None`            |
| **xdate**             | Boolean indicating whether to interpret `x` as dates.                        | `True`            |
| **ydate**             | Boolean indicating whether to interpret `y` as dates.                        | `False`           |
| **color**             | Sets the color of the plotted line and markers.                              | `None`            |
| **marker**            | Sets the marker style for data points.                                       | `None`            |
| **label**             | Label for the data series (useful for legends).                              | `None`            |
| **linewidth**         | Width of the plotted line.                                                   | 1.5               |
| **linestyle**         | Style of the plotted line (e.g., '-', '--', '-.', ':').                      | `'solid'`         |






#

# Additional functions:


##   show() function
The **`show()`** function in Matplotlib is used to display all the figures or plots that have been created. It renders the visual output of the charts, such as line plots, scatter plots, bar charts, and more, in a window or inline in environments like Jupyter notebooks.

* It does not take any mandatory arguments.
* It is typically called at the end of plotting commands to ensure the graphs are displayed properly.
* In Jupyter notebooks, plots often display automatically, but in scripts or programs, plt.show() is needed to explicitly render the plots.
* Without calling plt.show(), the graphs may not appear, especially in standalone scripts.






## title() function
The **`title()`** function in Matplotlib is used to set a title for the current plot or graph. It adds a descriptive text at the top of the figure to help identify or explain the plot.

**Syntax** : `matplotlib.pyplot.title(label, fontdict=None, loc='center', **kwargs)`

### Parameters:
* `label`: (str) The title text that will appear at the top of the plot.
* `fontdict`: (dict, optional) A dictionary to customize the font properties, such as font size, color, weight, etc.
* `loc`: (str, optional) Determines the alignment of the title. Can be:
    * `'center'` (default)
    * `'left'`
    * `'right'`
* `**kwargs`: Other keyword arguments to style the text (e.g., fontsize, color, etc.).







## xlable() function:
The **`xlabel()`** function is used to set the label for the x-axis of a plot.

**Syntax** : `matplotlib.pyplot.xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)`
### Parameters:

`xlabel`: (str) The label text for the x-axis.
`fontdict`: (dict, optional) A dictionary to customize the font properties, such as font size, color, weight, etc.
`labelpad`: (float, optional) Spacing in points between the label and the x-axis.
`**kwargs`: Additional arguments to control the appearance of the text (e.g., color, fontsize).

## ylable() function:
The **`ylabel()`** function is used to set the label for the y-axis of a plot.

**Syntax** : `matplotlib.pyplot.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)`

### Parameters:

* `ylabel`: (str) The label text for the y-axis.
* `fontdict`: (dict, optional) A dictionary to customize the font properties, such as font size, color, weight, etc.
* `labelpad`: (float, optional) Spacing in points between the label and the y-axis.
* `**kwargs`: Additional arguments to control the appearance of the text (e.g., color, fontsize).





## subplot() function:
The `subplot()` function in Matplotlib is used to create multiple subplots in a single figure. It divides the figure into a grid of subplots, and allows you to specify which subplot to activate.

**Syntax** : `matplotlib.pyplot.subplot(nrows, ncols, index, **kwargs)`
### Parameters:
* `nrows`: Number of rows in the grid.
* `ncols`: Number of columns in the grid.
* `index`: Index of the subplot to be created or accessed. This is a 1-based index, so the first subplot is 1, the second subplot is 2, and so on.
* `**kwargs`: Additional keyword arguments that can be passed to customize the subplot (e.g., title, xlabel, ylabel).

*NOTE* : Use this function before `matplotlib.pyplot.<plotting functions>()`





## annotate() function:
The plt.annotate() function in Matplotlib is used to add text annotations at specific points on a plot. It allows you to highlight or explain certain data points by attaching descriptive text to them.

**Syntax** : `matplotlib.pyplot.annotate(text, xy, xytext=None, arrowprops=None, **kwargs)`

### Parameters:

* `text`: (str) The text to display as the annotation.
* `xy`: (tuple) The (x, y) coordinates of the point being annotated.
* `xytext`: (tuple, optional) The (x, y) coordinates where the annotation text should be displayed. If not provided, the text is displayed at the same location as xy.
* `arrowprops`: (dict, optional) A dictionary to customize the appearance of the arrow that connects the text to the annotated point. This can include properties like arrowstyle, color, linewidth, etc.
* `**kwargs`: Additional keyword arguments to style the text (e.g., fontsize, color, weight).






## tight_layout() function:
The `tight_layout()` function in Matplotlib is used to automatically adjust the subplot parameters to give specified padding and prevent overlaps between plot elements. It helps to ensure that all subplots fit into the figure area without any clipping.

**Syntax**:  `matplotlib.pyplot.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)`
### Parameters:
* `pad`: (float, optional) Padding between the edges of the figure and the edges of subplots, as a fraction of the font size. Default is 1.08.
* `h_pad`: (float, optional) Padding (height) between rows of subplots. If None, it defaults to pad. Default is None.
* `w_pad`: (float, optional) Padding (width) between columns of subplots. If None, it defaults to pad. Default is None.
* `rect`: (tuple, optional) A rectangle (left, bottom, right, top) in normalized figure coordinates that specifies the area where subplots should fit. The default is None, which means the full figure area is used.
* `thin`: (bool, optional) If True, uses a thinner algorithm for layout adjustments. Default is False.






## errorbar() function:
The `plt.errorbar()` function in Matplotlib is used to create a plot with error bars, which are used to represent the uncertainty or variability of the data points. Error bars are helpful for visualizing the precision of measurements or the spread of data.

**Syntax**:  `matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt='o', ecolor='black', elinewidth=1, capsize=3, capthick=1, **kwargs)`

### Parameters:
* `x`: (array-like) The x-coordinates of the data points.
* `y`: (array-like) The y-coordinates of the data points.
* `yerr`: (array-like, optional) The vertical error (uncertainty) for each data point. It can be a single value or an array of the same length as y.
* `xerr`: (array-like, optional) The horizontal error (uncertainty) for each data point. It can be a single value or an array of the same length as x.
* `fmt`: (str, optional) The format string for the data points (e.g., 'o' for circles, '-' for lines). Default is 'o'.
* `ecolor`: (str, optional) The color of the error bars. Default is 'black'.
elinewidth: (float, optional) The width of the error bars. Default is 1.
* `capsize`: (float, optional) The size of the caps at the end of the error bars. Default is 3.
* `capthick`: (float, optional) The thickness of the caps at the end of the error bars. Default is 1.
* `**kwargs`: Additional keyword arguments to customize the appearance of the plot (e.g., color, linestyle, markersize).






## savefig() function:
The savefig() function in Matplotlib is used to save the current figure to a file. You can save the figure in various formats such as PNG, PDF, SVG, EPS, etc.

**Syntax**: `matplotlib.pyplot.savefig(fname, dpi=None, bbox_inches=None, pad_inches=0.1, transparent=False, **kwargs)`

### Parameters:
* `fname`: (str or Path-like) File name or path to save the figure to. It can include the file extension to specify the format (e.g., `plot.png`).
* `dpi`: (int, optional) Dots per inch. This controls the resolution of the saved figure. Default is `None`, which uses the figure's current DPI setting.
* `bbox_inches`: (str or Bbox, optional) Bounding box in inches for the figure. If set to `'tight'`, it will fit the bounding box to the figure's contents.
* `pad_inches`: (float, optional) Padding around the figure when `bbox_inches` is set to 'tight'. Default is 0.1.
* `transparent`: (bool, optional) If `True`, the figure background will be transparent. Default is `False`.
* `**kwargs`: Additional keyword arguments passed to the underlying `backend`.






## plt.grid():
# Grid Function in Matplotlib

The `grid()` function in Matplotlib is used to control the visibility and appearance of grid lines in a plot. Grid lines are useful for enhancing the readability of plots by making it easier to interpret the values.
**Syntax:**   `matplotlib.pyplot.grid(b=None, which='major', axis='both', **kwargs)`

### Parameters:
* `b`: (bool, optional) Whether to display the grid lines. If `True`, the grid is enabled; if `False`, it is disabled. If `None`, it toggles the grid state.
* `which`: (str, optional)
Determines which grid lines to apply the function to. Options are:
    * `'major'` (default): Major grid lines.
    * `'minor'`: Minor grid lines.
    * `'both'`: Both major and minor grid lines.
* `axis`: (str, optional)
Specifies which axis to apply the grid lines to. Options are:
    * `'both'` (default): Both x and y axes.
    * `'x'`: Only x-axis.
    * `'y'`: Only y-axis.
* `**kwargs`: Additional keyword arguments to customize grid line appearance. Examples include:
    * `color`: Color of the grid lines.
    * `linestyle`: Style of the grid lines (e.g., '-', '--', ':').
    * `linewidth`: Width of the grid lines.






## xticks() and yticks() functions

The `xticks()` and `yticks()` functions in Matplotlib are used to customize the tick locations and labels on the x-axis and y-axis, respectively. These functions allow you to define specific tick positions, customize tick labels, and style the ticks.

**Syntax**
`matplotlib.pyplot.xticks(ticks=None, labels=None, **kwargs)`
`matplotlib.pyplot.yticks(ticks=None, labels=None, **kwargs)`

### Parameters

* `ticks`: (array-like, optional)
    * Specifies the positions of the ticks on the axis.
    * If None, it uses the default tick locations.
* `labels`: (array-like, optional)
    * Defines the labels for the ticks. The length of labels should match the number of ticks.
    * f None, default tick labels (numbers) will be used.
* `**kwargs`: Additional keyword arguments to style the tick labels. Some common options include:
    * `fontsize`: Adjusts the size of the tick labels.
    * `rotation`: Rotates the tick labels to a specific angle (useful for crowded labels).
    * `color`: Changes the color of the tick labels.
    * `fontweight`: Adjusts the weight of the font (e.g., bold).







## xlim() and ylim() functions

The `xlim()` and `ylim()` functions in Matplotlib are used to set or get the limits of the x-axis and y-axis, respectively. These functions help in defining the range of data displayed on the axes, allowing you to zoom in or out of specific portions of your plot.

**Syntax**
`matplotlib.pyplot.xlim(left=None, right=None)`
`matplotlib.pyplot.ylim(bottom=None, top=None)`

### Parameters

* `left`, `right` (for `xlim`):
    * `left`: (float, optional) The minimum limit of the x-axis.
    * `right`: (float, optional) The maximum limit of the x-axis.
    * If None, the limit will not be changed.
* `bottom`, `top` (for `ylim`):
    * `bottom`: (float, optional) The minimum limit of the y-axis.
    * `top`: (float, optional) The maximum limit of the y-axis.
    * If None, the limit will not be changed.






## gca() function
**Get Current Axes**

The gca() function stands for Get Current Axes. It returns the current active Axes instance in the current Figure. If no axes exist in the current figure, it creates one.

**Syntax:** `ax = plt.gca()`






## gcf() function
**Get Current Figure**
The gcf() function stands for Get Current Figure. It returns the current active Figure instance. If no figure exists, it creates a new one.

**Syntax:** `fig = plt.gcf()`




