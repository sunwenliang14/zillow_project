import pandas as pd
from math import sqrt
from scipy import stats
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.feature_selection import RFE
import sklearn.linear_model
import warnings
warnings.filterwarnings("ignore")
import split_scale

def linear_model(X_train,y_train):
    lm = LinearRegression().fit(X_train,y_train)
    lm_y_intercept = lm.intercept_
    lm_coefficients = lm.coef_

    