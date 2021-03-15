import numpy
np = numpy
del numpy
def mean(data):
    total = 0
    for number in data:
        total += number
    return total / len(data)

def std_dev(data):
    temp = 0
    for number in data:
        temp += (number - mean(data)) ** 2
    return (temp / len(data)) ** 0.5

def covariance(x,y):
    temp = 0
    for i in range(len(x)):
        temp += (x[i] - mean(x)) * (y[i] - mean(y))
    return temp / len(x) 

def correlation(x,y):
    return covariance(x,y) / (std_dev(x) * std_dev(y))


x = list(np.random.randint(0,20,10))
y = list(np.random.randint(0,20,10))

print("\nPopulasi X")
print(f"Data            : {x}")
print(f"Rata-rata       : {mean(x)}")
print(f"Standar deviasi : {std_dev(x)}")

print("\nPopulasi Y")
print(f"Data            : {y}")
print(f"Rata-rata       : {mean(y)}")
print(f"Standar deviasi : {std_dev(y)}")

print(f"\nCovariance X dan Y    : {covariance(x,y)}")
print(f"Correlation X dan Y   : {correlation(x,y)}\n")
