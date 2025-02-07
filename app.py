#print('Hello Ntsako') 

#name = input("What's your name?")
#age = input('How old are you?')

#print("Hey Ntsako" + name)
#print("You are 30" + age + "?")

#conditional statement#

#X = 2

#if X > 2:
    #print("you've gotten only 23")
#elif X ==5:
    #print("gotten just 2")
    
#lse:X
#print("such a low score")

#age = 18
#has_id = True

#if age >= 18 and has_id == "yes":
    #print("Access granted.")

#else:
    #print("Access denied. You must be at least 18 years old.")
    
age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have an ID? (yes/no): ")
    
    if has_id == "yes":
        print("Access granted.")
    else:
        print("Access denied. You need an ID.")
else:
    print("Access denied. You must be at least 18 years old.")
    

    

