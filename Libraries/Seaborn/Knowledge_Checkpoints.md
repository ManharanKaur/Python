# Seaborn Library Knowledge Checkpoints

## 1. Line Plot

A line chart, also known as a line graph, is a type of chart used to visualize data points connected by straight lines. It is commonly used to track changes over time or to show trends in a continuous dataset. The x-axis typically represents the time intervals or categories, while the y-axis represents the values associated with each interval or category.

### `seaborn.lineplot()`
The `seaborn.lineplot()` function in the Seaborn library is used to create a line plot. It takes arrays of x and y coordinates as input and plots data points connected by lines. It is particularly useful for visualizing trends and relationships between variables over time or categories.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates of the data points (can be numeric or categorical).
- **`y`**: Array-like, the y-coordinates of the data points (numeric data).
- **`data`**: Dataset (optional) where x and y variables are extracted from.

Seaborn's lineplot can automatically handle multiple lines for different categories, making it useful for more complex datasets.

### Additional Parameters in `seaborn.lineplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will produce lines with different colors.  | `None`             |
| **style**                  | Grouping variable that will produce lines with different styles (dashed, dotted). | `None`             |
| **size**                   | Grouping variable that will produce lines with varying widths. | `None`             |
| **palette**                | Colors to use for the different levels of the `hue` variable. | `None` (default palette) |
| **legend**                 | If `True`, adds a legend for `hue`, `style`, and `size`. | `auto`             |
| **markers**                | Adds markers at each data point on the line.    | `False`            |
| **dashes**                 | Defines line style (solid, dashed, etc.).       | `True`             |
| **alpha**                  | Adjusts the transparency of the lines.          | 1.0 (fully opaque) |

### Different Line Styles:
- **Solid**: Automatically assigned for continuous variables.
- **Dotted**: Can be specified using `dashes=[(2, 2)]` for a dotted line.
- **Dashed**: `dashes=[(5, 5)]`
- **Markers**: Can be added using the `markers` parameter (e.g., `markers=True`).






## 2. Scatter Plot
A scatter plot is a type of chart used to display values for two variables. Each point on the plot corresponds to one observation in the dataset, with its position determined by the values of the two variables. Scatter plots are useful for identifying relationships, correlations, or patterns between two continuous variables.

### `seaborn.scatterplot()`
The `seaborn.scatterplot()` function in Seaborn creates a scatter plot by plotting points on a Cartesian plane. It allows you to visualize the relationship between two continuous variables and can be enhanced with additional features like color, size, and style to represent different categories or groups.

It takes the following arguments:
- **`x`**: Array-like, the x-coordinates of the data points.
- **`y`**: Array-like, the y-coordinates of the data points.
- **`data`**: Dataset (optional) from which the x and y variables are extracted.

### Additional Parameters in `seaborn.scatterplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will color the points by different colors.  | `None`             |
| **size**                   | Grouping variable that will size the points.    | `None`             |
| **style**                  | Grouping variable that will style the points (e.g., different markers). | `None`             |
| **palette**                | Colors to use for the different levels of the `hue` variable. | `None` (default palette) |
| **markers**                | Specifies the marker style for the points.      | `'o'` (circle)     |
| **alpha**                  | Adjusts the transparency of the points.         | 1.0 (fully opaque) |
| **s**                      | Size of the markers.                            | `default size`     |

**Common Marker Styles:**

* Circle: `'o'`
* Square: `'s'`
* Diamond: `'D'`
* Triangle Up:  `'v'`
* Triangle Down: `'^'`
* Cross: `'+'`
* X: `'x'`





## 3. Bar Plot
A bar plot, also known as a bar chart, is a type of chart used to display and compare the frequency, count, or other measures for different categories. In a bar plot, rectangular bars are used to represent the values associated with each category. The length of each bar corresponds to the value of the category it represents.

### `seaborn.barplot()`
The `seaborn.barplot()` function creates a bar plot by plotting the average (or other aggregation) of a quantitative variable across different categories. This function is useful for comparing values across different groups and visualizing differences in means or other summary statistics.

It takes the following arguments:
- **`x`**: Array-like, the categories for the x-axis.
- **`y`**: Array-like, the values for the y-axis.
- **`data`**: Dataset (optional) from which the x and y variables are extracted.

### Additional Parameters in `seaborn.barplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will color the bars by different colors.  | `None`             |
| **palette**                | Colors to use for the different levels of the `hue` variable. | `None` (default palette) |
| **ci**                     | Size of the confidence intervals (if `None`, no confidence interval is plotted). | 95 (percent)        |
| **estimator**              | Function to aggregate data (default is `mean`). | `mean`             |
| **order**                  | Order of the categories for the x-axis.          | `None`             |
| **capsize**                | Size of the caps on the error bars.              | `None`             |
| **errcolor**               | Color of the error bars.                         | `None`             |
| **errwidth**               | Width of the error bars.                         | `None`             |






## 4. Count Plot
A count plot, also known as a bar plot of counts, is a type of chart used to display the number of observations for each category of a categorical variable. Each bar represents the count of occurrences in each category. Count plots are useful for visualizing the distribution of categorical data.

### `seaborn.countplot()`
The `seaborn.countplot()` function creates a count plot by counting the number of observations for each category of a categorical variable. This function helps in understanding the frequency distribution of categories.

It takes the following arguments:
- **`x`**: Array-like, the categories for the x-axis.
- **`y`**: Not typically used for count plots; the counts are computed automatically based on `x`.
- **`data`**: Dataset (optional) from which the x variable is extracted.

### Additional Parameters in `seaborn.countplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will color the bars by different colors.  | `None`             |
| **palette**                | Colors to use for the different levels of the `hue` variable. | `None` (default palette) |
| **order**                  | Order of the categories for the x-axis.          | `None`             |
| **orient**                 | Orientation of the plot (horizontal or vertical). | `'v'` (vertical)   |
| **dodge**                  | If `True`, will separate the bars for different `hue` levels. | `True`             |
| **ax**                     | Matplotlib axes object to plot on.               | `None`             |
| **color**                  | Color of the bars.                              | `None`             |


### Difference Between Bar Plot and Count Plot

**Bar Plot:**
A bar plot displays the value of a numerical variable for each category. It's useful for visualizing various statistics such as averages, sums, or other aggregated metrics.

**Count Plot:**
A count plot shows the number of occurrences of each category. It automatically counts the number of observations for each category and displays these counts as bars.

Let's consider a dataset of anime shows with their genres and ratings.

```python
import pandas as pd
anime_data = pd.DataFrame({
    'title': ['Naruto', 'One Piece', 'Attack on Titan', 'My Hero Academia', 'Demon Slayer', 'Naruto', 'One Piece', 'My Hero Academia'],
    'genre': ['Action', 'Action', 'Action', 'Action', 'Action', 'Action', 'Action', 'Action'],
    'rating': [8.5, 8.7, 9.0, 8.8, 9.1, 8.5, 8.7, 8.8]
})
```
We use a bar plot to show the average rating of each anime:
```python
import seaborn as sns
import matplotlib.pyplot as plt
# Create bar plot showing average rating of each anime
sns.barplot(x='title', y='rating', data=anime_data, estimator='mean', palette='viridis')
plt.xticks(rotation=45)
plt.title('Average Rating of Each Anime')
plt.show()

```
* The y-axis represents the average rating.
* The x-axis represents anime titles.
* Bars show the average rating for each anime.

We use a count plot to show how many times each anime title appears in the dataset

```python
import seaborn as sns
import matplotlib.pyplot as plt
# Create count plot showing the number of occurrences of each anime
sns.countplot(x='title', data=anime_data, palette='viridis')
plt.xticks(rotation=45)
plt.title('Count of Each Anime')
plt.show()
```





## 5. Box Plot
A box plot (also known as a box-and-whisker plot) is a chart used to display the distribution of a dataset by showing the data's quartiles and highlighting any outliers. It is useful for comparing distributions between categories and visualizing measures of central tendency and variability.

### `seaborn.boxplot()`
The `seaborn.boxplot()` function in Seaborn is used to create a box plot. It displays the minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum of the data, along with any outliers.

It takes the following arguments:
- **`x`**: Categorical variable to group the data (optional).
- **`y`**: Quantitative variable to be plotted.
- **`data`**: The dataset from which the variables are extracted.

## Additional Parameters in `seaborn.boxplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will color the boxes by different levels. | `None`             |
| **palette**                | Colors to use for the different levels of the `hue` variable. | `None` (default palette) |
| **orient**                 | Orientation of the plot (horizontal or vertical). | `v` (vertical)     |
| **width**                  | Width of the boxes.                              | 0.8                |
| **dodge**                  | Whether to separate the boxes for different `hue` levels. | `True`             |
| **fliersize**              | Size of the markers for outliers.                | 5                  |
| **linewidth**              | Width of the lines outlining the boxes.          | `None`             |







## 6. Violin Plot
A violin plot is a method of visualizing the distribution of numerical data for different categories. It **combines aspects of both box plots and density plots**, showing the distribution of data across categories through kernel density estimation. The wider parts of the violin represent a higher density of data points.

### `seaborn.violinplot()`
The `seaborn.violinplot()` function in Seaborn is used to create a violin plot. It shows the full distribution of data for each category, making it useful for visualizing multimodal data and comparing distributions across categories.

It takes the following arguments:
- **`x`**: Categorical variable (optional).
- **`y`**: Numerical variable to be plotted.
- **`data`**: The dataset from which the variables are extracted.

### Additional Parameters in `seaborn.violinplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **hue**                    | Grouping variable that will split the violins by different colors. | `None`             |
| **split**                  | If `True`, splits the violins for each hue category. | `False`            |
| **scale**                  | Determines how the width of each violin is scaled (`area`, `count`, or `width`). | `area`             |
| **inner**                  | Controls what is displayed inside the violins (e.g., `box`, `quartile`, or `stick`). | `box`              |
| **bw**                     | Bandwidth for the kernel density estimation.     | `None`             |
| **linewidth**              | Width of the lines outlining the violins.        | `None`             |
| **palette**                | Colors to use for different categories.          | `None` (default palette) |
| **orient**                 | Orientation of the plot (horizontal or vertical). | `v` (vertical)     |







## 7. Heatmap
A heatmap is a graphical representation of data where individual values contained in a matrix are represented as colors. Heatmaps are particularly useful for visualizing correlations between variables, displaying distributions, or summarizing complex datasets.

### `seaborn.heatmap()`
The `seaborn.heatmap()` function in Seaborn is used to create a heatmap. It visualizes data in a matrix form with each cell colored according to its value.

It takes the following arguments:
- **`data`**: 2D dataset (e.g., a DataFrame) to plot.
- **`annot`**: If `True`, writes the data value in each cell.
- **`cmap`**: Colormap to use for coloring the heatmap.
- **`linewidths`**: Width of the lines that will divide each cell.
- **`linecolor`**: Color of the dividing lines between the cells.

### Additional Parameters in `seaborn.heatmap()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **annot_kws**              | Specifies the font properties for annotations.   | `None`             |
| **cbar**                   | Shows or hides the color bar.                    | `True`             |
| **vmin**                   | Minimum value for the color bar scale.           | `None`             |
| **vmax**                   | Maximum value for the color bar scale.           | `None`             |
| **fmt**                    | String formatting code for annotations.          | `.2g`              |
| **xticklabels**            | Labels for the x-axis, can be boolean or list.   | `auto`             |
| **yticklabels**            | Labels for the y-axis, can be boolean or list.   | `auto`             |






## 8. Histogram
A histogram is a type of bar plot used to visualize the distribution of a numerical variable by dividing the data into bins (intervals) and plotting the frequency of data points within each bin. It helps in understanding the underlying frequency distribution (e.g., normal distribution) of the data.

### `seaborn.histplot()`
The `seaborn.histplot()` function in Seaborn is used to create a histogram. It counts the occurrences of data points in each bin and represents these counts as bars.

It takes the following arguments:
- **`x`**: Numerical variable for which the histogram will be plotted.
- **`bins`**: Defines the number of bins or intervals to divide the data.
- **`data`**: The dataset from which the variables are extracted.
- **`hue`**: Grouping variable for color-coding different categories.

### Additional Parameters in `seaborn.histplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **binwidth**               | Width of each bin in the histogram.              | `None`             |
| **binrange**               | Specifies the range (min, max) for the bins.     | `None`             |
| **kde**                    | Whether to plot a kernel density estimate on top of the histogram. | `False`            |
| **color**                  | Color of the bars.                               | `None`             |
| **stat**                   | Defines the bar height (`count`, `density`, `probability`, etc.). | `count`            |
| **multiple**               | Controls how multiple distributions are plotted (`layer`, `dodge`, `stack`). | `layer`            |
| **shrink**                 | Proportion to shrink the width of the bars.      | `1` (no shrink)    |
| **element**                | Visual representation of the bars (`bars`, `step`, or `poly`). | `bars`             |







## 9. KDE Plot (Kernel Density Estimate)
A KDE (Kernel Density Estimate) plot is a way to visualize the probability density function (PDF) of a continuous random variable. It provides a smooth estimate of the data distribution, making it easier to identify the underlying patterns, such as peaks, spread, and skewness.

### `seaborn.kdeplot()`
The `seaborn.kdeplot()` function in Seaborn is used to create a KDE plot. It estimates the density of the data points and draws a smooth curve that represents the distribution.

It takes the following arguments:
- **`x`**: The data for which the density is estimated (univariate KDE).
- **`y`**: If provided, a bivariate KDE plot is created.
- **`data`**: The dataset from which the variables are extracted.

### Additional Parameters in `seaborn.kdeplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **bw_adjust**              | Adjusts the bandwidth of the KDE curve.          | `1` (no adjustment)|
| **shade**                  | Fills the area under the KDE curve with color.   | `False`            |
| **hue**                    | Adds a categorical variable for different KDE curves. | `None`         |
| **cumulative**             | If `True`, plots the cumulative distribution.    | `False`            |
| **multiple**               | When `hue` is used, controls how KDEs are drawn (`layer`, `stack`, `fill`). | `layer`         |
| **common_norm**            | Whether or not to normalize all KDEs to the same height. | `True`      |
| **cut**                    | Extends the curve beyond the extreme data points. | `3`                |
| **clip**                   | Limits the KDE curve within a specific range.    | `None`             |





## 10. Pair Plot
A pair plot is used to plot pairwise relationships in a dataset. It creates a grid of subplots where each numeric variable is plotted against every other numeric variable. Pair plots help visualize potential relationships or distributions in the data.

### `seaborn.pairplot()`
The `seaborn.pairplot()` function plots pairwise relationships for all numeric variables in the dataset.

It takes the following arguments:
- **`data`**: The dataset to plot.
- **`hue`**: A categorical variable to color different subsets of the data.
- **`vars`**: List of variable names to include in the pair plot. If omitted, all variables will be used.
- **`kind`**: The kind of plot to draw (`scatter`, `kde`, or `reg`).

### Additional Parameters in `seaborn.pairplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **diag_kind**              | Type of plot to draw on the diagonal (`auto`, `hist`, `kde`). | `auto`             |
| **palette**                | Color palette for the plot.                      | `None`             |
| **markers**                | Markers for different levels of the `hue` variable. | `None`           |
| **corner**                 | If `True`, only plots the lower triangle of the pair plot grid. | `False`          |







## 11. Joint Plot
A Joint Plot is used to visualize the relationship between two numeric variables, along with their univariate distributions. It **combines a scatter plot** (or another bivariate plot) **with histograms or kernel density estimates (KDE)** for each variable along the axes.

### `seaborn.jointplot()`
The `seaborn.jointplot()` function creates a plot that shows the relationship between two variables, as well as their marginal distributions.

It takes the following arguments:
- **`x`**: The variable on the x-axis.
- **`y`**: The variable on the y-axis.
- **`data`**: The dataset containing the variables.
- **`kind`**: Type of plot to draw (`scatter`, `kde`, `hex`, `reg`).

### Additional Parameters in `seaborn.jointplot()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **kind**                   | Type of plot (`scatter`, `kde`, `reg`, `hex`, etc.). | `scatter`           |
| **hue**                    | Categorical variable to add different color groupings. | `None`         |
| **height**                 | Size of the figure in inches.                    | `6`                |
| **ratio**                  | Ratio of the size of the marginal axes to the central plot. | `5`         |
| **space**                  | Space between the joint plot and the marginal plots. | `0.2`          |
| **dropna**                 | If `True`, drops missing values.                 | `True`             |







## 12. FacetGrid
`FacetGrid` is used to create a grid of plots based on a categorical variable. It allows you to visualize multiple plots of the same data across different subsets, facilitating comparisons across categories. Each subplot represents a particular subset of the data.

### `seaborn.FacetGrid()`
The `seaborn.FacetGrid()` function allows for the creation of multi-plot grids where each plot is visualized based on a categorical variable. You can specify the rows and columns of the grid based on different levels of the variables in the dataset.

It takes the following arguments:
- **`data`**: The dataset to visualize.
- **`row`**: Categorical variable that defines the rows in the grid.
- **`col`**: Categorical variable that defines the columns in the grid.
- **`hue`**: Variable to color the data points based on different categories.
- **`margin_titles`**: If `True`, titles will be on the margin of the grid rather than inside the subplots.

### Additional Parameters in `seaborn.FacetGrid()`
| Argument                  | Description                                      | Default Value      |
|---------------------------|--------------------------------------------------|--------------------|
| **row_order**              | Order to plot the categorical levels in the rows. | `None`             |
| **col_order**              | Order to plot the categorical levels in the columns. | `None`           |
| **hue_order**              | Order to plot the categorical levels for colors.  | `None`           |
| **palette**                | Color palette to use for `hue` variable.          | `None`             |
| **aspect**                 | Aspect ratio of each subplot (width/height).     | `1`                |
| **height**                 | Height of each subplot in inches.                | `2`                |

