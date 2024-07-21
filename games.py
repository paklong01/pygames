# membuat games kertas batu gunting kertas
def main():
    print('Pilih salah satu!')
    print('1. Kertas')
    print('2. Batu')
    print('3. Gunting')
    print('4. Keluar')

    pilih = int(input('Masukan pilihan anda: '))
    import random
    comp = random.randint(1,3)

    if pilih == 1:
        if comp == 1:
            print('Kamu memilih kertas')
            print('Komputer memilih kertas')
            print('Seri!')
        elif comp == 2:
            print('Kamu memilih kertas')
            print('Komputer memilih batu')
            print('Komputer menang!')
        else:
            print('Kamu memilih kertas')
            print('Komputer memilih gunting')
            print('Komputer menang!')
    elif pilih == 2:
        if comp == 1:
            print('Kamu memilih batu')
            print('Komputer memilih kertas')
            print('Kamu menang!')
        elif comp == 2:
            print('Kamu memilih batu')
            print('Komputer memilih batu')
            print('Seri!')
        else:
            print('Kamu memilih batu')
            print('Komputer memilih gunting')
            print('Komputer menang!')
    elif pilih == 3:
        if comp == 1:
            print('Kamu memilih gunting')
            print('Komputer memilih kertas')
            print('Komputer menang!')
        elif comp == 2:
            print('Kamu memilih gunting')
            print('Komputer memilih batu')
            print('Kamu menang!')
        else:
            print('Kamu memilih gunting')
            print('Komputer memilih gunting')
            print('Seri!')
    elif pilih == 4:
             print('Terima kasih!')
             exit()
    else:
        print('Pilihan tidak tersedia')

main()