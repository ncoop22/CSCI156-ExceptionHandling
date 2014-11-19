__author__ = 'Nickolas'


inputstring = "Social Security Number"

def SSnumber(number,s):
    try:
        area, group, serial = number.split("-")
        if len(area) != (3) or len(group) != 2 or len(serial)!=4:
            print("You are a Dumb Ass, please make a wiser choice")
            return None
        elif number=="078-05-1120":
            print("You are a Dumb Ass, please make a wiser choice")
            return None
        elif "666" == area:
            print("You are a Dumb Ass, please make a wiser choice")
            return None
        elif int(area)>=900:
            print("You are a Dumb Ass, please make a wiser choice")
            return None
        elif area=="000" or group=="00" or serial=="0000":
            print("You are a Dumb Ass, please make a wiser choice")
            return None
        else:
            print("You are not a Dumb Ass")
            return area, group, serial
    except ValueError:
        print("You are a Dumb Ass, please make a wiser choice")
        return None


def valid(s):
    number = input(s)
    ss = SSnumber(number,s)
    while ss is None:
        number = input(s)
        SSnumber(number, s)
    return ss


print(valid(inputstring))