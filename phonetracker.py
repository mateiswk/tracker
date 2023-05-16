import phonenumbers

# Validating a phone number
phone_number = "+40787836511"
isValid = phonenumbers.is_valid_number(phonenumbers.parse(phone_number))
print(isValid) # Output: True

# Formatting a phone number
formatted_number = phonenumbers.format_number(phonenumbers.parse(phone_number), phonenumbers.PhoneNumberFormat.NATIONAL)
print(formatted_number) # Output: (650) 253-0000
