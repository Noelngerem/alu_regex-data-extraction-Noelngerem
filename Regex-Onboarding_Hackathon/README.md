# Regex Data Extraction

## Project Overview
This project extracts various types of structured data (emails, URLs, phone numbers, credit card numbers, and time formats) from raw text using **Regular Expressions (Regex)** in Python.
## Features
- Extracts **emails**, **URLs**, **phone numbers**, **credit card numbers**, and **time formats**.
- Uses **Python's `re` module** for pattern matching.
- Well-structured with **separate extraction functions**.
- Organized as a **Python package** for easy integration.

## Usage Guide

### **Example Input Data**
input_data = """
Contact us at support@example.com or visit our site https://www.example.com.
Call (123) 456-7890 or 123-456-7890 for assistance.
Your credit card 1234-5678-9012-3456 is charged $19.99.
Meeting at 14:30 and another at 2:30 PM.


### **Function Calls and Output**
from Regex_Data_Extraction import extract_emails, extract_urls, extract_phone_numbers, extract_credit_cards, extract_time

print("Emails:", extract_emails(input_data))

print("URLs:", extract_urls(input_data))

print("Phone Numbers:", extract_phone_numbers(input_data))

print("Credit Cards:", extract_credit_cards(input_data))

print("Time Formats:", extract_time(input_data))


### **Expected Output**
Emails: ['support@example.com']
URLs: ['https://www.example.com']
Phone Numbers: ['(123) 456-7890', '123-456-7890']
Credit Cards: ['1234-5678-9012-3456']
Time Formats: ['14:30', '2:30 PM']
