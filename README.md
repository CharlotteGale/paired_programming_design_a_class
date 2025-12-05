# Music Tracker

## User Stories
> As a user     
> So that I can keep track of my music listening    
> I want to add tracks I've listened to and see a list of them.

## Class Interface
```python
class MusicTracker():
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side Effects:
        #   None
        # Internal State:
        #   Initalise empty list on initialization
        #       self.music_list = []
        pass

    def add_tracks(self, new_track):
        # Parameters:
        #   new_track: string
        # Returns:
        #   None
        # Side Effects:
        #   Updates self.music_list
        # Internal State:
        #   - returns a warning if string is empty
        #   - raises TypeError if new_track not string
        pass

    def list_tracks(self):
        # Parameters:
        #   None
        # Returns:
        #   A list
        # Side Effects:
        #   None
        # Internal State:
        #   None
        pass
    
```

## Tests
```python
"""
On initalising the class
The empty list is created
"""
    music_tracker = MusicTracker()
    assert music_tracker.music_list == []
```
```python
"""
Adding a track using add_tracks
Track is added to self.music_list
"""
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Sonne")
    assert music_tracker.music_list == ["Sonne"]
    music_tracker.add_tracks("Victory Lap 5")
    assert music_tracker.music_list == ["Sonne", "Victory Lap 5"]

```
```python
"""
Calling list_tracks
Returns a list
"""
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Sonne")
    music_tracker.add_tracks("Victory Lap 5")
    assert music_tracker.list_tracks() == ["Sonne", "Victory Lap 5"]

"""
Given empty string when adding tracks
Returns warning "Track cannot be empty
"""
    music_tracker = MusicTracker()
    assert music_tracker.add_tracks("") == "Please enter a track"

"""
Given wrong type as new track
Raises TypeError
"""
    music_tracker = MusicTracker()
    with pytest.raises(TypeError) as e:
        music_tracker.add_tracks(1334)
    error_message = str(e.value)
    assert error_message == "Please enter valid string"
