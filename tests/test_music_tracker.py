from lib.music_tracker import *
import pytest

"""
On initalising the class
The empty list is created
"""

def test_music_list_created_on_init():
    music_tracker = MusicTracker()
    assert music_tracker.music_list == []

"""
Adding a track using add_tracks
Track is added to self.music_list
"""

def test_add_track_adds_to_music_list():
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Sonne")
    assert music_tracker.music_list == ["Sonne"]
    music_tracker.add_tracks("Victory Lap 5")
    assert music_tracker.music_list == ["Sonne", "Victory Lap 5"]

