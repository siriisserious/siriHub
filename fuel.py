while True:
    fraction = input("Fraction: ")

    try:
        numer, deno = fraction.split("/")
        fuel_level = int(round((int(numer) / int(deno)) * 100))

        if fuel_level > 100:
            continue
        elif fuel_level <= 1:
            print("E")
        elif 100 >= fuel_level >= 99:
            print("F")
        else:
            print(f"{fuel_level}%")
        break

    except (ValueError, ZeroDivisionError):
        pass
