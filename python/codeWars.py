#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    def hasAnd(str,sub):
        x = str.rindex(sub) + 5
        if (len(str[x:]) >= 11):
            str = str[:x] + str[x:].replace(",", "")
        
        return f"{str[:x]} and{str[x:]}"
        
    isPlural = lambda x: "s" if x > 1 else ""
    isAlone = lambda x: ", " if x != 0 else ""
    str = ""

    while seconds != 0:
        if seconds/60/60 < 1:
            if seconds/60 < 1:
                str += f"{seconds} second{isPlural(int(seconds))}"
                seconds -= seconds
            else:
                str += f"{int(seconds/60)} minute{isPlural(int(seconds/60))}"
                seconds -= 60 * (seconds//60)
                if seconds != 0:
                    str += " and "
        else:
            if seconds/(3600*24*365) < 1:
                if seconds/(3600*24) < 1:
                    #Horas
                    str += f"{int(seconds/3600)} hour{isPlural(int(seconds/3600))}"
                    seconds -= 3600 * (seconds//3600)
                    str += isAlone(seconds)
                else:
                    #Dias
                    str += f"{int(seconds/(3600*24))} day{isPlural(int(seconds/(3600*24)))}"
                    seconds -= 86400 * (seconds//(3600*24))
                    str += isAlone(seconds)
            else:
                str += f"{int(seconds/(3600*24*365))} year{isPlural(int(seconds/(3600*24*365)))}"
                seconds -= 31536000 * (seconds//(3600*24*365))
                str += isAlone(seconds)

    hasAnd(str, "hour")
    return str

print(format_duration(285600))