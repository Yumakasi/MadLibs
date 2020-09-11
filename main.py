import random

TCOL =  '\033[33m' 
TWHITE = '\033[37m'

def story1():
 print('chose story 1');
 name = input("Enter a Name:");
 color = input("Pick a color, any color:");
 animal = input("Pick a animal:");
 place = input("Enter name of a place:");
 print ("On one sunny day, " + TCOL + name + TWHITE + " went to the park to feed some ducks at the pond. Upon arriving at the pond, " + TCOL + name + TWHITE + " spotted a " + TCOL + color +  " " + TCOL + animal + TWHITE + ". " + TCOL + name + TWHITE + " never seen an animal like this before and wanted to go over and pet it. but the " + TCOL + animal + TWHITE + " got startled and fled to " + TCOL + place + TWHITE + " within seconds." + TWHITE )
def story2():
 print('chose story 2')
 name = input("Enter a Name:");
 namo = input("Input another name:");
 place = input("Make up a name for a city:");
 monster = input("Type of of mythical creature:");
 print(TCOL + name + TWHITE +  " is a famous movie director. They're the one who made that amazing movie about the brave protagonist, " + TCOL + namo + TWHITE + ", defending the city of " + TCOL + place + TWHITE + " from the giant, terrifying " + TCOL + monster + TWHITE + "." + TWHITE)

def randy():
 print('randomized')

def storypicker(sc):
 if sc == "story 1":
   story1()
 elif sc == "story 2":
   story2()
 elif sc == "random":
   randy()
   rand = random.randint(1,2)
   if rand == 1:
     story1()
   elif rand == 2:
     story2()

def main():
  print("Welcome Player! Please pick a story by typing in story 1 or story 2 or random.");
  Choice = input("Enter Here:");
  storypicker(Choice)
print (main())

