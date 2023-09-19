class Album:

    GENRES = ["Hip-Hop", "Pop", "Jazz"]
    album_count = 0

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

mine=Album('pop',24)
print(mine.GENRES)
print(mine.album_count)


mine=Album('pop',24)
Album.GENRES='pop'
print(Album.GENRES)
print(Album.album_count)