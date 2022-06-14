from knn import KNN
from spotify_data import SpotifyData
import pandas as pd
genres = [
    'rap', 'rock', 'metal', 'classical', 'disco polo', 'r&b', 'punk', 'pop'
]


#query = 'patoprohibicja'
query = input("Podaj tytul piosenki: ")
spot = SpotifyData()

#x = spot.get_data(genres)
#pd.DataFrame.to_csv(x, 'new_data.csv')
prediction = spot.get_one_song_data(query)
data = pd.read_csv('new_data.csv')

classi = KNN(prediction=prediction, data=data, n=7)
print(classi.accuracy)
classi.plot()

print('Predykcja: ', classi.predi)

