def read_data(file: str) -> list[str]:
    with open(file, 'r') as f:
        return [z.strip() for z in f]

def task_1(dane: list[str]) -> int:
    rotation = 50
    counter = 0
    for i in dane:
        if rotation == 0:
            counter += 1
        kierunek = i[0]
        ile = i[1:]
        if kierunek == 'L':
            rotation = (rotation - int(ile)) % 100
        else:
            rotation = (rotation + int(ile)) % 100
    return counter

def task_2(dane: list[str]) -> int:
    rotation = 50
    counter = 0
    for i in dane:
        kierunek = i[0]
        ile = i[1:]
        if kierunek == 'L':
            for n in range(1, int(ile) + 1):
                if (rotation - n) % 100 == 0:
                    counter += 1
            rotation = (rotation - int(ile)) % 100
        else:
            for n in range(1, int(ile) + 1):
                if (rotation + n) % 100 == 0:
                    counter += 1
            rotation = (rotation + int(ile)) % 100
    return counter

# test

def main() -> None:
    print(task_1(read_data('data.txt')))
    print(task_2(read_data('data.txt')))

if __name__ == '__main__':
    main()
