# 2.3 Personal Message
person_name = 'Ann'
message = f'Hello {person_name}, would you like to learn some Python today?'
print(message)

#2.4 Name Cases
print(person_name)
print(person_name.upper())
print(person_name.lower())
print(person_name.title())

# 2.5 Famous Quote
famous_quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”' 
print(famous_quote)

#2.6 Famous Quote 2
famous_person = 'Albert Einstein'
quote = 'once said, "A person who never made a mistake never tried anything new."'
print(f'{famous_person} {quote}')

#2.7 Stripping Names
person_name = ' Ann\n'
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

#2.8 File Extensions
filename ='Python_notes.txt'
print(filename)
removed_suffix = filename.removesuffix('.txt') 