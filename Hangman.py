import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
list1=["request","please","saviour","chance","help","save me","java","postgre","Python"]
cg = random.choice(list1)
print(cg)
blank =[]
a= len(cg)
live =6
for i in range(a):
  blank += "_"
print (blank)
count_underscore= blank.count("_")
while count_underscore !=0:
  lg = input("\nguess a letter:- ").lower()
  if lg in blank:
    print("you have already guessed this letter, guess the remaining letters")
  for i in range(a):
    letter = cg[i]
    if lg == letter:
      blank[i] = lg
  if lg  not in cg:
    live -=1
    print(f"you lost a life \nyou left with {live} lifes")
    if live == 0:
      count_underscore =0
      print(" \ngame end")
  if '_' not in blank:
    count_underscore = 0
    print("game win")
    
  print(f"{' '.join(blank)}")
  print(stages[live])
