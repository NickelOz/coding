import sys
import re


def main():
    guards = {}

    current_guard = 0
    line = sys.stdin.readline()
    while line != '':

        # Check if a new guard is starting their shift
        match = re.search(r"Guard #([0-9]+)", line)
        if match is not None:
            current_guard = int(match.group(1))
            if current_guard not in guards:
                guards[current_guard] = [0]*60

        # Otherwise, it is a record of a guard falling asleep and waking up
        else:
            sleep = re.search(r"([0-9]{2})] falls asleep", line).group(1)
            awake = re.search(r"([0-9]{2})] wakes up",
                              sys.stdin.readline()).group(1)

            for i in range(int(sleep), int(awake)):
                guards[current_guard][i] += 1

        line = sys.stdin.readline()

    mode_sleep = 0
    score = 0
    for guard in guards:
        for i in range(60):
            if guards[guard][i] > mode_sleep:
                mode_sleep = guards[guard][i]
                score = i * int(guard)

    print(score)


if __name__ == "__main__":
    main()
