import pandas as pd
import numpy as np
from env import get_db_url

def get_data_from_mysql():
    query = """
    SELECT  bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet AS sqft, taxvaluedollarcnt AS tax_value
    FROM properties_2017
    JOIN predictions_2017 USING (id)
    JOIN propertylandusetype USING (propertylandusetypeid)
    WHERE (transactiondate  >='2017-05-01' AND transactiondate <= '2017-06-30') AND propertylandusetypeid = '261';
    """
    df = pd.read_sql(query, get_db_url("zillow"))
    return df


def wrangle_zillow():
    df = get_data_from_mysql()
    df.total_charges = df.total_charges.str.strip().replace('', np.nan).astype(float)
    df = df.dropna() 
    return df
   
def wrangle_grades():
    grades = pd.read_csv("student_grades.csv")
    grades.drop(columns="student_id", inplace=True)
    grades.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    df = grades.dropna().astype("int")
    return df