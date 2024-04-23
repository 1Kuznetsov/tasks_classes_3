from ost import Album, Track
import time

album = Album('.5: The Gray Chapter', 'Slipknot', 2014)
album.add_track(Track('XIX', 'Slipknot', 190))
album.add_track(Track('Sarcastrophe', 'Slipknot', 306))
album.add_track(Track('AOV', 'Slipknot', 332))
album.add_track(Track('The Devil in I', 'Slipknot', 342))
album.add_track(Track('Killpop', 'Slipknot', 225))
album.play()

time.sleep(6)
album.pause()

album.play()

album.stop()
