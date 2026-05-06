"""
Exercise 1: Playlist Manager
File: 01_playlist_manager.py

Rules:
1. Create a list called 'playlist' with 3 song names (strings).
2. A new hit just dropped! Use .append() to add a new song to the end of the list.
3. You want a specific song to play first. Use .insert() to add a song at index 0.
4. You got tired of one of the original songs. Use .remove() to delete it by its exact name.
5. The last song finished playing. Use .pop() to remove the last song and save it to a variable called 'played_song'.
6. Print: "Just played: [played_song]".
7. Print the final state of the 'playlist' list.
"""

# 1. Create a list called 'playlist' with 3 song names (strings).
playlist = ["Off To The Races","The Abyss","Gethshame"]
print(f"Initial Playlist: {playlist}")

# 2. A new hit just dropped! Use .append() to add a new song to the end of the list.
playlist.append("Pink Matter")
print(f"Playlist after adding the new song: {playlist}")

# 3. You want a specific song to play first. Use .insert() to add a song at index 0.
playlist.insert(0,"God is a Woman")
print(f"Playlist after adding the song at index 0: {playlist}")

# 4. You got tired of one of the original songs. Use .remove() to delete it by its exact name.
playlist.remove("The Abyss")
print(f"Playlist after removed the song \"The Abyss\" from the playlist: {playlist}")

# 5. The last song finished playing. Use .pop() to remove the last song and save it to a variable called 'played_song'.
played_song = playlist.pop()
print(f"Playlist after using .pop() to remove the last song: {playlist}")

# 6. Print: "Just played: [played_song]".
print(f"Just played: {played_song}")

# 7. Print the final state of the 'playlist' list.
print(f"Final state of the playlist: {playlist}")


