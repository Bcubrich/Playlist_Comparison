# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:07:49 2019

@author: bcubrich
"""

import pandas as pd
import numpy as np         #didn't even use numpy!!! HA!
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib_venn import venn2



def get_dat(text):
    root = Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost", True)      #makes the dialog appear on top
    filename = askopenfilename(title=text)      # Open single file
    root.destroy()
    root.quit()
    return filename



playlist1_file=get_dat('Playlist 1')

playlist2_file=get_dat('Playlist 2')

#playlist1_file='U:/PLAN/BCUBRICH/Python/Tests/playlist comparison/MoreBadPopPunk.csv'
#
#playlist2_file='U:/PLAN/BCUBRICH/Python/Tests/playlist comparison/Blairvis and Barthead Do America.csv'

playlist1_name=playlist1_file.split('/')[-1].split('.')[0]
playlist2_name=playlist2_file.split('/')[-1].split('.')[0]

playlist1=pd.read_csv(playlist1_file)
playlist2=pd.read_csv(playlist2_file)

artists1=playlist1.drop_duplicates(subset=['artist']).copy()
artists2=playlist2.drop_duplicates(subset=['artist']).copy()

artists_in_common=pd.merge(artists1,artists2,on='artist')
songs_in_common=pd.merge(playlist1,playlist2,on=['artist', 'track'],how='inner').drop_duplicates()


playlist1_artist_similarity=len(artists_in_common)/len(artists1)*100
playlist2_artist_similarity=len(artists_in_common)/len(artists2)*100
playlist1_song_similarity=len(songs_in_common)/len(playlist1)*100
playlist2_song_similarity=len(songs_in_common)/len(playlist2)*100

total_artists=len(pd.merge(artists1,artists2,on='artist',how ='outer'))
total_songs=len(pd.merge(playlist1,playlist2,on=['artist', 'track'],how='outer'))

print ('{} vs {}'.format(playlist1_name,playlist2_name))
print('-{:.2f}% of artists in {} are in {}'.format(playlist1_artist_similarity,playlist1_name,playlist2_name))
print('-{:.2f}% of artists in {} are in {}'.format(playlist2_artist_similarity,playlist2_name,playlist1_name))
print('-{:.2f}% of songs in {} are in {}'.format(playlist1_song_similarity,playlist1_name,playlist2_name))
print('-{:.2f}% of songs in {} are in {}'.format(playlist2_song_similarity,playlist2_name,playlist1_name))
print('-Of the {} artists in both playlists there are {} artists in common'.format(total_artists,len(artists_in_common)))
print('-Of the {} songs in both playlists there are {} songs in common'.format(total_songs,len(songs_in_common)))
print('-The songs in common are the following:{}'.format(songs_in_common))

# First way to call the 2 group Venn diagram:
def plot_ven(a,b,ab,title):
    plt.figure()
    venn2(subsets = (len(a), len(b), len(ab)), set_labels = (playlist1_name,playlist2_name))
    plt.title(title)
    plt.show()

plot_ven(playlist1,playlist2,songs_in_common, 'Song Similarity')

plot_ven(artists1,artists2,artists_in_common, 'Artist Similarity')
