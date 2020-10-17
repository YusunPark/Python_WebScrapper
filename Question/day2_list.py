def is_on_list(days, date):
    if date in days:
        return True
    else:
        return False


def get_x(days, num=int()):
    return days[num]


def add_x(days, date):
    days.append(date)
    return days


def remove_x(days, date):
    days.remove(date)
    return days

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

