import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#checking for NaN values

def check_na(dataframe):
    print(dataframe.shape)
    print (dataframe.isna().sum())

#change our dataframe to read as df

df = pd.Dataframe(data)

#then make sure to have a date column

df['date'] = pd.to_datetime(df['date'], format='%d/%b/%Y:%H:%M:%S +0000', utc = True)

#Ones and zeros from the assignment

ONES = pd.Dataframe(np.ones(10))
ZEROS = pd.Dataframe(np.zeros(20))



