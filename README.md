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

