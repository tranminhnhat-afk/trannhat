
from dem_nghich import dem_cham, dem_nghich_the


def main():
    print("===== CHUONG TRINH DEM NGHICH THE =====")

    try:
        n = int(input("Nhap so phan tu n: "))

        if n < 0 or n > 10000:
            print("Du lieu khong hop le!")
            return

        a = list(map(int, input("Nhap mang a: ").split()))

    except ValueError:
        print("Du lieu khong hop le!")
        return

    if len(a) != n:
        print("Du lieu khong hop le!")
        return

    if any(x < -1000 or x > 1000 for x in a):
        print("Du lieu khong hop le!")
        return

    b = a.copy()
    c = a.copy()

    kq_cham, cap = dem_cham(b)
    kq_nhanh = dem_nghich_the(c)

    print("\n===== KET QUA =====")
    print("So nghich the (hai vong lap):", kq_cham)
    print("So nghich the (Merge Sort):", kq_nhanh)

    if n <= 8:
        print("Cac cap chi so nghich the:", cap)

    print("Mang sau khi sap xep:", c)

    if kq_cham == kq_nhanh:
        print("Kiem tra: Hai phuong phap cho ket qua trung khop.")
    else:
        print("Kiem tra: Ket qua khong trung khop!")


if __name__ == "__main__":
    main()
