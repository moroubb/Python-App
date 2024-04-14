from passenger import *
from plane import *
from utils import *
import keyboard

l = PlaneRepo()


def create_p_list():
    # adds a passenger to a list if key "+" is selected
    ok = True
    lst = []
    while ok:
        if keyboard.is_pressed("+"):
            fn = input("input first name: ", )
            ln = input("input last name: ", )
            pn = input("passport number: ", )
            lst.append(Passenger(fn, ln, pn))
        elif keyboard.is_pressed('-'):
            ok = False
    return lst

def option3(plane_name):
    # sorts the passengers in a plane by their last name
    x = l.get_plane_by_name(plane_name).get_passengers()
    y = sort(x, compare_last_names)
    return y


def option4():
    # sorts the planes by the number of their passengers
    x = sort(l.get_planes(), compare_nr_of_passengers)
    return x


def option5(substring):
    # Sort planes according to the number of passengers with the first name starting with a given substring
    x = 0
    result = []
    plane_name = []
    plane = l.get_planes()
    for i in l.get_planes():
        name_list = PassengerRepo(i.get_passengers())
        y = 0
        for j in name_list.get_people():
            if j.get_first_name().find(substring) == 0:
                y += 1
        plane_name.append((x, y))
        x += 1
    plane_name = sorted(plane_name, key=lambda z: z[1])
    for i in plane_name:
        result.append(plane[i[0]])
    return result


def option6():
    # Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    x = l.get_planes()
    y = sort(x, compare_strings)
    return y


def option7():
    # no comment
    pass


def option8(plane_name, substring):
    # Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  namecontain a string given as parameter
    x = PassengerRepo(l.get_plane_by_name(plane_name).get_passengers())
    result = []
    for i in x.get_people():
        if i.get_first_name().find(substring) >= 0 or i.get_last_name().find(substring) >= 0:
            result.append(i)
    return result


def option9(fn, ln):
    # Identify plane/planes where there is a passenger with given name
    x = l.get_planes()
    result = []
    for i in x:
        for j in i.get_passengers():
            if j.get_first_name() == fn and j.get_last_name() == ln:
                result.append(i)
    return result

