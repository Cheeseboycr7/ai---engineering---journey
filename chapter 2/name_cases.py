###Personal Message: Store a person’s name in a variable, and print a mes
#sage to that person . Your message should be simple, such as, “Hello Eric, 
#would you like to learn some Python today?”

name = 'Mandla'
message = (
    f'Hello {name} would you like to learn some Python today'
)
#print(message)

## Name Cases: Store a person’s name in a variable, and then print that per
#son’s name in lowercase, uppercase, and titlecase 

lower = name.lower()
upper = name.upper()
title = name.title()

#print(lower)
#print(upper)
#print(title)
#print(name)


#2-5. Famous Quote: Find a quote from a famous person you admire . Print the 
#quote and the name of its author . Your output should look something like the 
#following, including the quotation marks:

qoute = (
    f"Albert Einstein once said,\n“A person who never made a \nmistake never tried anything new.”"
)

#print(qoute)

# Avoiding Type Errors with the str() Function
# you cant combine string with int

age = str(23)
message = "Happy " + age + "rd Birthday!"
print(message)