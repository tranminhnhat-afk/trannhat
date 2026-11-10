
from dem_nghich import dem_cham, dem_nghich_the


def kiem_thu():
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

    print("-" * 85)

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
            ma, str(a), mong_doi, kq_nhanh, ket_qua
        ))

    print("-" * 85)
    print("Tong so ca kiem thu:", len(cac_ca))
    print("So ca dat:", dat)
    print("So ca khong dat:", len(cac_ca) - dat)

    if dat == len(cac_ca):
        print("KET LUAN: TAT CA CAC CA KIEM THU DEU DAT!")
    else:
        print("KET LUAN: CO CA KIEM THU CHUA DAT!")


if __name__ == "__main__":
    kiem_thu()
