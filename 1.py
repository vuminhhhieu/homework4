def print_stair(steps):
    for i in range(1, steps + 1):
        print(' ' * (steps - i) + '#' * i)
def main():
    while True:
        try:
            steps = int(input("Nhap so bac cau thang: "))
            if steps <= 0:
                print("So bac phai lon hon 0")
            else:
                break
        except ValueError:
            print("Chi nhap so nguyen")

    print("Cau thang co", steps, "bac")
    print_stair(steps)
if __name__ == "__main__":
    main()