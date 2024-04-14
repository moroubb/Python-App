def search(lst, el):
    pos = -1
    for i in range(len(lst)):
        if el == lst[i]:
            pos = i
    return pos


def sort(l, functie):
    issort = False
    while not issort:
        issort = True
        for i in range(0, len(l) - 1):
            if functie(l[i], l[i+1]):
                aux = l[i]
                l[i] = l[i + 1]
                l[i + 1] = aux
                issort = False
    return l

def compare_last_names(a,b):
    if b.get_last_name() >= a.get_last_name():
        return False
    return True

def compare_nr_of_passengers(a,b):
    if len(b.get_passengers()) >= len(a.get_passengers()):
        return False
    return True
def compare_strings(a,b):
    x=str(a.get_number_of_seats())+a.get_destination()
    y=str(b.get_number_of_seats())+b.get_destination()
    print(x)
    print(y)
    if x <= y:
        return False
    return True
