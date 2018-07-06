class Song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_asong(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([
    "happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "There rally around the family",
    "wiht pockets full of shells"
])


happy_bday.sing_me_asong()

bulls_on_parade.sing_me_asong()