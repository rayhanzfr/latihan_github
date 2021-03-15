# Langkah:
	# mendefinisikan item
	# jumlah angka yang ada pada list
	# jumlah page
	# angka dari item di page sekarang. page_index dihitung dari 0
	# method ini harus return -1 untuk values dari page_index yang tidak masuk ukuran
	# memutuskan halaman mana item tersebut ditempatkan. index dimulai dari 0.
	# method ini harus return -1 untuk values dari page_index yang tidak masuk ukuran
import math
class PaginationHelper:
	def __init__(self, list, page):
			self.list = list
			self.page = page
	def item_count(self):
			return len(self.list)
	def page_count(self):
			return int(math.ceil(self.item_count() / self.page))			
	def page_item_count(self,page_index):
			if (page_index+1) * self.page <= self.item_count():
					return self.page
			if page_index*self.page<self.item_count() and (page_index+1) * self.page > self.item_count():
					return self.item_count()%self.page
			return -1
	def page_index(self,item_index):
			if item_index < self.item_count() and item_index >= 0 :
					return item_index//self.page
			return -1
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # should == 2
print(helper.item_count())# should == 6
print(helper.page_item_count(0)) # should return 4
print(helper.page_item_count(1)) # last page – should return 2
print(helper.page_item_count(2)) # should return -1 since the page is invalid
# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should return 1 (zero based index)
print(helper.page_index(2)) # should return 0
print(helper.page_index(20)) # should return -1
print(helper.page_index(-10)) # should return -1 because negative indexes are invalid