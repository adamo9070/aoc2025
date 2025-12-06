import os
import argparse
import time
import importlib

parser = argparse.ArgumentParser()
parser.add_argument('day', type=int)
parser.add_argument('-t', '--test', action='store_true')
args = parser.parse_args()

# Załaduj moduły dla dni, jeśli istnieją
days = [None]  # days[0] = None
for i in range(1, 13):
    try:
        days.append(importlib.import_module(f'src.day{i}'))
    except ModuleNotFoundError:
        days.append(None)

def run_day(day_number: int):
    if day_number >= len(days) or days[day_number] is None:
        print(f"Nie ma jeszcze dnia {day_number}")
        return None, None

    path = f'data/data{day_number}-example.txt' if args.test else f'data/data{day_number}.txt'

    if not os.path.exists(path):
        print(f"Plik {path} nie istnieje!")
        return None, None

    with open(path, 'r') as f:
        lines = [line.strip() for line in f]

    start_time = time.time()
    results = []

    # Uruchomienie zadań, jeśli istnieją
    try:
        results.append(days[day_number].task_1(lines))
    except AttributeError:
        results.append(None)

    try:
        results.append(days[day_number].task_2(lines))
    except AttributeError:
        results.append(None)

    elapsed = time.time() - start_time
    return results, elapsed * 1000  # czas w ms

def print_day(intro, results, elapsed):
    print(intro)
    if results is None:
        print("No output")
    else:
        print("Part 1:", results[0])
        if results[1] is not None:
            print("Part 2:", results[1])
        print(f"Took {elapsed:.3f}ms")

def main() -> None:
    results, elapsed = run_day(args.day)
    print_day(f"Day {args.day}:", results, elapsed)

if __name__ == '__main__':
    main()
