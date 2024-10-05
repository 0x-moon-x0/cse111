'''In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders.
There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can.
Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food.
A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.'''

import math

def main ():
    '''Computes and prints the storage efficiency for each of the 12 steel can sizes.'''

    can_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    can_radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
    can_heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    best_storage = None
    best_cost = None
    max_storage_efficiency = -1
    max_cost_efficiency = -1

    for i in range (len (can_names)):

        name = can_names [i]
        radius = can_radiuses [i]
        height = can_heights [i]
        cost = can_costs [i]

        storage_efficiency = compute_storage_efficiency (radius, height)
        cost_efficiency = compute_cost_efficiency (cost, radius, height)

        print (f"Can name: '{name}' | Storage efficiency: {storage_efficiency:.2f} | Cost efficiency: {cost_efficiency:.0f}")

        if storage_efficiency > max_storage_efficiency:

            best_storage = name
            max_storage_efficiency = storage_efficiency
        
        if cost_efficiency > max_cost_efficiency:

            best_cost = name
            max_cost_efficiency = cost_efficiency
    
    print()
    print(f"Best can size in storage efficiency: {best_storage}")
    print(f"Best can size in cost efficiency: {best_cost}")

def compute_volume (radius, height):
    '''Computes and returns the volume of a cylinder.
        Parameters
            radius: the radius of the cylinder
            height: the height of the cylinder
        Return: the volume of the cylinder'''
    
    volume = math.pi * radius ** 2 * height

    return volume

def compute_surface_area (radius, height):
    '''Computes and returns the surface area of a cylinder.
        Parameters
            radius: the radius of the cylinder
            height: the height of the cylinder
        Return: the surface area of the cylinder'''
    
    area = 2 * math.pi * radius * (radius + height)

    return area

def compute_storage_efficiency (radius, height):
    '''Computes and returns the storage efficiency of a steel can.
        Parameters
            radius: the radius of the steel can
            height: the height of the steel can
        Return: the storage efficiency of a steel can'''
    
    volume = compute_volume (radius, height)
    surface_area = compute_surface_area (radius, height)
    efficiency = volume / surface_area

    return efficiency

def compute_cost_efficiency (cost, radius, height):
    '''Computes and returns the storage efficiency of a steel can.
        Parameters
            cost: the cost of a steel can
            radius: the radius of the steel can
            height: the height of the steel can
        Return: the storage efficiency of a steel can'''
    
    volume = compute_volume (radius, height)
    efficiency = volume / cost

    return efficiency

main ()