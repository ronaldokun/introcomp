#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:54:30 2016

@author: ronaldo
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name, song_len, song_size)
    max_size: float, maximum size of total songs that you can fit
    
    Start with the song first in the 'songs' list, then pick the next song to
    be the one with the lowest file size not already picked, repeat
    
    Returns: a list of a subset of songs fitting in 'max_size' in the order
    in which they were chosen.
    
    """
    
    orderedSongs = sorted(songs, key = lambda x: x[2])
    
    songList = []

    #add the first song    
    if songs[0] in songList:
        
        orderedSongs.remove(songs[0])
        
    elif songs[0][2] <= max_size:
            
        songList.append(songs[0][0])
        max_size -= songs[0][2]
        orderedSongs.remove(songs[0])
        
    else:
        return songList

    for song in orderedSongs:
        if song in songList:
            next
        elif song[2] <= max_size:
            
            songList.append(song[0])
            
            max_size -= song[2]

        else:
            
            return songList
            
    else:
        return songList
        
songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), \
         ('Wannabe', 2.7, 1.2)]

max_size = 20

print(song_playlist(songs, max_size))
    
            