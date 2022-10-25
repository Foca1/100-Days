#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    if seconds == 0:
        return 'now'

    #Verifica se dps das horas vai precisar de and
    def hasAnd(str,sub):
        x = str.rindex(sub) + 5
        if (len(str[x:]) < 13):
            str = str[:x] + str[x:].replace(",", "")
            str = f"{str[:x]} and{str[x:]}"
        return str 
    
    str = ""
    isPlural = lambda x: "s" if x > 1 else ""
    isAlone = lambda x: ", " if x != 0 else ""

    while seconds != 0:
        #Se for menos que uma hora
        if seconds/60/60 < 1:
            #Se for menos que um minuto
            if seconds/60 < 1:
                str += f"{seconds} second{isPlural(int(seconds))}"
                seconds -= seconds
            else:
                str += f"{int(seconds/60)} minute{isPlural(int(seconds/60))}"
                seconds -= 60 * (seconds//60)
                if seconds != 0:
                    str += " and "
        else:
            #Se for menos de um ano
            if seconds/(3600*24*365) < 1:
                #Se for menos de um dia
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

    return str if str.count("hours") == 0 else hasAnd(str, "hours")

print(format_duration(5000122))