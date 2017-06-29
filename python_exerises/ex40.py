class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

yellowLyric = """
Look at the stars
Look how they shine for you
And everything you do
Yeah they were all yellow1

I came along
I wrote a song for you
And all the things you do
And it was called yellow

So then I took my turn
Oh what a thing to have done
And it was all yellow
"""

yellow = Song([yellowLyric])

yellow.sing_me_a_song()
