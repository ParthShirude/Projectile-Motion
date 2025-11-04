import math as m
def inputs ():

    initial_vel=int(input('Enter initial velocity:'))

    Alpha=int(input('\nEnter initial angle with horizontal:'))

    return initial_vel,Alpha

initial_vel,Alpha=inputs()

def Projectile (initial_vel,Alpha):
    
    g=9.81

    Time_of_flight=((2*initial_vel)*(m.sin(m.radians(Alpha))))/g
    print('\nTotal time of flight is:',Time_of_flight)

    Range=((initial_vel**2)/g)*m.sin(m.radians(2*Alpha))
    print('\nHorizontal Range is:',Range)

    Height_max=((initial_vel**2)*((m.sin(m.radians(Alpha)))**2))/(2*g)
    print('\nMaximun Height Attend is:',Height_max)

Projectile(initial_vel,Alpha)