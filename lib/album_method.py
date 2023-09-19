class Album:
    count=0
    def __init__(self,date):
        self.release_date=date
        self.increase_album_count()
        

    @classmethod
    def increase_album_count(cls):
        cls.count +=1

album=Album(1996)
print(album.count)

album=Album(1996)
print(album.count)
