def nhap_so_duong():
    while True:
        try:
            so = float(input("Nhập vào một số thực: "))
            if so > 0:
                return so
            else:
                print("Vui lòng nhập một số dương.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

so_duong = nhap_so_duong()
print("Số bạn đã nhập là:", so_duong)