import smtplib
import datetime as dt
import random
my_email="your gmail"
password="YOUR password"


date = dt.datetime.now()
if date.weekday()==0:
    with open("quotes.txt", "r") as file:
        quotes = [line.strip() for line in file.readlines()]
        quote="".join(random.choices(quotes))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tharunbheemanadula@gmail.com",
                            msg=f"Subject:Motivation\n\n{quote}")








