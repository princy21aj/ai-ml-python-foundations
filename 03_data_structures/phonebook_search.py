#this program searches for a name and returns the phone number

def phone_book(book,value):
        if value in book:
            return book[value]
        else:
            return "Not found"
        
phonebook ={
    "eva":12423,
    "jack":14324,
    "alice":44756,
    "isha":87644,
    "john":66479
   }

name = (input("Enter your name :"))
check = phone_book(phonebook,name)

print(f"name : {name} \nnumber : {check}")





