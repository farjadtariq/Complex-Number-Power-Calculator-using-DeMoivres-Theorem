#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/16
#
#Purpose:       The purpose of this is to write a complete Python program
#               that calculates powers of complex numbers using DeMoivre’s theorem.


from time import ctime
from math import cos, sin, pi

def computeDeMoivre(maxAngle, intervals, power):
    """Creates a list of equally spaced angles from 
        0 to maxAngle based on the number of
        intervals and lists of complex numbers."""
    #Angles =       List of equally spaced angles expressed in radians
    #cNumtoN1 =     The list created using equation 1
    #cNumtoN2 =     The list created using equation 2
    angles = []
    cNumtoN1 = []
    cNumtoN2 = []
    for i in range(intervals+1):

        x = i * maxAngle / intervals                #valus of equally spaced angles
        x = x * pi / 180                            #angle converted into radian
        angles.append(x)
        equation1 = ((cos(x)+1j*sin(x))**power)     #first equation of the DeMoivre Theorem
        cNumtoN1.append(equation1)
        equation2 = cos(power*x)+sin(power*x)*1j    #second equation of the DeMoivre Theorem
        cNumtoN2.append(equation2)

    return angles, cNumtoN1, cNumtoN2

def displayLists(angles, cNumtoN1, cNumtoN2):
    """Displays the headngs and the lists. Counts
        the difference between two complex numbers
        and determines whether they're equal or not."""
    #difference = difference between the two complex numbers
    #x = complex number 1
    #y = complex number 2
    print("\n%21s %44s %44s %5s %s" % ("Angle in Radians", "(cos(x)+i*sin(x))^n", 
            "cos(n*x)+i*sin(n*x)","Equal", "Difference"))

    for angles, x, y in zip(angles, cNumtoN1, cNumtoN2):

        difference = x - y         
        print("%21.14e %44r %44r %-5r %r" % (angles, x, y, x==y, difference))

def main():
    """The main function which calls other functions.
        Inputs intervals as integer and maximum angle
        and power as floats."""
    #intervals = Number of intervals between angles
    #maxAngle = Maximum angle
    #power = The power used in the equations of DeMoivre Theorem     
    print('\n' + '-'*60)
    intervals = int(input("Enter the number of intervals between the angles (0 to quit): "))

    while intervals > 0:
        maxAngle = float(input("Enter the maximum angle in degrees (>0): "))
        if maxAngle <= 0:       
            print("The maximum angle, %i, must be greater than zero!" % (maxAngle))
            intervals = int(input("Enter the number of intervals between the angles (0 to quit): "))
            #Checks whether the angle is greater than zero or not, if not gives and error
            #   message and asks for the values again starting from intervals.
        else:
            #Gets input for the power used in equation
            power = float(input("Enter the value of the power: "))
            #calls computeDeMoivre
            angles, cNumtoN1, cNumtoN2 = computeDeMoivre(maxAngle, intervals, power)  
            #calls displayLists
            displayLists(angles, cNumtoN1, cNumtoN2)    

            intervals = int(input("Enter the number of intervals between the angles (0 to quit): "))

def displayTerminationMessage():
    print("""
Programmed by Farjad Tariq
Date: %s
End of processing.\n""" % ctime())

main()
displayTerminationMessage()