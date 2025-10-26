#Conditional Statement : if, else, elseif (elif)

bill_total = 100
discount = 10

if (bill_total < 100):
	print("Bill Total is less than 100")
elif(bill_total > 100):
	bill_total -= discount
	print("Bill Total is greater than 100. Discount has been applied")
else:
	print("Bill Total is 100")


# Another example. Let say light is currently off

current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')


#Match statement
day = "Friday"
match day:
	case "Monday":
		print("Today is Monday. Beginning of week")
	case "Friday" :
		print("Issa Friiidayyy")
	case "Saturday" | "Sunday": #The | is representing an or condition in a match statement as would be in if else or
		print("Almost mondayyyy")
	case *_:
		print("unknown ")


