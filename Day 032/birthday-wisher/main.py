##################### Normal Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

import datetime as dt
import smtplib
from importlib.resources import contents
now = dt.datetime.now()
import random
today_tuple = (now.month,now.day)
my_email = "*********************"
to_email = "****************"
password = "************"


# HINT 2: Use pandas to read the birthdays.csv

import pandas

data = pandas.read_csv("birthdays.csv")


# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:

#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
    
        connection.starttls()
        
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )




