highway_number = int(input())

if 1 <= highway_number <= 99:
    highway_type = "primary"
elif highway_number >= 101:
    highway_type = "auxiliary"

if (highway_number % 2) == 0:
    highway_direction = "east/west"
elif (highway_number % 2) != 0:
    highway_direction = "north/south"

if (highway_number % 100) == 0 or (highway_number % 1000) == 0:
    print(f"{highway_number} is not a valid interstate highway number.")
elif 1 <= highway_number <= 99:
    print(f"I-{highway_number} is {highway_type}, going {highway_direction}.")
elif highway_number >= 101:
    print(f"I-{highway_number} is {highway_type}, serving I-{highway_number % 100}, going {highway_direction}.")
