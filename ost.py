import time


class Album:
    def __init__(self, id, name, artist, year, tracks):
        self.id = id
        self.name = name
        self.artist = artist
        self.year = year
        self.tracks = tracks


class Track:
    def __init__(self, id, name, duration, artist, album):
        self.id = id
        self.name = name
        self.duration = duration
        self.artist = artist
        self.album = album

    def play(track):
        print(f"Воспроизводится трек: {track.name}")
        time.sleep(track.duration)

    def pause(track):
        print(f"Трек {track.name} поставлен на паузу")

    def stop(track):
        print(f"Воспроизведение трека {track.name} остановлено")

    def get_duration(track):
        return track.duration

    def get_artist(track):
        return track.artist
