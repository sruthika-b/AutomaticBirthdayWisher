import smtplib
import datetime as dt
import pandas
import random

tod = dt.datetime.now()
today_month, today_day = tod.month, tod.day

birthday_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for(index,data_row) in birthday_data.iterrows()}


if (today_month,today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]["name"]
    birthday_email = birthdays_dict[(today_month, today_day)]["email"]
    rand_num = int(random.random()*4)
    if rand_num == 0:
        file_name = "letter_templates/letter_1.txt"
    elif rand_num == 1:
        file_name = "letter_templates/letter_2.txt"
    else:
        file_name = "letter_templates/letter_3.txt"

    file_obj = open(file_name)
    letter = file_obj.read().replace("[NAME]",birthday_person)
    file_obj.close()

    my_email = "sample test email"
    password = "sample password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # For encryption and securing connection
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_email,
                            msg=f"Subject:Happy Birthday\n\n{letter}"
                            )


