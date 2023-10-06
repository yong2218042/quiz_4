def main():
    while True:
        try:
            dan_input = input("몇 단까지 출력할까요? (종료하려면 'q' 또는 'quit'): ")

            if dan_input.lower() in ['q', 'quit']:
                print("프로그램을 종료합니다.")
                break

            dan_input = int(dan_input)

            if 1 <= dan_input <= 19:
                for dan in range(1, dan_input + 1):
                    print_gugudan(dan)
            else:
                print("1에서 19 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
