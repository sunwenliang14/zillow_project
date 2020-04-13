import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from env import get_db_url

def acquire_zillow():
    query = """
    SELECT  bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet AS sqft, taxvaluedollarcnt AS tax_value, fips,taxamount 
    FROM properties_2017
    JOIN predictions_2017 USING (id)
    JOIN propertylandusetype USING (propertylandusetypeid)
    WHERE (transactiondate  >='2017-05-01' AND transactiondate <= '2017-06-30') AND propertylandusetypeid = '261'
    AND taxvaluedollarcnt <= 1000000;"""
    
    df = pd.read_sql(query, get_db_url("zillow"))
    return df

