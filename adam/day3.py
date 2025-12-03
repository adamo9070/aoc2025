def read_data(file: str) -> list[str]:
    with open(file, 'r') as F:
        return [z.strip() for z in F]

def part_1(dane: list[str]) -> int:
    result = 0
    for bank in dane:
        max_bat = str(max([int(z) for z in bank]))
        if max_bat == bank[-1]:
            bank = bank[:-1]
            max_bat2 = str(max([int(z) for z in bank]))
            result += int(max_bat2 + max_bat)
        elif max_bat == bank[0]:
            bank = bank[1:]
            max_bat2 = str(max([int(z) for z in bank]))
            result += int(max_bat + max_bat2)
        else:
            bank = bank[bank.index(max_bat)+1:]
            max_bat2 = str(max([int(z) for z in bank]))
            result += int(max_bat + max_bat2)
    return result

def main() -> None:
    print(part_1(read_data('data/data3-example.txt')))
    print(part_1(read_data('data/data3.txt')))

if __name__ == '__main__':
    main()

