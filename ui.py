from passenger import *
from utils import *
from console import *
from plane import *


def menu():
    p = True
    l = PlaneRepo()
    while p == True:
        print("choose a menu")
        print("1.Print planes")
        print("2.Remove plane")
        print("3.Add plane")
        print("4.Update plane")
        print("5.Sort passengers in a plane by last name")
        print("6.Sort planes by the number of passengers")
        print("7.Sort planes according to the number of passengers with the first name starting with a given substring")
        print(
            "8.Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination")
        print(
            "9.Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter")
        print("10.Identify plane/planes where there is a passenger with given name")
        print("11.Exit")
        try:
            i = int(input())
        except:
            print("incorrect input")
            continue
        if (i < 1 or i > 18):
            print("select number from 1-11")
            continue
        if (i == 1):
            for i in l.get_planes():
                print(i)
        if (i == 2):
            name = input("type the name of the plane: ", )
            try:
                l.remove_plane(name)
            except:
                print("no plane with such name")
        if (i == 3):
            name = input("insert plane name: ", )
            company = input("insert company: ", )
            try:
                nrs = int(input("insert number of seats: ", ))
            except:
                print("invalid value")
            destination = input("insert destination: ", )
            plst = create_p_list()
            try:
                l.add_plane(name, company, nrs, destination, plst)
            except:
                print("name or list of passengers already in use")
        if (i == 4):
            name = input("insert plane name: ", )
            company = input("insert company: ", )
            try:
                nrs = int(input("insert number of seats: ", ))
            except:
                print("invalid value")
            destination = input("insert destination: ", )
            plst = create_p_list()
            try:
                l.update_plane(name, company, nrs, destination, plst)
            except:
                print("no plane with such name")
        if (i == 5):
            plane_name = input("insert plane name: ", )
            try:
                print(option3(plane_name))
            except:
                print("no plane with such name")
        if (i == 6):
            print(option4())
        if (i == 7):
            substring = input("insert a substring: ", )
            print(option5(substring))
        if (i == 8):
            print(option6())
        if (i == 9):
            plane_name = input("insert plane name: ", )
            s = input("insert a string: ", )
            try:
                print(option8(plane_name, s))
            except:
                print("no plane with such name")
        if (i == 10):
            fn = input("input first name: ", )
            ln = input("input last name: ", )
            if option9(fn, ln) == []:
                print("no passenger with such name")
            else:
                print(option9(fn, ln))
        if (i == 11):
            quit()


menu()
