#Soal:
# harga tiket 25 dollar
# orang orang akan bayar diantara 25,50,100
# Vasya tanpa modal
# Beri output yes jika vasya bisa menjual
# Beri output no jika vasya tidak bisa menjual

def tiket(antrian):
	vasya_dollar25 = 0 
	vasya_dollar50 = 0
	for bayar in antrian:
		print("Sebelum transaksi\nUang $25= {} lembar dan Uang $50= {} lembar".format(vasya_dollar25,vasya_dollar50))
		print("Uang masuk: ${}".format(bayar))
		if(bayar==25):
			vasya_dollar25+=1
		elif(bayar==50):
			vasya_dollar25-=1
			vasya_dollar50+=1
		elif(bayar==100):
			if(vasya_dollar50>0):
				vasya_dollar50-=1
				vasya_dollar25-=1
			else:
				vasya_dollar25-=3
		if(vasya_dollar25<0 or vasya_dollar50 <0):
			print("Uang kembalian tidak cukup")
			return "NO"
		print("Setelah transaksi\nUang $25= {} lembar dan Uang $50= {} lembar\n".format(vasya_dollar25,vasya_dollar50))
	return "YES"

# print(tiket([25,25,50]))
#$25=1 -> $25=2 -> $50=1 dan $25=1 maka jawabannya YES
# print(tiket([25,100]))
# #$25=1 -> $100 tidak bisa kembalian karena jumlah uang yang ada tidak cukup maka jawabannya NO
# print(tiket([25,25,50,50,100]))
#$25=1 -> $25=2 -> $50=1 dan $25=1 -> $50=2 dan $25=0 -> 
#$100 tidak bisa kembalian karena jumlah uang yang ada tidak cukup-->$25=0
#maka jawabannya NO 
