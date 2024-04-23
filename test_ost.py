from ost import Album, Track
import time

album = Album(1, '.5: The Gray Chapter', 'Slipknot', 2014, [])
track1 = Track(1, 'XIX', 190, 'Slipknot', album)
track2 = Track(2, 'Sarcastrophe', 220, 'Slipknot', album)

album.tracks.append(track1)
album.tracks.append(track2)

while True:
    command = input("Введите команду (play, pause, stop, quit): ")
    if command == "play":
        track_name = input("Введите название трека: ")
        track = next((track for track in album.tracks if track.name == track_name), None)
        if track:
            track.play()
        else:
            print("Трек не найден")
    elif command == "pause":
        track_name = input("Введите название трека: ")
        track = next((track for track in album.tracks if track.name == track_name), None)
        if track:
            track.pause()
        else:
            print("Трек не найден")
    elif command == "stop":
        track_name = input("Введите название трека: ")
        track = next((track for track in album.tracks if track.name == track_name), None)
        if track:
            track.stop()
        else:
            print("Трек не найден")
    elif command == "quit":
        break
    else:
        print("Неизвестная команда")