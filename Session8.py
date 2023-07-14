"""
    Circular Doubly Linked List
"""


class Song:

    def __init__(self, track, artists, duration):
        self.track = track
        self.artists = artists
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.track)
        print(self.artists)
        print(self.duration)
        print("CURRENT:", self, "NEXT:", self.next, "PREVIOUS:", self.previous)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    song1 = Song(track="1. Udd Jaa Kaale Kaava", artists="Udit Narayan, Alka Yagnik", duration=4.48)
    song2 = Song(track="2. Gustakhiyan", artists="Gurnam Bhullar", duration=3.5)
    song3 = Song(track="3. Desperado", artists="Raghav, Tesher", duration=5.6)
    song4 = Song(track="4. Chorni", artists="DIVINE, Sidhu Moose Wala", duration=4.12)
    song5 = Song(track="5. Kasol", artists="Mani Longia, Starboy X", duration=2.28)

    """
    print("song1:", song1)
    print("song2:", song2)
    print("song3:", song3)
    print("song4:", song4)
    print("song5:", song5)
    """


    # HardCode
    # Reference Copy :)
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song5
    song5.next = song1

    song1.previous = song5
    song2.previous = song1
    song3.previous = song2
    song4.previous = song3
    song5.previous = song4

    """
    print("song1 data:", vars(song1))
    print("song2 data:", vars(song2))
    print("song3 data:", vars(song3))
    print("song4 data:", vars(song4))
    print("song5 data:", vars(song5))
    """

    print("Printing the Linked Song Objects :)")
    print("Iterating in Forward Direction...")
    temp = song1
    while True:
        temp.show()
        temp = temp.next

        if temp == song1:
            break

    print("Iterating in Backward Direction...")
    temp = song5
    while True:
        temp.show()
        temp = temp.previous

        if temp == song5:
            break


if __name__ == "__main__":
    main()