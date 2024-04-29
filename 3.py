def tinh_giai_thua(n):
    if n < 0:
        return "Invalid"
    elif n == 0:
        return 1
    else:
        giai_thua = 1
        for i in range(1, n + 1):
            giai_thua *= i
        return giai_thua

so_nguyen = int(input("Nhập vào một số nguyên không âm: "))
ket_qua = tinh_giai_thua(so_nguyen)
print("Giai thừa của", so_nguyen, "là:", ket_qua)