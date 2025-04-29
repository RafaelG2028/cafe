#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Imports the pandas library
import pandas as pd


# In[10]:


# Loads the cafe dataset from a CSV file into a DataFrame
cafe = pd.read_csv(r"C:\Users\rafae\OneDrive\Desktop\cafe2.csv")


# In[747]:


# Displays the DataFrame
cafe


# In[749]:


# Provides a summary of the DataFrame
cafe.info()


# In[751]:


# Converts columns from object (character) to numeric format
cafe[['Quantity', 'Price Per Unit', 'Total Spent']] = cafe[['Quantity', 'Price Per Unit', 
                                                            'Total Spent']].apply(pd.to_numeric, errors='coerce')


# In[503]:


# Displays the data types of each column
cafe.dtypes


# In[753]:


# Retrieves a list of the unique values from the 'Item' column
cafe['Item'].unique()


# ### CLEANING AND REFINING THE COLUMN 'Item'

# In[ ]:


# The column 'Item' contains placeholder values: 'UNKNOWN', 'ERROR', and 'NaN', which must be replaced or the corresponding rows removed
# for proper cleaning


# In[755]:


# Counts the occurences of the value 'UNKNOWN' in the 'Item' column 
cafe[cafe['Item'] == 'UNKNOWN'].shape[0]


# In[757]:


# Replaces the generic 'UNKNOWN' label with the specific item based on pricing patterns
def clean_item(row):
    if row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 1:
        return 'Cookie'
    elif row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 1.5:
        return 'Tea'
    elif row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 2:
        return 'Coffee'
    elif row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 3:
        return 'Cake or Juice'
    elif row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 4:
        return 'Sandwich or Smoothie'
    elif row['Item'] == 'UNKNOWN' and row['Price Per Unit'] == 5:
        return 'Salad'
    return row['Item']


# In[759]:


# Uses the custom function to update the 'Item' column, replacing 'Unknown' with the appropriate item name
cafe['Item'] = cafe.apply(clean_item, axis=1)


# In[761]:


# Counts the occurences of the value 'UNKNOWN' in the 'Item' column 
cafe[cafe['Item'] == 'UNKNOWN'].shape[0]


# In[763]:


# Calculates missing 'Price Per Unit' values by dividing 'Total Spent' by 'Quantity'
cafe['Price Per Unit'] = cafe['Price Per Unit'].fillna(cafe['Total Spent'] / cafe['Quantity'])


# In[765]:


# Uses the custom function to update the 'Item' column, replacing 'Unknown' with the appropriate item name
cafe['Item'] = cafe.apply(clean_item, axis=1)


# In[767]:


# Counts the occurences of the value 'UNKNOWN' in the 'Item' column 
cafe[cafe['Item'] == 'UNKNOWN'].shape[0]


# In[769]:


# Filters the DataFrame to identify rows where 'Item' is labeled as 'UNKNOWN' 
cafe[cafe['Item'] == 'UNKNOWN']


# In[771]:


# Counts the occurences of the value 'ERROR' in the 'Item' column 
cafe[cafe['Item'] == 'ERROR'].shape[0]


# In[773]:


# Replaces the generic 'ERROR' label with the specific item based on pricing patterns
def clean_item2(row):
    if row['Item'] == 'ERROR' and row['Price Per Unit'] == 1:
        return 'Cookie'
    elif row['Item'] == 'ERROR' and row['Price Per Unit'] == 1.5:
        return 'Tea'
    elif row['Item'] == 'ERROR' and row['Price Per Unit'] == 2:
        return 'Coffee'
    elif row['Item'] == 'ERROR' and row['Price Per Unit'] == 3:
        return 'Cake or Juice'
    elif row['Item'] == 'ERROR' and row['Price Per Unit'] == 4:
        return 'Sandwich or Smoothie'
    elif row['Item'] == 'ERROR' and row['Price Per Unit'] == 5:
        return 'Salad'
    return row['Item']


# In[775]:


# Uses the custom function to update the 'Item' column, replacing 'ERROR' with the appropriate item name
cafe['Item'] = cafe.apply(clean_item2, axis=1)


# In[777]:


# Counts the occurences of the value 'ERROR' in the 'Item' column 
cafe[cafe['Item'] == 'ERROR'].shape[0]


# In[779]:


# Filters the DataFrame to identify rows where 'Item' is labeled as 'ERROR'  
cafe[cafe['Item'] == 'ERROR']


# In[781]:


# Counts the total number of 'NaN' values in the 'Item' column 
cafe[cafe['Item'].isna()].shape[0]


# In[783]:


# Replaces the generic 'NaN' label with the specific item based on pricing patterns
def clean_item3(row):
    if pd.isna(row['Item']) and row['Price Per Unit'] == 1:
        return 'Cookie'
    elif pd.isna(row['Item']) and row['Price Per Unit'] == 1.5:
        return 'Tea'
    elif pd.isna(row['Item']) and row['Price Per Unit'] == 2:
        return 'Coffee'
    elif pd. isna(row['Item']) and row['Price Per Unit'] == 3:
        return 'Cake or Juice'
    elif pd.isna(row['Item']) and row['Price Per Unit'] == 4:
        return 'Sandwich or Smoothie'
    elif pd.isna(row['Item']) and row['Price Per Unit'] == 5:
        return 'Salad'
    return row['Item']


# In[785]:


# Uses the custom function to update the 'Item' column, replacing 'NaN' with the appropriate item name
cafe['Item'] = cafe.apply(clean_item3, axis=1)


# In[787]:


# Counts the total number of missing 'NaN' values in the 'Item' column 
cafe[cafe['Item'].isna()].shape[0]


# In[789]:


# Filters the DataFrame to identify rows where 'Item' is labeled as 'NaN' 
cafe[cafe['Item'].isna()]


# In[791]:


# Standardizes item names by filling missing values, replacing 'ERROR', and ensuring consistent title case formatting
cafe['Item'] = cafe['Item'].fillna('UNKNOWN').replace('ERROR', 'UNKNOWN').str.title()


# In[793]:


# Retrieves a list of the unique values from the 'Item' column
cafe['Item'].unique()


# In[795]:


# Counts the total number of 'Unknown' values in the 'Item' column 
cafe[cafe['Item'] == 'Unknown'].shape[0]


# In[797]:


# Filters the DataFrame to identify rows where 'Item' is labeled as 'Unknown'
cafe[cafe['Item'] == 'Unknown']

# These six rows should be retained until all possible efforts have been made to determine the correct item. Tracing the transaction using
# 'Transaction Date' and 'Transaction ID' can help recover accurate item details


# ### CLEANING AND REFINING THE COLUMN 'Price Per Unit' 

# In[799]:


# Counts the total number of 'NaN' values in the 'Price Per Unit' column 
cafe[pd.isna(cafe['Price Per Unit'])].shape[0]


# In[801]:


# Filters the DataFrame to identify rows where 'Price Per Unit' is labeled as 'NaN'
cafe[pd.isna(cafe['Price Per Unit'])].head()


# In[803]:


# Replaces the generic 'NaN' label with the correct Price Per Unit based on the associated item
def clean_price(row):
    if pd.isna(row['Price Per Unit']) and row['Item'] == 'Cookie':
        return 1
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Tea':
        return 1.5
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Coffee':
        return 2
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Cake':
        return 3
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Juice':
        return 3
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Sandwich':
        return 4
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Smoothie':
        return 4
    elif pd.isna(row['Price Per Unit']) and row['Item'] == 'Salad':
        return 5
    return row['Price Per Unit']


# In[805]:


# Uses the custom function to update the 'Price Per Unit' column, replacing 'NaN' with the appropriate item name
cafe['Price Per Unit'] = cafe.apply(clean_price, axis=1)


# In[807]:


# Counts the total number of 'NaN' values in the 'Price Per Unit' column 
cafe[pd.isna(cafe['Price Per Unit'])].shape[0]


# In[809]:


# Filters the DataFrame to identify rows where the 'Price Per Unit' column contains the value 'NaN'
cafe[pd.isna(cafe['Price Per Unit'])]

# These six rows correspond to the same entries flagged in the 'Item' colum. As previously noted, they should be traced using 
# 'Transaction Date' and 'Transaction ID' to recover accurate details before considering removal.


# ### CLEANING AND REFINING THE COLUMN 'Quantity'

# In[811]:


# Counts the total number of 'NaN' values in the 'Quantity' column 
cafe[pd.isna(cafe['Quantity'])].shape[0]


# In[813]:


# Filters the DataFrame to identify rows where 'Quantity' is labeled as 'NaN'
cafe[pd.isna(cafe['Quantity'])]


# In[815]:


# Calculates missing 'Quantity' values by dividing 'Total Spent' by 'Price Per Unit'
cafe['Quantity'] = cafe['Quantity'].fillna(cafe['Total Spent'] / cafe['Price Per Unit'])


# In[817]:


# Counts the total number of 'NaN' values in the 'Quantity' column 
cafe[pd.isna(cafe['Quantity'])].shape[0]


# In[819]:


# Filters the DataFrame to identify rows where 'Quantity' is labeled as 'NaN'
cafe[pd.isna(cafe['Quantity'])].head()

# 23 rows remain unresolved due to missing data in the 'Total Spent' column. While these rows lack essential information,
# they should be retained until tracing efforts using 'Transaction Date' and 'Transaction ID' have been completed.


# ### CLEANING AND REFINING THE COLUMN 'Total Spent' 

# In[821]:


# Counts the total number of 'NaN' values in the 'Total Spent' column 
cafe[pd.isna(cafe['Total Spent'])].shape[0]


# In[823]:


# Filters the DataFrame to identify rows where 'Total Spent' is labeled as 'NaN'
cafe[pd.isna(cafe['Total Spent'])]


# In[825]:


# Calculates missing 'Total Spent' values by multiplying 'Quantity' by 'Price Per Unit'
cafe['Total Spent'].fillna(cafe['Quantity'] * cafe['Price Per Unit'], inplace=True)


# In[827]:


# Counts the total number of 'NaN' values in the 'Total Spent' column 
cafe[pd.isna(cafe['Total Spent'])].shape[0]


# In[829]:


# Filters the DataFrame to identify rows where 'Total Spent' is labeled as 'NaN'
cafe[pd.isna(cafe['Total Spent'])].head()

# 20 of These 23 rows correspond to the same entries flagged in the 'Quantity' column. As previously noted, tracing them using 
# 'Transaction Date' and 'Transaction ID' may help recover details before considering removal.


# ### CLEANING AND REFINING THE COLUMN 'Payment Method'

# In[831]:


# Retrieves a list of the unique values from the 'Payment Method' column
cafe['Payment Method'].unique()


# In[833]:


# Standardizes Payment Methods by filling missing values, replacing 'ERROR', and ensuring consistent title case formatting
cafe['Payment Method'] = cafe['Payment Method'].fillna('Unknown').str.replace('ERROR', 'Unknown').str.title()


# In[835]:


# Retrieves a list of the unique values from the 'Payment Method' column
cafe['Payment Method'].unique()


# In[837]:


# Counts the total number of 'Unknown' values in the 'Payment Method' column 
cafe[cafe['Payment Method'] == 'Unknown'].shape[0]


# In[839]:


# Filters the DataFrame to identify rows where 'Payment Method' is labeled as 'Unknown'
cafe[cafe['Payment Method'] == 'Unknown']

# While a significant number of transactions lack a recorded payment method, these rows still offer valuable insights and should be retained.
# To enhance data accuracy, tracing through 'Transaction Date' and 'Transaction ID' should be conductd to determine the actual payment method
# for each of the 3,178 transactions.


# ### CLEANING AND REFINING THE COLUMN 'Location'

# In[841]:


# Retrieves a list of the unique values from the 'Location' column
cafe['Location'].unique()


# In[843]:


# Standardizes Location by filling missing values, replacing 'ERROR', and ensuring consistent title case formatting
cafe['Location'] = cafe['Location'].fillna('Unknown').str.replace('ERROR', 'Unknown').str.title()


# In[845]:


# Retrieves a list of the unique values from the 'Location' column
cafe['Location'].unique()


# In[847]:


# Counts the total number of 'Unknown' values in the 'Location' column 
cafe[cafe['Location'] == 'Unknown'].shape[0]


# In[849]:


# Filters the DataFrame to identify rows where 'Location' is labeled as 'Unknown'
cafe[cafe['Location'] == 'Unknown']

# While a significant number of transactions lack a recorded location, these rows still offer valuable insights and should be retained.
# To enhance data accuracy, tracing through 'Transaction Date' and 'Transaction ID' should be conductd to determine the actual location
# for each of the 3,961 transactions.


# ### CLEANING AND REFINING THE COLUMN 'Transaction Date'

# In[851]:


# Retrieves the data type of the 'Transaction Date' column
cafe['Transaction Date'].dtype


# In[899]:


# Converts 'Transaction Date' from object data type to datetime format
cafe['Transaction Date'] = pd.to_datetime(cafe['Transaction Date'], format='mixed', errors='coerce').dt.date


# In[903]:


# Counts the total number of 'NaN' values in the 'Transaction Date' column 
cafe[pd.isna(cafe['Transaction Date'])].shape[0]


# In[905]:


# Replaces 'NaN' in the 'Transaction Date' column with 'Unknown'
cafe['Transaction Date'] = cafe['Transaction Date'].fillna('Unknown')


# In[907]:


# Counts the total number of 'NaN' values in the 'Transaction Date' column 
cafe[pd.isna(cafe['Transaction Date'])].shape[0]


# In[909]:


# Counts the total number of 'Unknown' values in the 'Transaction Date' column 
cafe[cafe['Transaction Date'] == 'Unknown'].shape[0]


# In[911]:


# Filters the DataFrame to identify rows where 'Transaction Date' is labeled as 'Unknown'
cafe[cafe['Transaction Date'] == 'Unknown']

# While a significant number of transactions lack a recorded Transaction Date, these rows still offer valuable insights and should be retained.
# To enhance data accuracy, tracing through 'Transaction ID' should be conductd to determine the actual date for each of the 460 transactions.


# ### FINAL OVERVIEW

# In[867]:


# Provides a summary of the DataFrame
cafe.info()


# In[869]:


# Replaces NaN values in the column 'Price Per Unit' with the placeholder 'Unknown'
cafe['Price Per Unit'] = cafe['Price Per Unit'].fillna('Unknown')


# In[871]:


# Replaces NaN values in the column 'Quantity' with the placeholder 'Unknown'
cafe['Quantity'] = cafe['Quantity'].fillna('Unknown')


# In[873]:


# Replaces NaN values in the column 'Total Spent' with the placeholder 'Unknown'
cafe['Total Spent'] = cafe['Total Spent'].fillna('Unknown')


# In[875]:


# Provides a summary of the DataFrame
cafe.info()


# In[877]:


# Counts the total occurrences of 'Unknown' across the specified columns
(cafe[['Item', 'Quantity', 'Price Per Unit', 'Total Spent', 'Payment Method', 'Location', 'Transaction Date']].isin(['Unknown']).sum().sum())


# In[879]:


# Counts the total number of 'Unknown' values in the 'Item' column 
cafe[cafe['Item'] == 'Unknown'].shape[0]


# In[881]:


# Counts the total number of 'Unknown' values in the 'Quantity' column 
cafe[cafe['Quantity'] == 'Unknown'].shape[0]


# In[883]:


# Counts the total number of 'Unknown' values in the 'Price Per Unit' column 
cafe[cafe['Price Per Unit'] == 'Unknown'].shape[0]


# In[885]:


# Counts the total number of 'Unknown' values in the 'Total Spent' column 
cafe[cafe['Total Spent'] == 'Unknown'].shape[0]


# In[887]:


# Counts the total number of 'Unknown' values in the 'Payment Method' column 
cafe[cafe['Payment Method'] == 'Unknown'].shape[0]


# In[889]:


# Counts the total number of 'Unknown' values in the 'Location' column 
cafe[cafe['Location'] == 'Unknown'].shape[0]


# In[893]:


# Counts the total number of 'Unknown' values in the 'Transaction Date' column 
cafe[cafe['Transaction Date'] == 'Unknown'].shape[0]


# In[915]:


# Displays the DataFrame
cafe


# In[ ]:




