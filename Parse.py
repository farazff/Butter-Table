def main():
    lines = []
    ans = int(0)
    while True:
        line = input()
        if line == "d":
            break
        ans = ans + int(line)

    print(ans)

if __name__ == "__main__":
    main()
