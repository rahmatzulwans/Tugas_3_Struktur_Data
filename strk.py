print ("NAMA  : RAHMAT ZULWAN S")
print ("NIM   : E1E1 19 010")
print ("KELAS : GENAP")
print ("   ")
print ("   ")


print ("Menu Pilihan Papan Scoreboad")
print ("   ")

print ("1. Tampilkan list_data")
print ("2. Input Data Baru")
print ("   ")


pilih = int(input("Masukkan pilihan yang anda mau : "))
if pilih==1:
    data = print("Nama         score         time")
    data_baru_1 = print("Rahmat         3         30 menit")
    data_baru_2 = print("Asril          4         40 menit")
    data_baru_3 = print("Mirza          5         50 menit")
elif pilih==2:
    print ("Masukkan Nama, Score, Time")
    data_1 = (input("Masukkan nama : "))
    data_2 = int(input("Masukkan score : "))
    data_3 = (input("Masukkan time : "))
    data = print("Nama         score         time")
    data_baru_1 = print("Rahmat         3         30 menit")
    data_baru_2 = print("Asril          4         40 menit")
    data_baru_3 = print("Mirza          5         50 menit")
    print(data_1,"       ", data_2, "       ",data_3)
else:
    print("pilihan menu yang anda masukkan tidak ada di option")




    
    
    
    
    
    
