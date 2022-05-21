str1 = 'Hello World! This is my python class. '
str2 = 'Welcome\t to MY house'
str3 = 'i just love this course!'
# capitalize() : Converts the first character to upper case
str_out = str1.capitalize()
print(str_out, '>>capitalize()')
# casefold() : Converts string into lower case
str_out = str1.casefold()
print(str_out, '>>casefold()')
# center() : Returns a centered string
str_out = str3.center(35, '*')  # returns the centered padded string of length 35
print(str_out, '>>center()')
# count() : Returns the numbers of times a specified value occurs in a string
str_out = str3.count('o')
print("Number of occurrence of 'p' is ", str_out, '>>count()')
# encode() : Returns an encoded version of the string
str_out = str3.encode()  # change encoding to utf-8
print(str_out, '>>encode()')
# endswith() : Returns true if the string ends with the specified value
str_out = str2.endswith('house')
print(str_out, '>>endswith()')
# expandtabs() : Sets the tab size of the string
str_out = str2.expandtabs(2)
print(str_out, '>>expandtabs()')
# find() : Searches the string for a specified value and returns the position of where it was found
str_out = str1.find('is')
print("The position of 'is' ", str_out, '>>find()')
# format() : Formats specified values in a string
txt = "It's only {price:.2f} dollars!"
str_out = txt.format(price=23)
print(str_out, '>>format()')
# format_map() : Formats specified values in a string
dict = {'x':10, 'y': 30}
print('{x} {y}'.format_map(dict), '>>format_map()')
# index() : Searches the string for a specified value and returns the position of where it was found
str_out = str2.index('MY')
print(str_out, '>>index()')
# isalnum() : Returns True if all characters in the string are alphanumeric
str_out = str2.isalnum()
print(str_out, '>>isalnum()')
# isalpha() : Returns True if all characters in the string are in tha alphabet
str_out = str1.isalpha()
print(str_out, '>>isalpha()')
# isascii() : Returns True if all characters in the string are ascii characters
str_out = str3.isascii()
print(str_out, '>>isascii()')
# isdecimal() : Returns True if all characters in the string are decimals
str_out = str3.isdecimal()
print(str_out, '>>isdecimal()')
# isdigit() : Returns True if all characters in the string are digits
str_out = str1.isdigit()
print(str_out, '>>isdigit()')
# isdentifier() : Returns True if the string is an identifier
txt = 'Python'
str_out = txt.isidentifier()
print(str_out, '>>isidentifer()')
# islower() : Returns True if all characters in the string are lower case
str_out = str1.islower()
print(str_out, '>>islower()')
# isumeric() : Returns True if all characters in the string are numeric
str_out = str1.isnumeric()
print(str_out, '>>isnumeric()')
# ispritable() : Returns True if all characters in the string are printable
str_out = str2.isprintable()
print(str_out, '>>isprintable()')
# isspace() : Returns True if all characters in the string are whitespaces
txt = '  '
str_out = txt.isspace()
print(str_out, '>>isspace()')
# isupper() : Returns True if all characters in the string are upper case
str_out = str1.isupper()
print(str_out, '>>isupper()')
# join() : Returns a left justified version of the string
str_list = ['John', 'Peter', 'Vicky']
str_out = ' @ '.join(str_list)
print(str_out, '>>join()')
# ljust() : Returns a left justified version of the string
string = 'cat'
width = 6
fillchar = '&'
print(string.ljust(width, fillchar), '>>ljust()')
# rjust() : Returns a right justified version of the string
string = 'cat'
width = 6
fillchar = '$'
print(string.rjust(width, fillchar), '>>rjust()')
# lower() : Converts a string into lower case
str_out = str1.lower()
print(str_out, '>>lower()')
# lstrip() : Returns a left trim version of the string
string = '     that is a good idea     '
str_out = string.lstrip()
print(str_out, '>>lstrip()')
# rstrip() : Returns a right trim version of the string
string = '     that is a good idea     '
str_out = string.rstrip()
print(str_out, '>>rstrip()')
# strip() : Returns a trimmed version of the string
string = '     that is a good idea     '
str_out = string.strip()
print(str_out, '>>strip()')
# maketrans() : Returns a translation table to be used in translations
dict = {'a': '1234', 'b': '5678', '$': '1010'}
string = ''
print(string.maketrans(dict), '>>maketrans()')
# partition() : Returns a tuple where the string is parted into three parts
str_out = str1.partition('my')
print(str_out, '>>partition()')
# replace() : Returns a string where a specified value is replaced with a specified value
txt = 'bat ball boy'
str_out = txt.replace('b', 'c')
print(str_out, '>>replace()')
# rfind() : Searches the string for a specified value and returns the last position of where it was found
# rindex() == rfind()
str_out = str1.rfind('World')
print(str_out, '>>rfind()')
# split() : Splits the string at the specified separator, and returns a list
# rsplit() == split()
str_out = str1.split(' ')
print(str_out, '>>split()')
# splitlines() : Splits the string at line breaks and returns a list
str_out = str1.splitlines()
print(str_out, '>>splitlines()')
# startswith() : Returns true if the string starts with the specified value
str_out = str3.startswith('i')
print(str_out, '>>startswith()')
# swapcase() : Swaps cases, lower case becomes upper case and vice versa
str_out = str2.swapcase()
print(str_out, '>>swapcase()')
# title() : Converts the first character of each word to upper case
str_out = str1.title()
print(str_out, '>>title()')
# translate() : Returns a translated string
dict = {83: 80}  # ascii 83(S) 80(P)
txt = 'Hello Sam!'
print(txt.translate(dict), '>>translate()')
# upper() : Converts a string into upper case
str_out = str1.upper()
print(str_out, '>>upper()')
# zfill() : Fills the string with a specified number of 0 values at the beginning
txt = 'Program is fun'
str_out = txt.zfill(20)
print(str_out, '>>zfill()')
