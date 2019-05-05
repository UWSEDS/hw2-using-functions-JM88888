import numpy as np
import pandas as pd

"""Import the Seattle building permits with columns of permit class, permit type and estimated project cost"""
permits = pd.read_csv("https://data.seattle.gov/api/views/76t5-zqzr/rows.csv?accessType=DOWNLOAD",
                                       usecols=["PermitClass", "PermitTypeDesc", "EstProjectCost"],
                                       dtype={"PermitClass": object, "PermitTypeDesc": object, "EstProjectCost":float})


def test_create_dataframe(df):
    """
    Tests a dataframe and returns True if the following three conditions hold:
   1. The DataFrame contains only the columns that you specified in part 1.
   2. The columns contain the correct data type
   3. There are at least 10 rows in the DataFrame.
    """
    if len(df.columns) < 3:
        print("Dataframe has less than three columns")
        return False

    df_cols = ["PermitClass", "PermitTypeDesc", "EstProjectCost"]
    check = df.columns == df_cols
    if not all(check):
        print("Column names not the same")
        return False

    rows = np.size(df, 0)
    if rows < 10:
        print("Fewer than ten rows")
        return False

    if permits["PermitClass"].dtype != object:
        print("PermitClass wrong data type")
        return False
    elif permits["PermitTypeDesc"].dtype != object:
        print("PermitTypeDesc wrong data type")
        return False
    elif permits["EstProjectCost"].dtype != float:
        print("EstProjectCost wrong data type")
        return False
    else:
        return True

"""A simple check to show the function can work"""
test_create_dataframe(permits)
