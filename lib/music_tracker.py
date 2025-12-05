class MusicTracker():
    def __init__(self):
        self.music_list = []

    def add_tracks(self, new_track):
        if new_track == "":
            return "Please enter a track"
        self.music_list.append(new_track)

    def list_tracks(self):
        return self.music_list