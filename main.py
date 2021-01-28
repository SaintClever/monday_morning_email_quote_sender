import datetime, smtplib, random


# Datetime
now = datetime.datetime.now()
weekday = now.weekday()
# print(type(weekday)) # 0 = Mon, 1 = Tue, 2 = Wed, 3 = Thr, 4 = Fri, 5 = Sat, 6 = Sun


# Email
sender_email = 'sender_email'
recipient_email = 'recipient_email'
password = 'my_password' # input('password: ')


if weekday == 0:
    # Quote
    with open('quotes.txt') as f:
        quotes = [quote.strip() for quote in f.readlines()]
        while '' in quotes:
            quotes.remove('')
            
    quote = random.choice(quotes)
    # print(quote)
        
        
    try:        
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg= ' '.join([
                    f'From: {sender_email}',
                    f'To: {recipient_email}',
                    f'Subject: Monday morning positivity quote',
                    '',
                    f'{quote}'
                ]).encode('utf-8').strip()
            )
    except Exception as exception:
        print(f'Error: {exception}')