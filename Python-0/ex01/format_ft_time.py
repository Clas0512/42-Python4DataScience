import time, datetime


if __name__ == ("__main__"):
    print(f'Seconds since January 1, 1970: {time.time():,.4f} or {time.time():.2e} in scientific notation\n{datetime.date.today().strftime("%b")} {datetime.date.today().strftime("%d")} {datetime.date.today().strftime("%Y")}')