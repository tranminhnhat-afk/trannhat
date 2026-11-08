
def dem_cham(a):
    """Đếm số cặp nghịch thế bằng hai vòng lặp."""
    dem = 0
    cap = []

    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                dem += 1
                cap.append((i, j))

    return dem, cap


def tron_va_dem(a, l, m, r):
    """Trộn hai nửa đã sắp xếp và đếm nghịch thế."""
    t = []
    i = l
    j = m + 1
    dem = 0

    while i <= m and j <= r:
        if a[i] <= a[j]:
            t.append(a[i])
            i += 1
        else:
            t.append(a[j])
            dem += m - i + 1
            j += 1

    t.extend(a[i:m + 1])
    t.extend(a[j:r + 1])

    a[l:r + 1] = t

    return dem


def dem_nghich_the(a, l=0, r=None):
    """Đếm nghịch thế bằng chia để trị."""
    if r is None:
        r = len(a) - 1

    if l >= r:
        return 0

    m = (l + r) // 2

    dem_trai = dem_nghich_the(a, l, m)
    dem_phai = dem_nghich_the(a, m + 1, r)
    dem_ghep = tron_va_dem(a, l, m, r)

    return dem_trai + dem_phai + dem_ghep


def main():
    n = int(input("Nhap so phan tu n: "))
    a = list(map(int, input("Nhap mang a: ").split()))

    if n < 0 or n > 10000 or len(a) != n:
        print("Du lieu khong hop le!")
        return

    # Giữ lại mảng ban đầu
    b = a.copy()

    # Phương pháp hai vòng lặp
    kq_cham, cap = dem_cham(b)

    # Phương pháp Merge Sort
    c = a.copy()
    kq_nhanh = dem_nghich_the(c)

    print("\n--- KET QUA ---")
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
