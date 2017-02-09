# Copyright Anshuman73.
# Visit anshuman73.github.io for more info.
# Released under MIT License.
# Works with Python 2.7

import json
import requests

def main(query):
	#get the data
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/53.0.2785.116 Safari/537.36'}
	raw_data = requests.get("https://www.musixmatch.com/search/%s/lyrics" % query, headers=headers).text.encode('utf-8')
	#raw_data is now a HTML dump, parse it to make it perfect json
	raw_data = raw_data[raw_data.find('{', raw_data.find('mxmProps')) : raw_data.find('</script>', raw_data.find('mxmProps'))]
	data = json.loads(raw_data) # Data ready to be queried
	
	total_results = data['lyricsTracks']['length']
	
	print "Top 5 results are:\n"
	
	for x in xrange(5):
		song =  data['lyricsTracks'][str(x)]['attributes']['track_name']
		artist = data['lyricsTracks'][str(x)]['attributes']['artist_name']
		album = data['lyricsTracks'][str(x)]['attributes']['album_name']
		
		print "\n\nSong Name:", song
		print "\nArtist:", artist
		print "\nAlbum:", album

main(str(raw_input("\nEnter the lyrics: \n\n")))
