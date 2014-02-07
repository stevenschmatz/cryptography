import binascii

key = int('0001010', 2) #sample 7-digit binary string

message = "Hello! How are you doing today?"

encrypted_message = 'Boffe+*Be}*kxo*se*necdm*~enks5'

def Encrypt(string):
	return ' '.join(str(int(format(ord(x)))^key) for x in string)

def Return_Int_List(space_separated_string):
	string_list = space_separated_string.split(' ')
	num_list = []
	for num in string_list:
		num_list.append(int(num))
	return num_list

def Get_Encoded_String(string):
	num_list = Return_Int_List(string)
	return ''.join(chr(x) for x in num_list)

def Get_Chars(encrypted_message):
	return " ".join([str(ord(x)) for x in encrypted_message])

def Decode(string):
	num_list = Return_Int_List(string)
	decoded_list = [x^key for x in num_list]
	return "".join(map(chr, decoded_list))

print Get_Encoded_String(Encrypt('Hello! How are youaWFE POIFEJWFOIWEJ F8238942110!!! doing today?'))

print Decode(Get_Chars(encrypted_message))