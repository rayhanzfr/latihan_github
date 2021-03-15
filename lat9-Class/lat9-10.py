class Playlist:
	def __init__(self,daftar_lagu):
		self.daftar_lagu = daftar_lagu
		self.current_position = 0  
  
	def __switch_to_song(self,to_index):
		last_pos = len(self.daftar_lagu) - 1
		if to_index > last_pos: # geser ke lagu awal
			self.current_position = 0
		elif to_index < 0: # geser ke lagu terakhir
			self.current_position = last_pos
		else: # putar sesuai index
			self.current_position = to_index 
		lagu = self.daftar_lagu[self.current_position]
		print('Memutar: {} oleh {}'.format(lagu.judul,lagu.penyanyi))  

	def play_first_song(self):
		self.__switch_to_song(0)  
	def play_last_song(self):
		last_pos = len(self.daftar_lagu) - 1
		self.__switch_to_song(last_pos)	
	def play(self):
		self.__switch_to_song(self.current_position)
	def play_next_song(self):
		self.__switch_to_song(self.current_position+1)
	def play_prev_song(self):
		self.__switch_to_song(self.current_position-1)
class Lagu:
	def __init__(self,judul,penyanyi):
		self.judul = judul
		self.penyanyi = penyanyi
song1 = Lagu('Kalau Sang Surya Tenggelam','Erwin Gutawa feat Synch Stage Orchestra-Vienna')
song2 = Lagu('Itsumo Nando Demo','Dazbee Cover') 
song3 = Lagu('Dreams','The Cranberries') 
song4 = Lagu('One Summer\'s Day','Joe Hisaishi') 
song5 = Lagu('Kala Tangan dan Kaki Berkata','Chrisye')
pl = Playlist([song1,song2,song3,song4,song5])
stop = False
while not stop:
	konfirm = input('tekan g (play), f (first), n (next), p (prev), l (last), lainnya (stop) kemudian ENTER \n')
	if konfirm == 'g':
		pl.play()
	elif konfirm == 'f':
		pl.play_first_song()
	elif konfirm == 'n':
		pl.play_next_song()
	elif konfirm == 'p':
		pl.play_prev_song()
	elif konfirm == 'l':
		pl.play_last_song()
	else:    
		stop = True
		print('Pemutar lagu dihentikan')