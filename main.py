# Barang yang dapat di input
barang_jualan = {
    "ayam" : 19000,
    "roti" : 5000,
    "telor" : 10000,
    "daging" : 24000,
    "sayur" : 12000,
    "tepung" : 14000,
    "mangga" : 15000
}
keranjang = []
total = []
#  Function for create a bom
def create_bon():
    daftar = input("Masukkan Barang yang ingin dibeli: ")
    while daftar != "done":
        if daftar in barang_jualan:
            count = int(input("Masukkan Jumlah barang: "))
            temp = barang_jualan[daftar]*count
            keranjang.append(daftar)
            total.append(temp)
            daftar = input("Masukkan Barang yang ingin dibeli (Type 'done' to end): ")
        else:
            print("Barang Gk Ada")  
            daftar = input("Masukkan Barang yang ingin dibeli (Type 'done' to end): ")
    display_bon()
# Function for Menu UI
def menu():
    x = 0
    y = 2
    while x != y:
        print("==============")
        print("|Mesin Kasir |")
        print("|1. Buat Bon |")
        print("|2. Exit     |")
        print("==============")
        x = int(input("Masukkan Pilihan Anda:"))
        if x == 1:
            create_bon()

#Fucntion for print Bon
def display_bon():
    ch = input("Apakah ada barang yang ingin ditambah(Y/N)?")
    if ch == "Y":
        create_bon()
    elif ch == "N":
        print("==========================")
        print("No   Barang   Total Harga")
        i =1
        for j in range(len(keranjang)):
            print("%d%10s%13d" %(i,keranjang[j], total[j]))
            # print(f"{i}     {keranjang[j]}  Rp {total[j]}")
            i+=1
        print("--------------------------")
        print(f"Sub Total       Rp {sum(total)}")
        print("==========================") 

        
menu()