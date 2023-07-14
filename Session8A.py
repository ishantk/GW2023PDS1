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


class PlayList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, song):

        self.size += 1

        if self.head is None:
            self.head = song
            self.tail = song
        else:
            self.tail.next = song
            song.previous = self.tail

            # Any newly added song will be tail :)
            self.tail = song

            # CIRCULAR
            self.head.previous = self.tail
            self.tail.next = self.head

    def iterate(self, direction=0):

        if direction == 0:
            temp = self.head
            while True:
                temp.show()
                temp = temp.next

                if temp == self.head:
                    break
        else:
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous

                if temp == self.tail:
                    break

    # Weekend Assignment

    # Add at head
    def insert(self):
        pass

    # Delete the Song Object
    def delete(self, track):
        pass

