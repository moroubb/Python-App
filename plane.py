from passenger import *


class Plane:
    def __init__(self, n, c, nrs, dest, p):
        self.__name = n
        self.__company = c
        try:
            self.__number_of_seats = int(nrs)
        except:
            raise ValueError("incorrect input")
        self.__destination = dest
        self.__passengers = p[:]

    def get_name(self):
        return self.__name

    def get_company(self):
        return self.__company

    def get_number_of_seats(self):
        return self.__number_of_seats

    def get_destination(self):
        return self.__destination

    def get_passengers(self):
        return self.__passengers

    def set_name(self, n):
        if type(n) == str:
            self.__name = n
        else:
            raise ValueError("invalid value")

    def set_company(self, c):
        if type(c) == str:
            self.__company = c
        else:
            raise ValueError("invalid value")

    def set_number_of_seats(self, nrs):
        if type(nrs) == int and int(nrs) > 0:
            self.__number_of_seats = nrs
        else:
            raise ValueError("invalid value")

    def set_destination(self, d):
        if type(d) == str:
            self.__destination = d
        else:
            raise ValueError("invalid value")

    def set_passengers(self, p):
        if type(p) == list:
            self.__passengers = p[:]
        else:
            raise ValueError("invalid input")

    def __repr__(self):
        return 'Plane(' + self.__name + ", " + self.__company + ", " + str(
            self.__number_of_seats) + ", " + self.__destination + ')'+ ', ' + str(self.__passengers)



class PlaneRepo:
    def __init__(self):
        self.planes = [Plane('x123', "BlueAir", 170, 'Bali', [Passenger("Vlad", "Morosanu", "2309x"), Passenger("Octa", "Morosanu", "1310y"), Passenger("Alex", "Grigo", "0405z")]), Plane("y25", "JetBlue", 155, "Vietnam", [])]


    def get_planes(self):
        return self.planes

    def add_plane(self, n, c, nrs, d, p):
        for i in self.planes:
            if p == i.get_passengers():
                raise ValueError("two planes with same passengers")
            if n == i.get_name():
                raise ValueError("two planes with same name")
        self.planes.append(Plane(n, c, nrs, d, p))

    def remove_plane(self, n):
        ok = False
        for i in self.planes:
            if i.get_name() == n:
                self.planes.remove(i)
                ok = True
        if ok == False:
            raise ValueError("no plane with such name")

    def update_plane(self, n, c, nrs, d, p):
        ok = False
        for i in self.planes:
            if i.get_name() == n:
                ok = True
                i.set_company(c)
                i.set_destination(d)
                i.set_number_of_seats(nrs)
                i.set_passengers(p)
        if ok == False:
            raise ValueError("no plane with such name")
    def get_plane_by_name(self, n):
        for i in self.planes:
            if i.get_name() == n:
                return i
        raise ValueError("no plane with such name")
    def get_nr_of_passengers(self,i ):
        return len(self.planes[i].get_passengers())



