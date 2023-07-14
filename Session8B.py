from Session8A import Song, PlayList


def main():
    play_list = PlayList()
    print("PlayList:", play_list, vars(play_list))

    song1 = Song(track="1. Udd Jaa Kaale Kaava", artists="Udit Narayan, Alka Yagnik", duration=4.48)
    play_list.append(song=song1)

    print("PlayList:", play_list, vars(play_list))

    song2 = Song(track="2. Gustakhiyan", artists="Gurnam Bhullar", duration=3.5)
    play_list.append(song=song2)

    song3 = Song(track="3. Desperado", artists="Raghav, Tesher", duration=5.6)
    play_list.append(song=song3)

    play_list.append(
        song=Song(track="4. Chorni", artists="DIVINE, Sidhu Moose Wala", duration=4.12)
    )

    play_list.append(song=Song(track="5. Kasol", artists="Mani Longia, Starboy X", duration=2.28))

    print("PlayList:", play_list, vars(play_list))

    print("PRINTING PLAYLIST - FORWARD")
    play_list.iterate()

    print("PRINTING PLAYLIST - BACKWARD")
    play_list.iterate(1)


if __name__ == "__main__":
    main()