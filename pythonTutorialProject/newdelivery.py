"""def deliver_packages(n, m, x):
    path = [1]
    num_stops = 1
    current_house = 1

    while len(path) < m:
        for _ in range(x - 1):
            current_house += 1
            if current_house > n:
                current_house = 1

        current_house += 1
        if current_house > n:
            current_house = 1

        path.append(current_house)
        num_stops += 1

    print("Delivery path:", path)
    num_goes_around = (num_stops - 1) // n
    if (num_stops - 1) % n > 0:
        num_goes_around += 1
    print("Chef goes around:", num_goes_around)


def main():
    n = int(input("Enter the number of houses: "))
    m = int(input("Enter the number of houses to deliver packages: "))
    x = int(input("Enter the integer value for stopping after every x house: "))

    deliver_packages(n, m, x)


if __name__ == "__main__":
    main()"""

def deliver_packages(n, m, x):
    path = [1]
    num_stops = 1
    current_house = 2

    while len(path) < m:
        count = 0
        while count < x:
            current_house += 1
            if current_house > n:
                current_house = 1
            count += 1

        path.append(current_house)
        num_stops += 1

        current_house += 1
        if current_house > n:
            current_house = 1

    print("Chef will stop at:", path)
    num_goes_around = (num_stops + 1) // n
    if (num_stops) % n > 0:
        num_goes_around += 2
    print("Chef goes around:", num_goes_around)


def main():
    n = 10
    m = 7
    x = 3

    deliver_packages(n, m, x)

if __name__ == "__main__":
    main()