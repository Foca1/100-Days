#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds, str):
    while seconds != 0:
        if seconds/60/60 < 1:
            if seconds/60 < 1:
                str += f"{seconds} seconds"
                seconds -= seconds
            else:
                str += f"{int(seconds/60)} minutes"
                seconds -= 60 * (seconds/60)
        else:
            str += f"{int(seconds/3600)} hours"
            seconds -= 3600 * (seconds/60)

    return str

print(format_duration(720, ''))
