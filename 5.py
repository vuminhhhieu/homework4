def kiem_tra_tong_chu_so_bang_9(so):
    tong = sum(int(chu_so) for chu_so in str(so))
    return tong == 9

so_luong_so_tim_duoc = 0
so = 1000

print("10 số tự nhiên đầu tiên có 4 chữ số và có tổng các chữ số bằng 9:")
while so_luong_so_tim_duoc < 10:
    if kiem_tra_tong_chu_so_bang_9(so):
        print(so)
        so_luong_so_tim_duoc += 1
    so += 1