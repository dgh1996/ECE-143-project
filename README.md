# ECE-143-project
In this project, we provide functionalities to:
- Plot useful visualizations of Australian rain
- Train and select models to predict the future whether

## Project dependencies:
pandas
numpy
matplotlib
seaborn
sklearn

## Data: 
The data folder contain the dataset we used (courtesy to https://www.kaggle.com/jsphyg/weather-dataset-rattle-package).

## To use:
runcode.ipynb shows how to run the code. Notice that the features used to train the model can be modified from here. 
In addition, each attempt may be different due to the randomized aspect of data splitting and training initialization.

## Scripts:
The src folder contains the functions that we wrote.

main.py contains essentially the code in the jupyter notebook.
region.py contains functions to add the region column and plot data according to region.
plot.py contains functions to plot the comparison plots by year and by season.
models.py contains functions to split the data, train the models and visualize their performance.
correlation.py contains functions to calculate the correlation and visualize it with a heatmap.
scatter.py contains functions to plot scatter plots of selected datapoints with and without the prediction turned on.
