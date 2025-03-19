import re

from datetime import datetime

class DataValidator:
    def __init__(self):
        pass

    def validate_email(self, email):
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+' # regex to check valid email
        if not email: 
            return False
        
        if re.match(email_pattern, email):
            return email
        else:
            raise ValueError("Invalid email format.")

    def validate_phone(self, phone):
        phone_pattern = r'\+(\d{3})\d{10}'
   
# If the phone is empty return false
        if not phone:
            return False

    # Return the phone if it matched the Regex
        if re.match(phone_pattern, phone):
            return phone
        else:
            raise ValueError("Invalid phone format.")

    def validate_date(self, date):
        date_pattern = r'(0[1-9]|[12][0-9]|3[01])(\/|-)(0|[1-9]|1[1,2])(\/|-)(19|20)\d{2}'
    # If the date is empty return false
        if not date:
            return False

    # Return the date if it matched the Regex
        if re.match(date_pattern, date):
            return date
        else:
            raise ValueError("Invalid date format.")

    def validate_url(self, url):
        url_pattern=  r'https?://(www\.)?(\w+)(\.\w+)'
    # If the url is empty return false
        if not url:
            return False

    # Return the url if it matched the Regex
        if re.match(url_pattern, url):
            return url
        else:
            raise ValueError("Invalid url format.")
