###################################################
#                                                 #
#   set the default browser to chrome/mozilla     #
#                                     firefox     #
#   need to login first to your account           #
#   can only change the tracks (cannot play a     #
#           track without pushing play button)    #
#                                                 #
###################################################

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser
    
username = 'priyankadey'
correlation = 0.45
something = ''

client_credentials_manager = SpotifyClientCredentials(client_id='d784e038a57d4b329a5ec538f56a8ad4',client_secret='b14a43b4233e44fd89fd21ae76f372b5')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

drake = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
spotify_url_pref = 'https://open.spotify.com/track/'
track = ''
drakeStuff = []

results = sp.artist_top_tracks(drake)

for track in results['tracks'][:10]:
    tck = spotify_url_pref + track['id']
    drakeStuff.append(tck)

correlation = float(input('What is the correlation??'))

if (0 <= correlation < 0.2) :
    something = drakeStuff[9]
if (0.2 <= correlation < 0.3) :
    something = drakeStuff[8]
if (0.3 <= correlation < 0.4) :
    something = drakeStuff[7]
if (0.4 <= correlation < 0.5) :
    something = drakeStuff[6]
if (0.5 <= correlation < 0.6) :
    something = drakeStuff[5]
if (0.6 <= correlation < 0.7) :
    something = drakeStuff[4]
if (0.7 <= correlation < 0.8) :
    something = drakeStuff[3]
if (0.8 <= correlation < 0.9) :
    something = drakeStuff[2]
if (0.9 <= correlation < 1) :
    something = drakeStuff[1]
if (correlation == 1) :
    something = drakeStuff[0]

webbrowser.open(something)

