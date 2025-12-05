"""
On initalising the class
The empty list is created
"""

def test_music_list_created_on_init():
    music_tracker = MusicTracker()
    assert music_tracker.music_list == []