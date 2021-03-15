def find_median(sorted_list):
    indices = []

    list_size = len(sorted_list)
    median = 0

    if list_size % 2 == 0:
        indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))

        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2

    else:
        indices.append(int(list_size / 2))

        median = sorted_list[indices[0]]


    return median, indices
samples = list(i for i in input("Masukkan Angka : ").split(','))
samples1 = [int(j) for j in samples]
median, median_indices = find_median(samples1)
Q1, Q1_indices = find_median(samples1[:median_indices[0]])
Q3, Q3_indices = find_median(samples1[median_indices[-1] + 1:])

quartiles = [Q1, median, Q3]
iqr=Q3-Q1
print("(Q1, median, Q3): {} dan %d".format(quartiles)%iqr)