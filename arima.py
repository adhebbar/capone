import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#data = pd.read_csv("smithK.csv")
def predict(purchaseData, weeks):
	purchaseData.iloc[:,0] = pd.to_datetime(purchaseData.iloc[:,0])
	resampled_data = purchaseData.resample("W", on="Posted Date").sum()
	y = resampled_data
	y = y.fillna(y.bfill())
	mod = sm.tsa.statespace.SARIMAX(y,
	                                order=(1, 1, 1),
	                                seasonal_order=(1, 1, 1, 12),
	                                enforce_stationarity=False,
	                                enforce_invertibility=False)

	results = mod.fit()

	# Get forecast 500 steps ahead in future
	pred_uc = results.get_forecast(steps=weeks)

	# Get confidence intervals of forecasts
	pred_ci = pred_uc.conf_int()
	pred_uc.prediction_results.end
	return pred_uc.predicted_mean