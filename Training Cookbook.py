''' PART ONE - BASIC PYTHON '''



# Basics

a = 1			# Integer
a = 2.5			# FLoat	
a = 'String'    # String
a = True        # Boolean
a = None       	# Null

a = float(var)	# Convert to Float
a = int(var)	# Convert to Int
a = bool(var)	# Convert to Bool
a = str(var)	# Convert to String

type(var)		# Returns the type of the object
print(var)		# Prints the object
help()			# Returns the help for anything specified

a.count('s')    # Counts the number of times the supplied argument appears in the variable
a.lower()       # Converts the string to lower case
a.upper()       # Converts the string to upper case
a.capitalize()  # Converts the string to title case
a.find('c')     # Finds and returns the index of the first occurance of the argument. Returns -1 if not found.
a.index('V')    # Returns the index of the argument. Returns an error if not found

# Creating Functions

def func1(var1,var2):  											# Defining a function
    '''Help goes here '''     									# Function help (docstring)
    print("There were %s cars counted on %s"  % (var1,var2))  	# Using a string token
    															# Whitespace
func1(var1=600,'Tuesday')										# Calling a function

def func2(var):	 											# if / elif / else syntax								
    '''Help goes here '''
    if var == 'cars':
        return cars_vol											
    elif var == 'bikes':
        return bikes_vol
    elif var == 'buses':
        return buses_vol
    else:
        return 'error'

func2(var=vehicle)

def func3(var):				# Try / Except function
    try:                    # Try tries to execute the code             
        var = var + 100      
        print(var)
    except TypeError:       # Except tells Python how to handle certain exceptions
        var = int(var)    	# Converts the string value to an integer
        var = var + 100      
        print(var)
        
func3(var=a) 

f = lambda x, y : x + y   # Basic syntax for a non-anonymous lambda function
print(type(f),f(1,2))

# Data Structures

list1 = [1,2,3,4,5]					# List
tuple1 = (1,2,3,4,5)           		# Tuple
dict1 = {'key1':'value1',
		 'key2':'value2'}			# Dictionary
myset1 = set()    					# Set

# List Methods

mylist1.append('Item')				# Adding an item to the end of a list  
mylist1.count('Fruit')     			# Counting how many times a value appears within a list
mylist1.remove('Fruit')				# Removing an item from the list
mylist2.sort(reverse=True)			# Reverse sorting a list

tuple2 = tuple(data)				# Tuple Conversion
list2 = list(data)					# List Conversion
dict2 = dict(zip(keys,values))      # Dict Conversion

list1[0]							# Calling the first item in a data structure
list1[-1]							# Callind the last item in a data structure
list1[:3]       					# Returns items up to item 3
list1[3:5]      					# Returns items after item 3 (inclusive) but before item 5
list1[0][1]							# Returning items from a nested data structure

# Loops & Iterators

for item in mylist1:     # Basic for loop 
    print(item)

i = 0                    # Setting the starting value for i
mylist1 = []             # Blank list to append items to

while i <= 9:            # While loop syntax
    mylist1.append(i)    # Appends the current value of i to the list
    i = i + 1            # Adding 1 to i for the current iteration


mylist2 = [item * 10 for item in mylist1]     # List Comprehension syntax


''' PART TWO: PYTHON FOR DATA ANALYSIS '''

import pandas as pd
import numpy as np

# Advanced Data Structures	

arr = np.random.random(10)  					# Creating a Numpy array of 10 random numbers
arr = np.random.random((6,4))     				# Creating a 6 (axis) x 4 (length) array with random numbers

ser = pd.Series(list1)     						# Creating a pandas series using the Series class
ser = pd.Series(data=list1,
				index=['A','B','C','D','E'])   	# Creating a series with a custom index

df = pd.DataFrame(data=[data1,data2,data3],  	# Creating a pandas dataframe
                  index=index_data,           	# Specifying the index
                  columns=cols_data)          	# Specifying the column headers

df = pd.DataFrame({'col1':['A','B','C'],    	# Creating a pandas dataframe from a dictionary
                    'col2':[1,2,3]})   

df = pd.DataFrame({'col1':['A','B','C',],  		# Setting column1 data
                    'col2':[1,2,3]},            # Setting column2 data
                    index = ['a','b','c']) 		# Creating index values



list1 = arr1.tolist()         					# Converting an array to a list
list2 = df2['col1'].tolist()  					# Converting a column to a list
dict1 = df2['col1'].to_dict() 					# Converting a column to a dict 
dict1 = df2.to_dict()         					# Converting a dataframe to a dict

# Reading data in

df = pd.read_csv(csv_path)   					# Imports a csv
df = pd.read_json(json_path)					# Imports a JSON file

df = pd.read_csv(filepath_or_buffer=csv_path,	# Keyword argument for the file location
                  sep=',',                    	# The separator for the data fields. Pandas will try and determine this automatically
                  header = 0,                 	# The row of the input file to use for the headers
                  names = cols,               	# Custom column names - passed as a list
                  index_col = 'Site',         	# Column to use as an index - can also pass a number
                  usecols = [0,1,2,3,4,5,6])  	# Specify specific columns to import

# Grabbing a table from Wikipedia

link = 'https://en.wikipedia.org/wiki/2012_Summer_Olympics_medal_table'
data = pd.io.html.read_html(link)   # The page with our table in (will return a list of objects)
df = pd.DataFrame(data[1])          # The item in the list that is our table
df.columns = df.iloc[0]             # Setting the column headers
df = df.drop(0)                     # Dropping the top row as it contains the headers and not data

df.to_csv(out_path)                             # Exporting a dataframe to a CSV

order = ['Index','Patient ID','Gender','Age','Treatment Type',
         'Baseline Arthritis Score','Arthritis Score','Time of Score'] # List of the new column order
  
# Refining the structure of the dataset:
    
df = df.rename(columns = {'Var1':'Index',
                         'Var2':'ID',
                         'Var3':'Score'})        					# Renaming columns
df = df['Var2','Var3','Var1']                    					# Ordering / Keeping columns in the dataframe.
df = df.drop(['Var3'],axis=1)                    					# Dropping a column. The axis=1 is used to specify the vertical (column) axis
df2 = df[(df['Var1'] > 50)]                                         # Single where clause                        
df3 = df[(df['Var1'] <= 50) & (df['Var2'] == 5)]                    # Multiple where clause
df4 = df[(df['Var1'] <= 50) | (df['Var2'] == 5)]                    # Or clause
df5 = df[df['Var1'].isin([1,2,3])]                                  # In list
df6 = df[~df['Var1'].isin([1,2,3])]                                 # Not in list - note the ~ 
df7 = df[df['Var1'].isin([1,2,3]) & (df['Var2'] != 5)]              # Combination of both where and inlist
df.columns               											# Returns a list of columns

df = df.sort_values(by=['Var1']) 	 			 														  # Sorting the dataframe 
baseline_values = df['Arthritis Score'].unique() 														  # Returns the unique values contained in a column
df['Var'] = df['Var'].fillna(0)  				 														  # Replaces NaN values with 0
df['Arthritis Score'] = df['Arthritis Score'].astype('int')												  # Converting the values in a column to integers
df['Combined Score'] = df['Baseline Arthritis Score'] + df['Arthritis Score']                             # Basic Arithmetic
df['Scores'] = df['Baseline Arthritis Score'].astype('str') + ',' + df['Arthritis Score'].astype('str')   # Using strings
df['Count'] = 1                                                                                           # Creating a new column with a constant value

# Converting data with Functions:

def gd_change (row):              # Creating the function - the 'row' parameter can be any word. Pandas will automatically assign a value based upon the index
    if row['Var'] == 1:
        return 'M'
    elif row['Var'] == 2:
        return 'F'
    else:
        return 'O'
    
df['Var'] = df.apply(gd_change,axis=1)     # Creating a new column using the apply method to apply the function to the dataframe

# Dataframe indexing / iloc

df.iloc[0]       				# Selecting a record based upon the location in the dataframe
df.iloc[0]['Var'] 				# Selecting a record and a column header
df.iloc[0:7]     				# Selecting records based upon a slice
df.iloc[0:7][['Var1','Var2']]  	# Selecting records based upon a slice and a column list
df.ix['a']		                # Selecting a record based upon the index value
df = df.reset_index()         	# Resetting the index
df = df.reset_index(level=0)    # Reseting the index to a specific level
df.reset_index(inplace=True)    # Reseting the index inplace without creating a new object
df = df.set_index('col1')    	# Setting the index to a new variable
df.index.name = None          	# Removing the index name to make it look nicer!

# Merging and Concatenating

df = pd.concat([df1,df2])       	# Concatanating datasets (on top)
df = pd.concat([df1,df2],axis=1)	# Concatanating datasets (sideways)
df = pd.merge(df1,df2)

df = pd.merge(left=df1,
              right=df2,
              left_index=True, 
              right_index=True)   # Setting both left / right index arguments to true will merge on the index 

df = pd.merge(left=df1,
              right=df2,
              left_on='col1', 
              right_on='col4',   # Merging using columns using the left_on / right_on arguments:
              sort=True,         # Sorting the dataframe
              indicator=True)    # Adding a column to indicate the source of data 

df10 = pd.merge(left=df1,
               right=df5,
               how='inner', 	# Options are: inner left right outer
               sort=True)   	    

# Summary Statistics

sum_col = df['Var'].sum()      						# Summing columns (ignores NaN values)
cou_col = df['Var'].count()    						# Counting values in a column (ignores NaN values)
min_col = df['Var'].min()             				# Returns the minimum value in a column
min_idx = df['Var'].idxmin()         				# Returns the index of the minimum value in a column
max_col = df['Var'].max()            				# Returns the maximum value in a column
max_idx = df['Var'].idxmax()         				# Returns the index of the maximum value in a column

''' Averages + Stats '''

med_col = df['Var'].median()                       	# Returns the median  
mean_col = df['Var'].mean()                       	# Returns the mean
mode_col = df['Var'].mode()                        	# Returns the mode
std_col = df['Var'].std()                           # Returns the standard deviation
var_col = df['Var'].var()                           # Returns the variance
qua_col = df['Var'].quantile([.25,.5,.75,1]) 		# Returns the quantile values (note you can use any % values you like!)
stats_col = df['Var'].describe()             		# Returns summary statistics (count, mean, std, min, 25%, 50%, 75%, max)

''' Cumulative Values'''

df['tip cumulative'] = df['Var'].cumsum()           # Creating a column for the Cumulative Sum
df['tip cumulative max'] = df['Var'].cummax()       # Creating a column for the Cumulative Max
df['tip cumulative min'] = df['Var'].cummin()       # Creating a column for the Cumulative Min

# Groupby

gp = df.groupby('Var').sum()         				# Simple Groupby statment
gp = df.groupby(['Var1','Var2']).mean() 			# Grouping by two variables

# String slicing in Pandas

df['data2'] = df['data1'].str[0:3]   # First 3
df['data3'] = df['data1'].str[3:]    # Everything from 3rd 
df['data4'] = df['data1'].str[-1]    # Last

# Binning in Pandas

bins = [0, 25, 50, 75, 100]									# Defining the bin values
names = ['Low', 'Okay', 'Good', 'Great']					# Defining the categories
df['categories'] = pd.cut(df['Var'], bins, labels=names)	# Applying the bins / categories to a new columns

# Duplicates

dup = df.duplicated()              				# Finds duplicates
df = df.drop_duplicates()         				# Drops duplicates 
df = df.drop_duplicates(['Var'])    			# Drops duplicates in the specified column - Defaults to keep the first duplicate
df = df.drop_duplicates(['Var'],keep='last')  	# Keeping the last record

# Pivoting

df = df.pivot(index='time', columns='category', values='data')		# Transposing data

# Datetime format
# List of tokens here: http://strftime.org/

def dttm(row):
	try:
		return pd.to_datetime(row['date'],dayfirst=True, format= "%d/%m/%Y") 		# Converting a variable to a datetime
	except ValueError:																# Except if it can't
		pass
    
df['datetime'] = df.apply(dttm,axis=1)												# Applying the datefime function






''' PART 3: Data Vis '''

# Matplotlib

import pandas as pd
import matplotlib.pyplot as plt # Standard Convention for matplotlib
%matplotlib inline    

# Simple line plot

plt.plot(data1)            # Plotting the data
plt.show()                 # Showing the plot

# Pandas df.plot() method

df[['A','B']].plot(figsize=(10, 6),legend=False) # Only keeping 2 columns, setting the size of the plot and removing the legend
plt.title('Title')                               # Setting the title
plt.ylabel('Y Axis Label')                       # Setting the Y Axis Label
plt.xlabel('X Axis Label')                       # Setting the X Axis Label

# More Matplot Charts

df[['A','B']].plot(kind='bar',figsize=(10, 6),legend=False)				# Bar Chart
df.plot(kind='bar',figsize=(10, 6),legen=False, stacked=True)			# Stacked Bar
df.plot(kind='barh',figsize=(10, 6),legend=False, stacked=True)			# Column Chart
df.plot(kind='scatter',x = 'B', y= 'B',figsize=(10, 6),legend=False)	# Scatter Plot

# Custom Bar Chart:

''' The basic chart '''

chart = df.plot(kind='bar',					# Type of chart
				x='Category',				# x axis data
				y='Data',					# y axis data
				figsize=(10, 6),			# size of the plot (in inches)
				legend=False,   			# removing the legend
                color='#5169A7',			# colour for the bars
                alpha = 1, 					# Setting the transparacy of the bars
                edgecolor='white',			# Setting the colour of the lines
                width=0.95,         		# Setting the width of the bars
                rot=0)                      # Setting the rotation of the labels   
plt.title('Categorical Analysis: Apr 16',	# Setting the title
		  fontsize=14, 						# Setting the fontsize	
		  color='#6E6D6C')           		# Setting the font colour
plt.xlabel('')                              # Removing the x axis label
plt.ylabel('£',						 		# Setting the y axis label
		   fontsize=12, 					# Setting the font size
		   color='#6E6D6C',					# Setting the text colour
		   rotation=360)                    # Setting the rotation of the text

''' Removing the Borders'''

chart.spines["top"].set_visible(False)    
chart.spines["bottom"].set_visible(False)    
chart.spines["right"].set_visible(False)    
chart.spines["left"].set_visible(False) 

''' Removing the ticks '''

chart.tick_params(	  						# Setting the parameters foe the ticks in the borders
    which='both',      						# both major and minor ticks are affected
    bottom='off',      						# ticks along the bottom edge are off
    top='off',         						# ticks along the top edge are off
    left='off',        						# ticks along the left edge are off
    right = 'off')     						# ticks along the right edge are off 

''' Adding some gridlines '''

chart.yaxis.grid(True,						# Setting the gridlines
				 color='grey',				# Gridline color
				 linestyle='-',				# Gridline style
				 alpha=0.4)					# gridline transparency

''' Formatting the x axis labels '''

chart.tick_params(axis='both', colors='#6E6D6C')

''' Saving our chart as a .png file '''

plt.savefig('Chart.png', bbox_inches='tight')

# Custom Scatter Chart:

chart2 = df2.plot(kind='scatter',		# Scatter Chart
                  x = 'data1', 			# x axis
                  y= 'data2',			# y axis
                  color='#ec3a34',		# Setting the marker color
                  marker='s',			# Setting the marker style
                  xlim=(0,1000),		# Setting the x scale range
                  ylim=(0,1000))		# Setting the y scale range




# Seaborn

chart = sns.jointplot(data1,data2)									# Basic Jointplot
chart = sns.jointplot(data1,data2,kind='hex')						# Hex jointplot
chart = sns.kdeplot(data1,data2,shade=True)							# KDE plot
chart = sns.jointplot(data1,data2,kind='kde')						# Jointplot + KDE
chart = sns.boxplot([data1])										# Boxplot
chart = sns.violinplot(data2)										# Violin PLot
chart = sns.violinplot(x="sex", y="total_bill", data=tips)			# Grouped Violin Plot

flight_dframe = flight_dframe.pivot("month","year","passengers") 	# Pivoting the dataset to prepare for the heatmap
sns.heatmap(flight_dframe)  										# Heatmap

# Setting global options in Seaborns

sns.set(style='white',                          # Sets the background style of the plot
        palette='colorblind',       			# Sets the palette to be used (See below)
        font='calibri',                         # Sets the font to be used
        font_scale=1.5)                         # Sets the scale of the font

chart = sns.jointplot(data1,data2,kind='hex',   # Assigning our chart to a variable so we can store it
                     stat_func=None,            # Getting rid of the annotation
                     size = 12)                 # Setting the size of the plot

# Custom Jointplot:

chart = sns.jointplot(data1,data2,kind='hex',   
                     stat_func=None,            # Getting rid of the annotation
                     size = 12)                 # Setting the size of the plot
chart.fig.suptitle('My Hexy Jointplot!',        # The plot title 
                   fontsize=24,                 # The fontsize of the title
                   fontweight='bold',           # The fontweight of the title
                   color='#30476E',             # Setting the color title with a hex code
                   family = 'calibri')          # The font family of the title
plt.subplots_adjust(top=0.95)                   # Shifting the plot down a little bit to make room for the title
plt.show()     

# Custom Heatmap:

flight_dframe = sns.load_dataset('flights')                      # Importing the dataset
flight_dframe = flight_dframe.pivot("month","year","passengers") # Pivoting the dataset
chart2 = sns.heatmap(flight_dframe,
                     annot=True,                                 # Annotates the heatmap with values
                     fmt='d',                                    # Sets the format of the string to be used for the annotation
                     cmap="Blues",                               # Defines the colour scheme for the heatmap
                     linewidths=1,                               # Defines the width of the lines for each cell
                     )
chart2.set_title("Awesome Heatmap",
                 fontsize=24,                                    # The fontsize of the title
                 fontweight='bold',                              # The fontweight of the title
                 color='#30476E',                                # Setting the color title with a hex code
                 family = 'calibri'                              # Setting the font family
                )
chart2.figure.set_size_inches(12,8)                              # Changing the size of the heatmap
chart2.xaxis.set_label_text("Year",
                 fontsize=20,                                    # The fontsize of the X axis label
                 fontweight='bold',                              # The fontweight of the X axis label
                 color='#30476E',                                # Setting the color of the X axis label with a hex code
                 family = 'calibri' 
                )
chart2.yaxis.set_label_text("Month",
                 fontsize=20,                                    # The fontsize of the Y axis label
                 fontweight='bold',                              # The fontweight of the Y axis label
                 color='#30476E',                                # Setting the color of the Y axis label with a hex code
                 family = 'calibri'
                )
plt.show()


# Interactive Bokeh plot

from bokeh.plotting import figure, show
from bokeh.models import HoverTool

hover = HoverTool(
            tooltips=[
                ("Hover Location", "$x,$y"),		# Setting the behaviour of the hovertool
            ]
    )

x = [10,20,30,40,50]
y = [432,523,723,121,523]

chart3 = figure(plot_width=600, plot_height=600, tools=[hover])    # Creating the basic plot
''' The title '''

chart3.title = "An Awesome Plot"                    # Setting the title of the plot
chart3.title_text_font_size = '16'                  # Setting the font size for the title

''' The Line '''

chart3.line(x,y,                                    # Adding data in the form of a line
            line_width=3,                           # Setting the line width
            color='red')                            # Setting the line color

''' The Markers '''

chart3.circle(x,y,                                  # Adding markers in the form of circles 
              line_width=3,                         # Setting the line width
              size = 10,                            # Setting the size of the circle
              color='red',                          # Setting the colour of the circle
              fill_color="white")                   # Setting the fill colour of the circle

''' The Grid '''

chart3.grid.grid_line_color = None                  # Getting rid of the grid

''' y Axis '''

chart3.yaxis.axis_label = 'Something'               # Setting the axis label
chart3.yaxis.axis_label_text_font_size = '14'       # Setting the axis label font size
chart3.yaxis.major_tick_line_color = None           # Removing the ticks from the axis
chart3.yaxis.minor_tick_line_color = None           # Removing the ticks from the axis

''' x axis '''

chart3.xaxis.axis_label = "Or Other"                # Setting the axis label
chart3.xaxis.axis_label_text_font_size = '14'       # Setting the axis label font size
chart3.xaxis.major_tick_line_color = None           # Removing the major ticks from the axis
chart3.xaxis.minor_tick_line_color = None           # Removing the minor ticks from the axis

show(chart3)                                        # Showing the plot