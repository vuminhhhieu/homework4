def tinh_tong_chu_so(so_nguyen):
    tong = 0
    while so_nguyen > 0:
        tong += so_nguyen % 10
        so_nguyen //= 10
    return tong

def nhap_so_nguyen_duong():
    while True:
        try:
            so_nguyen = int(input("Nhập vào một số nguyên dương: "))
            if so_nguyen > 0:
                return so_nguyen
            else:
                print("Vui lòng nhập một số nguyên dương.")
        except ValueError:
            print("Vui lòng nhập một số nguyên dương hợp lệ.")

so_nguyen = nhap_so_nguyen_duong()
tong_chu_so = tinh_tong_chu_so(so_nguyen)
print("Tổng các chữ số của", so_nguyen, "là:", tong_chu_so)