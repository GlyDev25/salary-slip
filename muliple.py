samples = int(input('how many sample?_ '))
for rock_X in range (1, samples + 1):
    mass = int(input(f"What is the mass of rock {rock_X} (g):_ "))
    volume = int(input(f"what is the volume of rock {rock_X} (cm^3) _ "))
    density = mass/volume
    print(f'density of this rock sample is {density}(g/cm^3)')
    