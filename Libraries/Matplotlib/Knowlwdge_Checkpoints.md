# Knowledge Checkpoints

## Line Chart
A line chart, also known as a line graph, is a type of chart used to visualize data points connected by straight lines. It is commonly used to track changes over time or to show trends in a continuous data set. The x-axis typically represents the time intervals or categories, while the y-axis represents the values associated with each interval or category.

### matplotlib.pyplot.plot() 
The matplotlib.pyplot.plot() function in Matplotlib is used to create a 2D line plot. It takes arrays of x and y coordinates as input and plots points in a Cartesian plane. By default, the plot() function draws a line from point to point.
It take Two arguments i.e 1st arg for x-axis and 2nd for y-axis
While creating coordinate arrays, ensure that both arrays have the same size because plt.plot will map the x and y values based on their corresponding positions.

### Additional Parameters in matplotlib.pyplot.plot()
| Argument                  | Description                                      |
|---------------------------|--------------------------------------------------|
| **color (c)**             | Defines the color of the line.                   |
| **linewidth (lw)**        | Specifies the thickness of the line.             |
| **linestyle (ls)**        | Sets the style of the line (solid, dashed, etc.).|
| **marker**                | Adds a marker at each data point on the line.    |
| **markersize (ms)**       | Determines the size of the markers.              |
| **markeredgecolor (mec)** | Sets the color of the marker's edge.             |
| **markerfacecolor (mfc)** | Fills the marker with a specified color.         |
| **label**                 | Assigns a label to the line for use in a legend. |
| **alpha**                 | Adjusts the transparency of the line.            |
| **grid**                  | Enables or disables the grid on the plot.        |
| **xlim and ylim**         | Sets the limits for the x-axis and y-axis.       |
| **title**                 | Sets the title of the plot.                      |



## Bar Chart 
A bar chart, also known as a bar graph, is a type of chart that uses rectangular bars to represent data. The length or height of each bar corresponds to the value it represents, making it easy to compare different categories or groups. Bar charts are particularly effective for displaying discrete data, such as counts or frequencies, and are widely used in various fields for presenting and comparing information.

### matplotlib.pyplot.bar() 
The matplotlib.pyplot.bar() function in matplotlib is used to create a bar chart. Atleast 2 arguments are necessary to determine the 'x' and the 'y' axis. 
X-axis defines the positions or labels of the bars.
Y-axis specifies the heights of the bars, which correspond to the values or frequencies we want to visualize.

### Additional Parameters for matplotlib.pyplot.bar() 
| Argument       | Description                                                   |
|----------------|---------------------------------------------------------------|
| **width**      | Specifies the width of the bars. The default value is 0.8.    |
| **color**      | Sets the color of the bars.                                   |
| **align**      | Determines the alignment of the bars with respect to the x positions. It can be 'center' or 'edge'. The default is 'center'. |
| **edgecolor**  | Sets the color of the bar edges.                              |
| **linewidth**  | Specifies the width of the bar edges.                         |


## Pie Chart 
A pie chart is a circular statistical graphic that is divided into slices to illustrate numerical proportions. Each slice of the pie represents a category's contribution to the whole, with the size of the slice being proportional to the category's value. Pie charts are commonly used to visualize the composition of a dataset, showing how different parts make up a whole.

### matplotlib.pyplot.pie()
The matplotlib.pyplot.pie() function in matplotlib is used to create a pie chart: where each slice is proportional to the values in data. Each value in the data array or list corresponds to a slice of the pie, and the size of the slice is proportional to the value it represents.
**Note:** data should be *numeric*.

### Additional Arguments matplotlib.pyplot.pie()
| Argument         | Description                                                                    |
|------------------|--------------------------------------------------------------------------------|
| **labels**       | Labels for each slice in the pie chart.                                        |
| **autopct**      | Format string or function to display percentage of each slice.                 |
| **colors**       | Colors for each slice of the pie chart.                                        |
| **explode**      | Fractional offset for each slice to highlight specific slices.                 |
| **shadow**       | If `True`, draws a shadow beneath the pie chart.                               |
| **startangle**   | Rotates the start of the pie chart by the specified angle.                     |
| **radius**       | Radius of the pie chart.                                                       |
| **pctdistance**  | Distance from the center of the pie to the center of the percentage labels.    |
| **wedgeprops**   | Dictionary of properties for the wedge objects (e.g., line width, edge color). |
| **textprops**    | Dictionary of properties for the text labels (e.g., font size, color).         |
| **normalize**    | If `True`, normalizes the data so that the pie chart adds up to 1.             |
