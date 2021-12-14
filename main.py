print("welcome player")
print('welcome to the story, it is currently midnight and you are very tired, but you remember that you have a project')
choice1 = input("do you [sleep] or do you're [project]") 
if choice1 == 'sleep':
  print("you don't do the project and go to sleep")
elif choice1 == "project":
  print("you finish you're project but go to sleep at 4AM")
  choice1=input('you wake up. do you [sleep] in or go to [school] tired')
if choice1 == 'sleep':
  print("you sleep in and wake up at 1 PM")
  choice1=input('do you go to [school late] or [stay home]')
  if choice1=='sleep in':
   choice1a=input('you wake up do you make an [excuse] to not go to school, or [show up] without the  project')
  if choice1a == 'excuse':
    print("you make an excuse to stay home and you finish the project.THE END") 