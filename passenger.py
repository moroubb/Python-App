class Passenger:
    def __init__(self, fn, ln, pn):
        self.__first_name = fn
        self.__last_name = ln
        self.__passport_number = pn

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_passport_number(self):
        return self.__passport_number

    def set_first_name(self, n):
        self.__first_name = n

    def set_last_name(self, n):
        self.__last_name = n

    def set_passport_number(self, n):
        self.__passport_number = n

    def __repr__(self):
        return self.__first_name + ' ' + self.__last_name + ' ' + self.__passport_number


class PassengerRepo:
    def __init__(self, initial_list):
        self.list = initial_list[:]

    def get_people(self):
        return self.list

    def add_passenger(self, fn, ln, pn):
        ok = True
        for i in self.list:
            if i.get_passport_number() == pn:
                ok = False
        if ok == True:
            self.list.append((Passenger(fn, ln, pn)))
        else:
            raise ValueError("Passport Number already in use")

    def remove_passenger(self, pn):
        ok = False
        for i in self.list:
            if i.get_passport_number() == pn:
                self.list.pop(i)
                ok = True
        if ok == False:
            raise ValueError("No passenger with such passport number")

    def update_passenger(self, fn, ln, pn):
        ok = False
        for i in self.list:
            if i.get_passport_number() == pn:
                ok = True
                i.set_passport_number(pn)
                i.set_last_name(ln)
                i.set_first_name(fn)
        if ok == False:
            raise ValueError("no passsenger with such passport number")
