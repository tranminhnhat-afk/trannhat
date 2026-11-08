
def dem_cham(a):
    """Dem so cap nghich the bang hai vong lap."""
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
    """Tron hai nua da sap xep va dem nghich the."""
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
    """Dem nghich the bang chia de tri."""
    if r is None:
        r = len(a) - 1

    if l >= r:
        return 0

    m = (l + r) // 2

    dem_trai = dem_nghich_the(a, l, m)
    dem_phai = dem_nghich_the(a, m + 1, r)
    dem_ghep = tron_va_dem(a, l, m, r)

    return dem_trai + dem_phai + dem_ghep


def kiem_thu_tu_dong():
    """Chay tu dong 12 ca kiem thu."""

    cac_ca = [
        ("TC01", [2, 4, 1, 3, 5], 3),
        ("TC02", [3, 3, 1], 2),
        ("TC03", [0, -1, 0], 1),
        ("TC04", [2, 2, 2], 0),
        ("TC05", [], 0),
        ("TC06", [5], 0),
        ("TC07", [1, 2, 3, 4], 0),
        ("TC08", [4, 3, 2, 1], 6),
        ("TC09", [5, 5, 5, 5], 0),
        ("TC10", [-3, -1, -2], 1),
        ("TC11", [-2, 3, 0, -1], 3),
        ("TC12", [1000, -1000, 1000, -1000], 3)
    ]

    dat = 0

    print("\n========== TONG KET KIEM THU ==========")

    print("{:<8} {:<30} {:<12} {:<12} {}".format(
        "Ma ca", "Mang dau vao",
        "Mong doi", "Thuc te", "Ket qua"
    ))

    print("-" * 80)

    for ma, a, mong_doi in cac_ca:
        b = a.copy()
        c = a.copy()

        kq_cham, _ = dem_cham(b)
        kq_nhanh = dem_nghich_the(c)

        if kq_cham == mong_doi and kq_nhanh == mong_doi:
            ket_qua = "DAT"
            dat += 1
        else:
            ket_qua = "KHONG DAT"

        print("{:<8} {:<30} {:<12} {:<12} {}".format(
            ma, str(a),
            mong_doi, kq_nhanh, ket_qua
        ))

    print("-" * 80)
    print("Tong so ca kiem thu:", len(cac_ca))
    print("So ca dat:", dat)
    print("So ca khong dat:", len(cac_ca) - dat)

    if dat == len(cac_ca):
        print("KET LUAN: TAT CA CAC CA KIEM THU DEU DAT!")
    else:
        print("KET LUAN: CO CA KIEM THU CHUA DAT!")


def main():
    print("===== CHUONG TRINH DEM NGHICH THE =====")
    print("1. Nhap du lieu thu cong")
    print("2. Kiem thu tu dong 12 ca")

    chon = input("Lua chon cua ban: ")

    if chon == "2":
        kiem_thu_tu_dong()
        return

    if chon != "1":
        print("Lua chon khong hop le!")
        return

    try:
        n = int(input("Nhap so phan tu n: "))
        a = list(map(int, input("Nhap mang a: ").split()))
    except ValueError:
        print("Du lieu khong hop le!")
        return

    if n < 0 or n > 10000 or len(a) != n:
        print("Du lieu khong hop le!")
        return

    # Luu mang ban dau de so sanh
    b = a.copy()

    # Phuong phap hai vong lap
    kq_cham, cap = dem_cham(b)

    # Phuong phap Merge Sort
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
