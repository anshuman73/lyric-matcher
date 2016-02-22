# Copyright Anshuman73.
# Visit anshuman73.github.io for more info.
# Released under MIT License.
# Works with Python 2.7

import json
import urllib

def main(query):
	#get the data
	raw_data = urllib.urlopen("https://www.musixmatch.com/search/" + str(query)).readlines()[30]
	#Data has some HTML, parse it to make it perfect json
	raw_data = raw_data[raw_data.find('{') : raw_data.rfind('}') + 1]
	data = json.loads(raw_data) #Ready to query data
	song =  data['allResults']['bestMatch']['attributes']['track_name']
	artist = data['allResults']['bestMatch']['attributes']['artist_name']
	album = data['allResults']['bestMatch']['attributes']['album_name']

	print "\n\nSong Name:", song
	print "\nArtist:", artist
	print "\nAlbum:", album


main(str(raw_input("Enter the lyrics: \n\n")))
