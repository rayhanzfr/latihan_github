def n_lower_char(string):
    return sum(map(str.islower, string))
def n_upper_char(string):
	return sum(map(str.isupper, string))
string = input("Masukkan kata: ")
print("Kapital: ",n_lower_char(string))
print("Tidak Kapital: ",n_upper_char(string))