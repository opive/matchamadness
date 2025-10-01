from flask import Flask, render_template, request, redirect, url_for
import threading, time, random, requests
from bs4 import BeautifulSoup
import smtplib #for emails
from email.mime.text import MIMEText #for emails

app = Flask(__name__)
checking = False
last_status = "Not checked yet"

URL = "https://global.tokichi.jp/products/mc2" # ex. I want fuji no shiro really badly

def check_stock():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Look for the "Out of stock" badge
    out_of_stock_badge = soup.select_one(".price__badge-sold-out")

    if out_of_stock_badge and "out of stock" in out_of_stock_badge.get_text(strip=True).lower():
        return False  # out of stock

    # otherwise check if add cart button exists
    add_to_cart_button = soup.select_one(".product-form__submit")

    if add_to_cart_button and "add to cart" in add_to_cart_button.get_text(strip=True).lower():
        return True  # in stock

    return False  # default treat as out of stock

def send_email():
    MSG = MIMEText("The item is back in stock! " + URL)
    MSG['Subject'] = "Item Back In Stock!"
    MSG['From'] = "olivetree196@gmail.com"
    MSG['To'] = "oliviaspotify176@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your_email@example.com", "your_app_password")
        server.sendmail(MSG["From"], [MSG["To"]], MSG.as_string())


def background_check():
    global checking, last_status #says that function will use and change global variables (checing and last_status)
    while checking:
        stock = check_stock()
        if stock:
            last_status = "In Stock!"
            send_email()
            checking = False  # stop checking after sending email
        else:
            last_status = "Out of Stock"
    time.sleep(random.randint(600, 2400))  # wait between 10 to 40 minutes

@app.route('/')
def index():
    return "Hello, World!"