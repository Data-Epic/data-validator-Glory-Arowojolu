# DataValidator

This is a python package that allows users to validate different types of data (emails, phone numbers, dates and url).


## Installation
Install the package using:

```
pip install DataValidator
```

## Usage
Here is how to use the Data Validator:

```
from datavalidator.validator import DataValidator

validator = DataValidator()

Email Validation
print(validator.validate_email("aroglobal1@gmail.com"))

Phone Number Validation
print(validator.validate_phone("+2348167805789")) 

Date Validation
print(validator.validate_date("10-07-2020")) 

URL Validation
print(validator.validate_url("https://www.google.com"))
```


## Contributing
Contributions are welcome. To do this:
1. Fork the repository
2. Create a new branch
3. Make and commit changes
4. Push to the branch
5. Create a pull request

## License
This project is licensed under the **MIT License**.

## Author

Glory Arowojolu
Email: aroglobal1@gmail.com


