from datetime import datetime, timedelta

def pdate(start_year,start_month,start_day, end_year, end_month,end_day):
    # Start and end dates
    start_date = datetime(int(start_year),int(start_month),int(start_day))
    end_date = datetime(int(end_year),int(end_month),int(end_day))

    # Generate list of dates
    date_array = []
    current_date = start_date

    while current_date <= end_date:
        date_array.append(current_date.strftime('%d%m%Y'))
        current_date += timedelta(days=1)

    print(date_array)

    return date_array