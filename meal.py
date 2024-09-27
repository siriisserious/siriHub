def main(t):
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        print("")

def convert(t):
    hours, minutes = t.split(":")
    minutes = float(minutes)
    hours = float(hours)
    t = (hours + minutes/60)
    return float(t)

if __name__ == "__main__":
    time = input("What time is it?")
    main(convert(time))
