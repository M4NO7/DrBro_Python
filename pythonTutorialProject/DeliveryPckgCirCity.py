"""def deliver_packages(n, m, x):
    path = [1]  # Initialize the path with the starting house
    num_stops = 1  # Initialize the number of stops with 1 for the starting house
    current_house = 1  # Initialize the current house as the starting house

    while len(path) < m:
        current_house = (current_house + x) % n
        if current_house == 0:
            current_house = n

        path.append(current_house)
        num_stops += 1

    return path, num_stops


# Read input values
n = int(input("Enter the number of houses: "))
m = int(input("Enter the number of houses to deliver packages: "))
x = int(input("Enter the integer value for stopping after every x houses: "))

# Call the function to get the delivery path and number of stops
delivery_path, num_goes_around = deliver_packages(n, m, x)

# Print the delivery path and number of times chef goes around
print("Delivery path:", delivery_path)
print("Chef goes around:", num_goes_around)"""

"""def deliver_packages(n, m, x):
    path = [1]  # Initialize the path with the starting house
    num_stops = 1  # Initialize the number of stops with 1 for the starting house
    current_house = 1  # Initialize the current house as the starting house

    while len(path) < m:
        current_house = (current_house + x) % n
        if current_house == 0:
            current_house = n

        path.append(current_house)
        num_stops += 1

    return path, (num_stops - 1) // n  # Subtract 1 from num_stops and divide by n to get the number of times chef goes around

# Input
n = 10
m = 3
x = 7

# Call the function to get the delivery path and number of times chef goes around
delivery_path, num_goes_around = deliver_packages(n, m, x)

# Print the delivery path and number of times chef goes around
print("Delivery path:", delivery_path)
print("Chef goes around:", num_goes_around)"""

"""def deliver_packages(n, m, x):
    path = [1]  # Initialize the path with the starting house
    num_stops = 1  # Initialize the number of stops with 1 for the starting house
    current_house = 1  # Initialize the current house as the starting house

    while len(path) < m:
        current_house += x
        if current_house > n:
            current_house = current_house - n

        path.append(current_house)
        num_stops += 1

    return path, (num_stops - 1) // n  # Subtract 1 from num_stops and divide by n to get the number of times chef goes around

# Input
n = 10
m = 3
x = 7

# Call the function to get the delivery path and number of times chef goes around
delivery_path, num_goes_around = deliver_packages(n, m, x)

# Print the delivery path and number of times chef goes around
print("Delivery path:", delivery_path)
print("Chef goes around:", num_goes_around)"""

"""def deliver_packages(n, m, x):
    path = [1]  # Initialize the path with the starting house
    num_stops = 1  # Initialize the number of stops with 1 for the starting house
    current_house = 1  # Initialize the current house as the starting house

    while len(path) < m:
        for _ in range(x):
            current_house += 1
            if current_house > n:
                current_house = 1

        path.append(current_house)
        num_stops += 1

    return path, (num_stops - 1) // n  # Subtract 1 from num_stops and divide by n to get the number of times chef goes around

# Input your values here
n = int(input("Enter the number of houses: "))
m = int(input("Enter the number of houses to deliver packages: "))
x = int(input("Enter the integer value for stopping after every x house: "))

# Call the function to get the delivery path and number of times chef goes around
delivery_path, num_goes_around = deliver_packages(n, m, x)

# Print the delivery path and number of times chef goes around
print("Delivery path:", delivery_path)
print("Chef goes around:", num_goes_around)"""

