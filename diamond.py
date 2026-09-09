 # pola diamond / Belajar ketupat
 n = int(input("jumlah baris (setengah diamor):" \

 # 1. bagian atas (mulai dari 1 sampai n)
 for i in range(1, n + 1):
     print(" " * (n - i) + "*" * (2 * i - 1 ))

 for i in range(n - 1, 0, -1):
     print(" " * (n - i) + "*" * (2 * i - 1 ))
           
           