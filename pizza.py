print("Selamat Datang di PizzaHut")
print("Kami memiliki beberapa pizza spesial untuk Anda")


#daftar tampilan topping
print("silahkan pilih topping yang Anda inginkan :")
print("1. Frankfurter seharga 30000") 
print("2. Meat Monsta seharga 32000")
print("3. CheeseBurger seharga 35000")
print("4. Super Supreme Chicken seharga 40000")

hargaTopping = 0  
frankfurter = 30000
meatMonsta = 32000
cheeseBurger = 35000
superSupremechicken = 40000

while True:
    #input pemilihan topping 
    toppingChoice = int(input("masukan nomor toping yang Anda inginkan :"))
    if  toppingChoice == 1 : 
        hargaTopping = frankfurter
        break 
    elif toppingChoice == 2 :
        hargaTopping = meatMonsta
        break 
    elif toppingChoice == 3 :
        hargaTopping= cheeseBurger
        break 
    elif toppingChoice == 4 :
        hargaTopping = superSupremechicken
        break 
    else : 
        print ("Pilihan topping tidak valid")
        print("Tolong masukan nomor yang benar")


#fungsi untuk tampilan daftar Crust
print("silahkan pilih crust yang Anda inginkan :")
print("1. Thin  Crust seharga 35000") 
print("2. Thick Crust seharga 40000")
print("3. Cheese Crust seharga 45000")

hargaCrust = 0 
thinCrust = 35000
thickCrust = 40000
cheeseCrust = 45000

while True : 
#input pemilihan Crust
    crustChoice = int(input("masukan nomor Crust yang Anda inginkan :"))
    if  crustChoice == 1 : 
        hargaCrust = thinCrust
        break
    elif crustChoice == 2 :
        hargaCrust = thickCrust
        break
    elif crustChoice == 3 :
        hargaCrust = cheeseCrust
        break
    else : 
        print("Pilihan crust tidak valid")
        print("Tolong masukan nomor yang benar")

#fungsi untuk tampilan daftar Size
print(" silahkan pilih Size yang Anda inginkan :")
print("1. Small Size seharga 55000") 
print("2. Medium Size seharga 65000")
print("3. Large Size seharga 75000")

hargaSize = 0 
smallSize = 55000
mediumSize = 65000
largeSize = 75000

while True :
    #input pemilihan Size
    sizeChoice = int(input("masukan nomor Size yang Anda inginkan :"))
    if  sizeChoice == 1 : 
        hargaSize = smallSize
        break
    elif sizeChoice == 2 :
        hargaSize = mediumSize
        break
    elif sizeChoice == 3 :
        hargaSize = largeSize
        break
    else : 
        print("Pilihan size tidak valid")
        print("Tolong masukan nomor yang benar")


#tambahan keju
print ("Apakah Anda ingin menambahkan extra cheese seharga 13000? (ya/tidak)")

cheeseChoice = input("Masukkan pilihan Anda: ")
if cheeseChoice == "ya" :
    hargaCheese = 13000
else : 
    hargaCheese = 0

#total harga pizza 
totalHarga = hargaTopping + hargaCrust + hargaSize + hargaCheese
print("total harga yang harus di bayar sebesar :" , totalHarga)
print("terimakasih telah memesan pizza!")