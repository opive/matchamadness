from flask import Flask, render_template, request, redirect, url_for
import threading, time, random, requests
from bs4 import BeautifulSoup
import smtplib #for emails
from email.mime.text import MIMEText #for emails

app = Flask(__name__)

URL = "https://global.tokichi.jp/products/mc2" # ex. I want fuji no shiro really badly
@app.route('/')
def index():
    return "Hello, World!"