# HW2 - Using Functions

##### Grade: 1/7

-3: Didn't check that the dataframe has at least 3 columns   
-1: Didn't check that the dataframe has only the columns you specified in #1.   
-1: You only checked against the "object" class. Please use more specific data types.   
-1: Your test returns True even if only one column in the dataframe is object. I think you might want to initialize TorF to True, and set if to False immediately after you see a violation.   

-----


Create a python module (a file with extension ‘.py’) with the following functions:

1. (4 points) Find an on-line data source (e.g., from data.gov). Write python codes that read the on-line file and create a data frame that has at least 3 columns.

1. (3 points) Create the function test_create_dataframe that takes a pandas DataFrame as input and returns True if the following conditions hold:

   1. The DataFrame contains only the columns that you specified in #1.
   1. The columns contain the correct data type
   1. There are at least 10 rows in the DataFrame.
