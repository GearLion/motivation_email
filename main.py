import smtplib
import datetime
from random import choice
from passwords import EMAIL, PASSWORD

with open("quotation_docs/complete_quotations.txt") as quotes:
    # This is a strange code format, as this keeps the file around until the day arrives. We should do the reverse.
    if (datetime.datetime.now().weekday() + 2) % 7 == 5:
        quotation = choice(quotes.readlines())
        # After I've saved the quotation, I do not need to keep the txt file open either.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs="jjbaroff@gmail.com",
                                msg=f"Subject: Monday Motivation Quotation\n\nWelcome to the newsletter,"
                                    f"\n\n Here is today's quotation motivation:\n\n{quotation}.")
