print("welcome player")
print('welcome to the story, it is currently midnight and you are very tired, but you remember that you have a project')
choice1 = input("do you [sleep] or do you're [project]") 
if choice1 == 'sleep':
  print("you don't do the project and go to sleep")
  choice1=input('You wake up, do you make an [excuse] to not go to school or [show up] without the project?')
if choice1 == 'excuse':
  print('You make an excuse to stay home and you finish the project. (THE END)')
elif choice1 == "show up":
  print("You show up without the project and get a F in the class.(THE END)")
elif choice1 == "project":
  print("you finish you're project but go to sleep at 4AM")
  choice1=input('you wake up do you [sleep] in or go to [school] tired')
if choice1 == 'sleep':
  print("you sleep in and wake up at 1 PM")
  choice1=input('do you go to [school late] or [stay home]')
  if choice1=='school late':
   choice1a=input('You go to school late and get in school suspension for 2 days since you’ve been consistently late for the whole school year. (THE END)')
elif choice1 == "stay home":
  print("You stay at home and end up getting expelled from school since you’ve been missing school and been consistently late.(THE END)")
