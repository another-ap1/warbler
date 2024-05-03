from models import Playlist, Song, PlaylistSong,db, connect_db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

#playlists
playlist1 = Playlist(name = 'Grant', description = 'grants jams')
playlist2 = Playlist(name = 'Charlotte', description = 'charlottes jams')
playlist3 = Playlist(name = 'Emilia', description = 'Emilias jams')
playlist4 = Playlist(name = 'Alicia', description = 'alicias jams')

#songs
song1 = Song(title='ohio is for lovers', artist = 'hawthorn heights')
song2 = Song(title='discovering the water front', artist = 'silverstein')
song3 = Song(title='homesick', artist = 'ADTR')
song4 = Song(title='Swords dragons diet coke', artist = 'TDWP')
song5 = Song(title='December underground', artist = 'AFI')
song6 = Song(title='Equip sunglasses', artist = 'hot mulligan')
song7 = Song(title='into the hallow', artist = 'knocked loose')
song8 = Song(title='alone with you', artist = 'in her own words')
song9 = Song(title='grinding teath', artist = 'youth fountain')

db.session.add([playlist1, playlist2, playlist3, playlist4])
db.session.add([song1, song2, song3, song4, song5, song6, song7, song8, song9 ])
db.session.commit()



