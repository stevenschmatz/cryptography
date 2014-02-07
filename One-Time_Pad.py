import binascii

class OneTimePad:
	"""A simple toy cryptosystem"""
	def __init__(self, key):
		self.key = int(key, 2) #sample 7-digit binary string
		self.test_message = "Hello! How are you doing today?"

	def Encode(self, string):
		return ' '.join(str(int(format(ord(x)))^self.key) for x in string)

	def Return_Int_List(self, space_separated_string):
		string_list = space_separated_string.split(' ')
		num_list = []
		for num in string_list:
			num_list.append(int(num))
		return num_list

	def Get_Encoded_String(self, string):
		num_list = self.Return_Int_List(string)
		return ''.join(chr(x) for x in num_list)

	def Get_Chars(self, encrypted_message):
		return " ".join([str(ord(x)) for x in encrypted_message])

	def Decode(self, string):
		num_list = self.Return_Int_List(string)
		decoded_list = [x^self.key for x in num_list]
		return "".join(map(chr, decoded_list))

	def Encrypt_Message(self, plain_text):
		return self.Get_Encoded_String(self.Encode(plain_text))

	def Decrypt_Message(self, encrypted_message):
		return self.Decode(self.Get_Chars(encrypted_message))

Cryptosystem = OneTimePad('0001010') #Default '0001010', Enter the 7 digit binary key that is shared between both users
"""NOTE: Some binary keys introduce non-escaped quotation marks, which break the program when copied and pasted"""

message = "My name is Steven Schmatz and this is my original message."

print Cryptosystem.Encrypt_Message(message)
print Cryptosystem.Decrypt_Message(Cryptosystem.Encrypt_Message(message))
