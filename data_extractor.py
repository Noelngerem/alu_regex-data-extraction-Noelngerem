import re

# here wa are going to define regular expressions for each type of the data
def extract_emails(text):
    return re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

def extract_urls(text):
    return re.findall(r"https?://[\w.-]+\.\w+(?:/[\w.-]*)?", text)

def extract_phone_numbers(text):
    return re.findall(r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}", text)

def extract_credit_cards(text):
    return re.findall(r"\b(?:\d{4}[-\s]?){3}\d{4}\b", text)

def main():
    try:
        with open("test_input.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("Error: 'test_input.txt' file not found.")
        return

    emails = extract_emails(data)
    urls = extract_urls(data)
    phones = extract_phone_numbers(data)
    cards = extract_credit_cards(data)

    with open("test_output.txt", "w") as out:
        out.write("Emails:\n")
        if emails:
            for email in sorted(emails):
                out.write(f"- {email}\n")
        else:
            out.write("- None found\n")

        out.write("\nURLs:\n")
        if urls:
            for url in sorted(urls):
                out.write(f"- {url}\n")
        else:
            out.write("- None found\n")

        out.write("\nPhone Numbers:\n")
        if phones:
            for phone in sorted(phones):
                out.write(f"- {phone}\n")
        else:
            out.write("- None found\n")

        out.write("\nCredit Card Numbers:\n")
        if cards:
            for card in sorted(cards):
                out.write(f"- {card}\n")
        else:
            out.write("- None found\n")

    print("Data extracted successfully. Check 'test_output.txt'.")

if __name__ == "__main__":
    main()