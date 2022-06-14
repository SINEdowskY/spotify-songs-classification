import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import plot

x = pd.read_csv('new_data.csv')
x.drop('Unnamed: 0', inplace=True, axis=1)



with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    y = x.groupby(['genre'])
    print('mean:', y.mean())
    print('median: ', y.median())
    print('min:', y.min())
    print('max:', y.max())
