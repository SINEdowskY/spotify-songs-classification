def get_genres():
    def file_open(fn):
        try:
            file = open(fn, 'r')
            return file.readlines()
        except IOError:
            print('file doesnt exist')
            return 0

    genres = file_open('spotify-genres.md')
    genres = genres[4:len(genres)]
    for i in range(len(genres)):
        genres[i] = genres[i].replace('1. ', '').replace('\n', '')

    return genres

