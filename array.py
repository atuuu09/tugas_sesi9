import array as arr
print("NO 1")
arr = [8, 3, 12, 4, 7, 2]
output_arr = []
# menghapus semua angka kurang dari 5 dan menggantinya dengan nilai 0
for i in arr:
    if i <= 5:
        output_arr.append(0)
    else:
        output_arr.append(i)
# mengurutkan nilaimterbesar ke terkecil
output_arr.sort(reverse=True)
print(output_arr)  

print("NO 2")
arr = [7, 4, 9, 2, 5, 1]
output_arr = []
# menghapus nilai bilangan ganjil dan mengurutkan nilai tersebut dari terkecil ke terbesar
for i in arr:
    if i % 2 == 0:
        output_arr.append(i)

output_arr.sort()
print(output_arr)

print("NO 3")
kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []
# menghapus kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata tersebut secara alfabetis
for i in kata:
    if len(i) >= 5:
        output.append(i)

output.sort()
print(output)

print("NO 4")
list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]
# menggabungkan kedua list tersebut dan menghapus semua buah yang sama dan mengurutkan sisa buah-buahan secara alfabetis.
hasil = sorted(set(list1 + list2))
print(hasil)

print("NO 5")
input_arr = [105, 20, 8, 150, 30, 5, 200]
output_arr = []
# menghapus nilai yang kurang dari 10 dan lebih dari 100
for i in input_arr:
    if 10 <= i <= 100:
        output_arr.append(i)

# mengurutkan sisa nilai tersebut dari terkecil ke terbesar
output_arr.sort()
print(output_arr)

