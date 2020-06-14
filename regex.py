import re
import pyperclip


class Regex:
	def __init__(self):
		self.input_string = ''

	@property
	def find_phone_number(self):
		phone_regex = re.compile(r'''(
			# 415-555-000, +880-1521-433-158
			(([+]\d\d\d)|				#area code starting with +
			(\d\d\d))?    				# area code without starting +
			([ ]|-)                 	# separator
			((\d{4}) | (\d{3}))?    	# first 3 digits or first 4 digits
			([ ]|-)?                    	# separator
			((\d{6}) | (\d{4}) |(\d{3}))?      				# last 3 digits or middle 3 digits
			([ ]|-)?						# separator
			((\d{4}) | (\d{3}))?        # last 4 digits
			)''', re.VERBOSE)
		result = phone_regex.findall(self.input_string)
		all_phone_number = []
		for phn_number in result:
			if len(phn_number[0]) >= 12:
				all_phone_number.append(phn_number[0])
		return all_phone_number

	@property
	def validate_email(self):
		email_regex = re.compile(r'''(
					[a-zA-Z0-9._%+-]+       # username
					@						# @ symbol
					[a-zA-Z0-9.-]+          # domain name
					(\.[A-Za-z]{2,4})
					)''', re.VERBOSE)
		result = email_regex.findall(self.input_string)

		return result

	def find_vowels(self):
		rx = re.compile(r'[aeiouAEIOU]')
		result = rx.findall(self.input_string)
		return result

	def find_consonants(self):
		rx = re.compile(r'[^aeiouAEIOU ]')
		result = rx.findall(self.input_string)
		return result


if __name__ == '__main__':
	# while True:
	obj = Regex()
	# Get the text off the clipboard.
	obj.input_string = str(pyperclip.paste())

	# Find all phone numbers and email addresses in the text.
	phone_numbers = obj.find_phone_number
	emails = obj.validate_email
	print("Vowels : ", obj.find_vowels())
	print("Consonants : ", obj.find_consonants())
	extracted_phone_email = {"Phone No": [], "Email": []}
	for number in phone_numbers:
		extracted_phone_email["Phone No"].append(number.strip())
	for email in emails:
		extracted_phone_email["Email"].append(email[0])

	# Copy phone number to the clipboard.
	if len(extracted_phone_email["Phone No"]) > 0:
		pyperclip.copy('\n'.join(extracted_phone_email["Phone No"]))
		print('Copied phone number to clipboard:')
		print('\n'.join(extracted_phone_email["Phone No"]))
	else:
		print('No phone numbers found.')

	# Copy emails to the clipboard.
	if len(extracted_phone_email["Email"]) > 0:
		pyperclip.copy('\n'.join(extracted_phone_email["Email"]))
		print('Copied emails to clipboard:')
		print('\n'.join(extracted_phone_email["Email"]))
	else:
		print('No email found.')
