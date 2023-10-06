# 기초 계산기 프로그램 개발

def print_gugudan(dan):
    print(f"------[ {dan} 단 ] ------")
    for i in range(1, 20):
        print(f"{dan} X {i} = {dan * i}")

def main():
    try:
        dan_input = int(input("몇 단까지 출력할까요? "))
        if 1 <= dan_input <= 19:
            for dan in range(1, dan_input + 1):
                print_gugudan(dan)
        else:
            print("1에서 19 사이의 숫자를 입력해주세요.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
