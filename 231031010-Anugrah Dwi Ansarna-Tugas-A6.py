while True:
    pilih = input('pilihan (ya/tidak): ')
    if pilih.lower() == 'ya':
        break
    elif pilih.lower() == 'tidak':
        print("Terima kasih! Program berhenti.")
        break
    else:
        print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")


'''
Penjelasan singkat:
1. "while True:" membuat loop yang akan berjalan terus-menerus karena kondisinya selalu benar.
2. "pilih = input('pilihan (ya/tidak): ')" meminta pengguna memasukkan teks.
3. "if pilih.lower() == 'ya':" memeriksa apakah input pengguna adalah 'ya', dan jika benar, program akan berhenti dengan "break".
4. "elif pilih.lower() == 'tidak':" memeriksa apakah input pengguna adalah 'tidak', dan jika iya, program akan mencetak pesan "Terima kasih! Program berhenti." dan kemudian berhenti.
5. Jika input pengguna tidak 'ya' atau 'tidak', program akan mencetak pesan "Input tidak valid. Silakan masukkan 'ya' atau 'tidak'."

Jadi, loop ini memungkinkan program berjalan terus sampai pengguna memilih 'ya' atau 'tidak'. Jika pilihan yang dimasukkan pengguna adalah 'ya' atau 'tidak', program akan berhenti.
'''