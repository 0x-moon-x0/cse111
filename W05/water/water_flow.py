def water_column_height(tower_height, tank_height):
    '''Calculates and returns the height of a column of water in meters.
        Parameters
            tower_height: the height of the tower
            tank_height: the height of the tank
        Return: the height of a column of water in meters'''
    
    column_height = tower_height + (3 * tank_height) / 4

    return column_height

def pressure_gain_from_water_height(height):
    '''Calculates and returns the pressure caused by Earth's gravity pulling on the water stored in an elevated tank.
        Parameters
            height: the height of a column of water in meters
        Return: the pressure caused by Earth's gravity in kilopascals'''
    
    pressure = (998.2 * 9.80665 * height) / 1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    '''Calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.
        Parameters
            pipe_diameter: the diameter of the pipe in meters
            pipe_length: the length of the pipe in meters
            friction_factor: the pipe's friction factor
            fluid_velocity: the velocity of the water flowing through the pipe in meters/second
        Return: the water pressure lost because of friction from the pipe in kilopascals'''
    
    pressure_loss = ((-friction_factor) * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)

    return pressure_loss
