import re


class Regex:
	def __init__(self):
		self.input_string = ''

	def find_phone_number(self, pattern):
		rx = re.compile(pattern)
		result = rx.findall(self.input_string)
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
	obj = Regex()
	obj.input_string = input("Enter string to find something...\n")
	pattern = input("Enter a pattern in which you want to search...\n")
	print("Phone Number : ", obj.find_phone_number(pattern))
	print("Vowels : ", obj.find_vowels())
	print("Consonants : ", obj.find_consonants())
