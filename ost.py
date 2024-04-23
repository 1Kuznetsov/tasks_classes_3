import threading
import time


class Album:
    def __init__(self, title, artist, year):
        """
        Sets all the necessary attributes for the class Album
        :param title:
        :param artist:
        :param year:
        """

        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        self.current_track_index = 0

    def add_track(self, track):
        """
        Method of adding the track
        :param track:
        :return:
        """

        self.tracks.append(track)

    def play(self):
        """
        Method of playing the track
        :return:
        """

        self.tracks[self.current_track_index].play()

        next_track_start_time = time.time() + self.tracks[self.current_track_index].duration
        self.next_track_timer = threading.Timer(next_track_start_time - time.time(), self.play_next_track)
        self.next_track_timer.start()

    def play_next_track(self):
        """
        Method of playing the next track
        :return:
        """

        self.tracks[self.current_track_index].stop()

        self.current_track_index += 1

        if self.current_track_index < len(self.tracks):
            self.tracks[self.current_track_index].play()

            next_track_start_time = time.time() + self.tracks[self.current_track_index].duration
            self.next_track_timer = threading.Timer(next_track_start_time - time.time(), self.play_next_track)
            self.next_track_timer.start()

    def pause(self):
        """
        Method of pausing the track
        :return:
        """

        self.tracks[self.current_track_index].pause()

        self.next_track_timer.cancel()

    def stop(self):
        """
        Method of stopping the next track
        :return:
        """

        self.tracks[self.current_track_index].stop()

        self.next_track_timer.cancel()


class Track:
    """
    Class representing the track
    """

    def __init__(self, title, artist, duration):
        """
        Sets all the necessary attributes for the class Track
        :param title:
        :param artist:
        :param duration:
        """

        self.title = title
        self.artist = artist
        self.duration = duration
        self.is_playing = False

    def play(self):
        """
        Method of playing the track in separate flow
        :return:
        """

        self.is_playing = True
        self.play_thread = threading.Thread(target=self._play)
        self.play_thread.start()

    def _play(self):
        """
        Method of playing the track
        :return:
        """

        time.sleep(self.duration)
        self.is_playing = False

    def pause(self):
        """
        Method of pausing the track
        :return:
        """

        self.is_playing = False

    def stop(self):
        """
        Method of stopping playing the track
        :return:
        """

        self.is_playing = False
