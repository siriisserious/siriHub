months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}



while True:
    date = input("Date: ")

    if "/" in date:
        try:      #input should be all integers
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = year.strip()

            if month > 12 or day > 31:
                continue
            else:
                print(f"{year}-{month:02}-{day:02}")
                break

        except (ValueError, TypeError):
            pass


#change vvv to elif later
    elif "," in date:
         try:
            month, day, year = date.split(" ")
            day = day.removesuffix(",")
            day = int(day)
            month = str(month.title().strip())

            if month in months and day < 32:
                print(f"{year}-{months[month]:02}-{day:02}")
                break

            else:
                continue

         except (ValueError, TypeError):
            pass

    else:
        continue
