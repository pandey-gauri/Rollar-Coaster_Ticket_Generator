print("Welcome to the RollerCoaster Ticket Counter.")
height=int(input("What is your height in cm?\n"))
bill=0
if(height>=120):
  print("You can ride the RollerCoaster.")
  age=int(input("What is your age?\n"))
  if(age<12):
    bill=5
    print("You have to pay $5.")
  elif(12<age<18):
    bill=7
    print("You have to pay $7.")
  else:
    bill=12
    print("You have to pay $12.")
  photo=input("Do you want a photo taken? Y or N.\n")
  if(photo=="Y"):
    print("You have to pay $3 extra.")
    bill+=3
  print(f"Your final bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.")