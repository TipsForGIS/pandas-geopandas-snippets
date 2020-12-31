# create dataframes
pd.read_csv('table.csv') ### a pandas dataframe, first row is column header
pd.read_csv('table.csv', names=['col1','col2']) ### a pandas dataframe with given column names
pd.read_csv('table.csv', skiprows=3) ### a pandas dataframe starting from line 4
pd.read_csv('table.csv', nrows=50) ### a pandas dataframe from the first 50 rows of a csv file
pd.read_csv('table.csv', dtypes={'c1':int,'c7':float}) ### a pandas dataframe with new datatypes for the columns in the dictoinary
pd.read_csv('table.csv', parse_dates=['col7']) ### a pandas dataframe where col7 dtype is converted to date
pd.DataFrame.from_dict(dict_obj, orient='columns') ### a pandas dataframe from a dictionary object where keys are columns, DEFAULT
#ex -> data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
#ex -> pd.DataFrame.from_dict(data)
pd.DataFrame.from_dict(dict_obj, orient='index')  ### a pandas dataframe from a dictionary object where keys are rows indeces

# export dataframe
pd.to_csv('table.csv', index=False) ### exports the dataframe into a csv file without the index column: 0,1,2...

# reading properties of dataframes
df.shape ### returns the dimensions of the dataframe rows_num, cols_num
df.dtypes ### returns the columns data types
df.columns ### returns the columns names

# manipulating column
df.rename(columns={'old name': 'new_name',...}, inplace = True) ### renames column(s) name(s) in a dataframe
df.columns = df.columns.str.replace(' ', '_') ### replaces space characters in column names with underscores
df.drop(['column_name'], axis=1, inplace=True) ### drops a column from the dataframe obj
df.drop(['row_index'], axis=0, inplace=True) ### drops a row from the dataframe obj

# reading from the dataframe plus statistics
df.head() ### returns the first 5 rows of a dataframe
df.tail() ### returns the last 5 rows of a dataframe
df.describe() ### returns a statistical summary table for all the columns in the dataframe: mean, min, max, std etc..
df.describe().min() ### returns the min values for the columns in the dataframe
df.column_name.mean() ### returns the mean of the specified column
df.info(memory_usage='deep') ### returns the memory usage for the dataframe
df.memory_usage(deep=True) ### returns the memory usage for each column in the dataframe
df.isnull().sum() ### returns the sum of null values for each column or series in df
df.notnull().sum() ### returns the sum of not null values for each column or series in df

# iterating the dataframes and the series
for c in df.column_name: print(c) ### iterates a pandas series, a dataframe column
for index, row in df.iterrows(): print(index, row.col1, row.col2) ### iterates a pandas dataframe by index and row

# sorting rows
df.sort_values(by=['column_name']) ### returns a sorted dataframe object by a column name
df.sort_values(by=['column_name'], ascending=False) ### returns a decending sorted dataframe object by a column name

# drop or fill None
df.dropna(how='any', inplace=True) ### drops dataframe rows with none values in any column
df.dropna(how='all', inplace=True) ### drops dataframe rows with none values in all column
df['col3'].dropna(inplace=True) ## drops series rows with none values
df.fillna(value=-1, inplace=True) ### fill none values in dataframe with -1
df['col3'].fillna(value=-1, inplace=True) ### fill none values in series with -1

# drop duplicates
df.drop_duplicates(subset=None, keep='first', inplace=True) ### drops duplicates all columns
df.drop_duplicates(subset=['col2'], keep='first', inplace=True) ### drops duplicates of col2

# change column 'series' data type
df.column_name.astype('int') ### returns a pandas series with a new type of integer
df.column_name.astype('string') ### returns a pandas series with a new type of string
df.str_col.astype('int').mean() ### returns the mean of the specified string type column after casting it to integer

# group by
df.groupby('col3').col2.mean() ### groups by col3 and generates the mean value of col2 based on that

# series
pd.Series([1,2,3]) ### returns a pandas series based on the passed list
df.column_name.value_counts() ### returns the count of each value in a column
df.column_name.unique() ### returns the distinct values in a column
df[df.col.isnull()] ### returns the rows where the value of the column is null or no value, notnull() is also available

# indeces
pd.set_index('column_name',inplace=True) ### changes the index to the specified column

# create new columns
df['new_col'] = df['col1'] * df['col7'] * 2 ### creates a new column with a value created from one line of code
df['new_col'] = df.apply(lambda row: function_name(row['col1'], row['col7']), axis=1) ### creates a new column with a value created from a function

# loc method --> df.loc[rows,cols]
df.loc[0:50, ['col1','col7']] ### returns a new dataframe with the first 50 rows and the specificed columns
df.loc[:,['col1','col7']] ### returns a new dataframe with all rows and the two columns
df.loc[0:50,:] ### returns a new dataframe with the first 50 rows and all columns
df.loc[df.column_name == 'xyz', ['col1','col7']] ### returns rows based on the condition (returning a series of booleans of True values)
df.loc[df.column_name.isin(['val1','val2','val3']),['col4','col5']] ### returns rows where column name value is one of the values in the list
round(df.col1,2).astype('int') ### returns a column or series of float values into int after rounding the float

# set_value
idx = df[df['col_3'] == 'some value'].index ### gets the row index based on a value in a specific column
df.set_value(idx, 'col_7', 'some other value') ### sets the value of another column using the previously defined idx


# save memory
pd.to_numeric(column_name_or_series, downcast='float') ### if the column is in float64 and the values can be handled with float32, it will convert the values. downcast can also work with integer
df.col1.astype('category') ### returns an object column or series as category
pd.read_csv('...').fillna(0) ### fills in the null values with zeros


