##################### Extra Hard Starting Project ######################
import datetime as dt
import os
import pandas
import random
import smtplib
from dotenv import load_dotenv

# Load variables from the .env file into your environment
load_dotenv()

MY_EMAIL=os.environ.get("MY_EMAIL")
MY_PASSWORD=os.environ.get("MY_APP_PASSWORD")
TO_ADDRESS=os.environ.get("TO_ADDRESS")


now = dt.datetime.now()
today_tuple = (now.month, now.day)


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthday_dict)


# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path, encoding="utf-8") as data_file:
        contents = data_file.read()

        contents = contents.replace("[NAME]", birthday_person["name"])
 

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg=f"Subject: Birthday Message\n\n{contents}".encode("utf-8")
        )
        print("Mail sent successfully.")

else:
    print(f"Data not matched.")