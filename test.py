from IPython.display import display
import pandas as pd

# creating a DataFrame
dict = {'Products': ['Intel Dell Laptops', 'HP Laptops', 'Lenavo Laptops', 'Acer Laptops'],
        'Price dollar': [350, 300, 400, 250],
        'Percentage Sale': [83, 99, 84, 76]}
dataframe = pd.DataFrame(dict)

# displaying the DataFrame
print(dataframe)