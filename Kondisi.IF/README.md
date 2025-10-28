**LATIHAN 1 : Menentukan Bilangan Terbesar dari 4 bilangan ( Python )**

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">

</head>
<body>
  <pre><code class="language-python">

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
 
if a >= b and a >= c:
    terbesar = a
if b >= a and b >= c:
    terbesar = b
else:
    terbesar = c
 </code></pre>
</body>
</html>

"PENJELASAN PROGRAM"

1. Input data
-  Program meminta pengguna memasukkan empat bilangan bulat (a, b, c, dan d).
-  Fungsi int(input(...)) digunakan supaya nilai yang dimasukkan dianggap sebagai bilangan bulat (integer).
2. Menentukan bilangan terbesar
-  Fungsi max() adalah fungsi bawaan Python yang langsung mengembalikan nilai terbesar dari beberapa argumen.
-  Jadi max(a, b, c, d) otomatis membandingkan keempat bilangan dan memberikan yang paling besar.
3. Menampilkan hasil
-  Program mencetak hasilnya dengan fungsi print().

**LATIHAN 2 : PROGRAM MENAMPILKAN STATUS GAJI KARYAWAN**

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">

</head>
<body>
  <pre><code class="language-python">

gaji = int(input("Masukkan gaji: "))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T): ").upper() == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T): ").upper() == "Y"]

print("\n=== Status Karyawan ===")
if gaji > 3000000:
    print("Gaji sudah di atas UMR.")
    if berkeluarga:
        print("Wajib ikut asuransi dan menabung untuk pensiun.")
    else:
        print("Disarankan untuk mulai menabung untuk masa depan.")
    if punya_rumah:
        print("Wajib bayar pajak rumah.")
    else:
        print("Belum wajib pajak rumah, tapi bisa menabung untuk membeli rumah.")
else:
    print("Gaji masih di bawah atau sama dengan UMR.")
    if berkeluarga:
        print("Perlu mencari tambahan penghasilan untuk kebutuhan keluarga.")
    else:
        print("Fokus meningkatkan karier dan menabung.")
    if punya_rumah:
        print("Wajib bayar pajak rumah, meski gaji masih di bawah UMR.")
    else:
        print("Belum memiliki rumah — pertimbangkan untuk menabung.")
print("\n=== Terima kasih telah menggunakan program ini ===")

 </code></pre>
</body>
</html>

"PENJELASAN PROGRAM" 

1.  Input:
-  gaji → diambil sebagai angka (int).
-  berkeluarga → bernilai True jika pengguna menjawab Y.
-  punya_rumah → bernilai True jika pengguna menjawab Y.
2.  Proses:
-  Mengecek apakah gaji lebih dari Rp3.000.000 (anggap ini UMR).
-  Menentukan tindakan yang disarankan berdasarkan kondisi tersebut.
3.  Output:
-  Menampilkan status dan saran sesuai kondisi gaji, keluarga, dan rumah.

**LATIHAN 3 : Pengunaan QR**
"PENJELASAN PROGRAM"

Program ini menerima tiga input bilangan bulat (a, b, dan c) dan kemudian memeriksa apakah penjumlahan dua bilangan sama dengan bilangan ketiga.
Jika kondisi itu benar, program mencetak "BENAR", kalau tidak — "SALAH".
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">

if a + b == c or b + c == a or c + a == b:
 </code></pre>
</body>
Artinya:
-  Jika a + b sama dengan c, atau
-  Jika b + c sama dengan a, atau
-  Jika c + a sama dengan b,
-  maka hasilnya adalah BENAR

- **LATIHAN 3 : MEMBUAT PROGRAM PYTHON UNTUK KASUS TERTENTU**
-  **(KASUS 1 PROGRAM PEMESANAN TIKET BIOSKOP)**

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
tipe = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
 </code></pre>
</body>
1.  Program meminta dua input dari pengguna:
-  tipe tiket (reguler atau vip)
-  apakah pengguna member atau bukan
-  Fungsi .lower() memastikan input jadi huruf kecil semua (supaya tidak sensitif terhadap kapitalisasi).
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
  harga = 50000 if tipe == "reguler" else 100000 if tipe == "vip" else 0
</code></pre>
</body>
2.  Ini adalah operator ternary (if satu baris):
-  Jika tipe adalah "reguler", maka harga = 50.000
-  Jika tipe adalah "vip", maka harga = 100.000
-  Jika tidak keduanya, maka harga = 0 (tanda input salah)
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
diskon = 0.2 * harga if member == "ya" else 0
</code></pre>
</body>
3.  Jika user punya kartu member (ya), maka diskon 20% dari harga tiket.
Kalau tidak (tidak), diskonnya 0.
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
  total = harga - diskon
</code></pre>
</body>
4.  Hitung total harga yang harus dibayar setelah potongan diskon.
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
  if harga == 0:
    print("Tipe tiket tidak valid.")
else:
    print(f"Harga tiket: Rp{harga:,.0f}")
    if member == "ya":
        print(f"Diskon member: Rp{diskon:,.0f}")
    print(f"Total yang harus dibayar: Rp{total:,.0f}")
</code></pre>
</body>

5.  Program memeriksa:
-  Kalau harga = 0, berarti input tiket tidak valid.
-  Jika valid, tampilkan harga, diskon (jika ada), dan total pembayaran.-  
F-string (f"...") digunakan agar tampilan angka jadi rapi seperti Rp100,000.

-  **(KASUS 2 PROGRAM KALKULATOR SEDERHANA)**

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
  
  a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
op = input("Masukkan operator (+, -, *, /): ")
</code></pre>
</body>
1.  Program meminta dua angka (a dan b) serta operator matematika (op).
Tipe datanya float agar bisa menghitung bilangan desimal juga.
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <pre><code class="language-python">
  if op == "+":
    hasil = a + b
elif op == "-":
    hasil = a - b
elif op == "*":
    hasil = a * b
elif op == "/":
    hasil = a / b if b != 0 else "Tidak bisa dibagi dengan nol!"
else:
    hasil = "Operator tidak valid!"
</code></pre>
</body>
-  Gunakan struktur if – elif – else untuk memeriksa operator:
-  Jika + → lakukan penjumlahan
-  Jika - → lakukan pengurangan
-  Jika * → lakukan perkalian
-  Jika / → lakukan pembagian, tapi periksa dulu apakah b ≠ 0
(supaya tidak terjadi error “division by zero”)
-  Jika operator tidak dikenal → ta
