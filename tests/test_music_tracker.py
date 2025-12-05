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

"""
Calling list_tracks
Returns a list
"""

def test_returns_list():
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Sonne")
    music_tracker.add_tracks("Victory Lap 5")
    assert music_tracker.list_tracks() == ["Sonne", "Victory Lap 5"]

"""
Given empty string when adding tracks
Returns warning "Track cannot be empty
"""

def test_empty_string_as_new_track():
    music_tracker = MusicTracker()
    assert music_tracker.add_tracks("") == "Please enter a track"

"""
Given wrong type as new track
Raises TypeError
"""

def test_raise_type_error_with_wrong_type():
    music_tracker = MusicTracker()
    with pytest.raises(TypeError) as e:
        music_tracker.add_tracks(1334)
    error_message = str(e.value)
    assert error_message == "Please enter valid string"