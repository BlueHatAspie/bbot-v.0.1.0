import os
import random
from email.message import EmailMessage
import ssl
import smtplib
import datetime
import json


meals = [
    "Wisconsin Cauliflower Soup",
    "Weight Loss Vegetable Soup",
    "Slow Cooker White Bean Soup",
    "Healthy Slow Cooker Lentil and Vegetable Soup",
    "Crockpot White Chicken Chili",
    "Panera 10 Vegetable Soup",
    "Chicken Noodle Soup",
    "Homemade Rice Bowls",
    "Quesadillas",
    "Homemade Pizza",
    "Chili Cheese Dogs/Fries",
    "Crockpot BBQ Chicken Sandwiches/Fries",
    "Chicken Wings, Macaroni & Cheese, and a Vegetable",
    "Chicken Parmesan/Pasta",
    "Fettuccine Alfredo",
    "Fried Rice (shrimp or chicken)",
    "Lo Mein (shrimp or chicken)",
    "Meatball Subs",
    "Chicken Stroganoff",
    "Steak, Baked Potatoes, and Corn",
    "Chicken Pot Pi Bubble Up",
    "Fried Chicken Sandwiches & Fries",
    "Turkey & Spinach Salisbury Steak with Rice",
    "Salmon, Rice, and Vegetables",
    "Fried Fish, Potatoes, and Vegetables",
    "Air Fried Chicken, Creamed Spinach, and Potatoes",
    "Homemade Cheeseburger Macaroni with a vegetable",
    "Spaghetti with Meat Sauce and a Vegetable",
    "Smoked Sausage Potatoes and Carrots Sheetpan",
    "Chicken, Chicken Rice, and Vegetables",
    "Creamy Crockpot Chicken Stuffing with Green beans",
    "Chicken Spaghetti (Recipie: The Pioneer Woman)",
    "Grilled Whole Fish & Salad",
    "Sheet Pan Parmesan Chicken Drumsticks with Carrots and Potatoes",
    "Cheeseburger Sliders and Fries",
    "Turkey Burgers/Fries",
    "Chicken or Beef Gyros",
    "Jollof Chicken and Rice",
    "Southwest White Chicken Chili",
    "Corn and Turkey Chili with Black Beans"
]


def find_next_sunday():
    _today = datetime.date.today()

    # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    # 1       2        3          4         5       6         7

    if _today.isoweekday() == 1:
        _today_delta = datetime.timedelta(days=6)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 2:
        _today_delta = datetime.timedelta(days=5)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 3:
        _today_delta = datetime.timedelta(days=4)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 4:
        _today_delta = datetime.timedelta(days=3)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 5:
        _today_delta = datetime.timedelta(days=2)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 6:
        _today_delta = datetime.timedelta(days=1)
        _today = _today + _today_delta
        return f'{_today.month}/{_today.day}/{_today.year}'
    elif _today.isoweekday() == 7:
        return f'{_today.month}/{_today.day}/{_today.year}'


def send_list():
    random.shuffle(meals)   

    email_sender = os.environ.get('BBOT_EMAIL_ADDRESS')
    email_password = os.environ.get('BBOT_EMAIL_PASSWORD')
    email_receiver = os.environ.get('LIST_RECIEVER')

    email_subject = f'Weekly Dinner List -- Week of {find_next_sunday()}'
    email_body = f"""
    Possible dinner list for week of {find_next_sunday()} is:
    1. {meals[0]}
    2. {meals[1]}
    3. {meals[2]}
    4. {meals[3]}
    5. {meals[4]}
    
    Reply with "shuffle" if you would like a different list ~Feature Coming Soon~
                  """

    email_to_send = EmailMessage()
    email_to_send['To'] = email_receiver
    email_to_send['From'] = email_sender
    email_to_send['Subject'] = email_subject
    email_to_send.set_content(email_body)
    email_context = ssl.create_default_context()

    with open(os.path.join('data', 'general.json'), 'r') as f:
        content = json.load(f)
        if find_next_sunday() != content["lastTimeDinnerListSent"]:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=email_context) as smtp:
                smtp.login(email_sender, email_password)
                print('Sending email... ')
                smtp.sendmail(email_sender, email_receiver, email_to_send.as_string())
        else:
            print("Already sent the email for this week.")


def mCookingPy__onload():
    with open(os.path.join('data', 'general.json'), 'r') as f:
        content = json.load(f)
        if find_next_sunday() != content["lastTimeDinnerListSent"]:
            send_list()
            with open(os.path.join('data', 'general.json'), 'w') as f:
                content['lastTimeDinnerListSent'] = find_next_sunday()
                json.dump(content, f, indent=2)