print("~~~ Tabel Matematika Nich ~~~")
print("pilihlah Model Matematika \n1. Perkalian \n2. Pembagian")
int(input("Masukkan Model Matematika yang di inginkan 1/2 :"))

num = int(input("Menampilkan Tabel Matematika yang di inginkan "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


