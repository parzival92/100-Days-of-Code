
import random
import smtplib
import datetime as dt

now = dt.datetime.now()

weekday = now.weekday()

my_email = "******************"
to_email = "********************"
password = "***************"

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
    
        connection.starttls()
        
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Wednesday Motivation\n\n{quote}"
        )