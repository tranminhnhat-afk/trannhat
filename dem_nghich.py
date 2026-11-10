
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
