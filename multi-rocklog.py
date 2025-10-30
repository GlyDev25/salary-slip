locality = int(input('how many lacalities did you visit? _'))
for localities in range (1, locality + 1):
    rock_types =int(input(f'how many rockypes did you see at locality {localities} _'))
    for rocks in range (1,rock_types +1):
        rock_type = input(f'enter the name of rock-type {rocks} you found at locality {localities} _ ')
    print(rock_type)