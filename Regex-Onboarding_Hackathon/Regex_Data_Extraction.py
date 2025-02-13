import re

def extract_emails(data):
    regex_for_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(regex_for_email, data)

def extract_urls(data):
    regex_for_urls = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9./?=&%#-]*)?"
    return re.findall(regex_for_urls, data)

def extract_phone_numbers(data):
    regex_for_phone_numbers = r"\+?\d{1,3}[\s.-]?\(?\d{2,4}\)?[\s.-]?\d{2,4}[\s.-]?\d{2,4}[\s.-]?\d{0,4}"
    return re.findall(regex_for_phone_numbers, data)

def extract_credit_cards(data):
    regex_for_credit_cards = r"\b(?:\d{4}[- ]?){3}\d{4}|\b\d{4}[- ]?\d{6}[- ]?\d{5}\b"
    return re.findall(regex_for_credit_cards, data)

def extract_time(data):
    regex_for_time = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?i)(?:AM|PM))?\b"
    return re.findall(regex_for_time, data)