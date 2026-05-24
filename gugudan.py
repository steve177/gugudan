def get_result(n, m):
    return n * m


def print_gugudan(n):
    for m in range(1, 10):
        print(f"{n} x {m} = {get_result(n, m)}")


def print_all_gugudan():
    for n in range(2, 10):
        print_gugudan(n)
        if n < 9:
            print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            if n < 2 or n > 9:
                print("오류: 2~9 사이의 단을 입력하세요.", file=sys.stderr)
                sys.exit(1)
            print_gugudan(n)
        except ValueError:
            print("오류: 숫자를 입력하세요.", file=sys.stderr)
            sys.exit(1)
    else:
        print_all_gugudan()
