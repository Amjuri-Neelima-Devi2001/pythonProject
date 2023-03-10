# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Neel:
    def __init__(self,name,dob,skills):
        self.name=name
        self.dob=dob
        self.skills=skills
    def watch(self):
        print(f"{self.name} likes watching movies")
    def trick(self):
        print(f"many tricks have used to do {self.skills}")
p=Neel("neelima",272001,"python")
p.watch()
p.trick()
class Devi:
    def __init__(self,likes,dislikes):
        self.likes=likes
        self.dislikes=dislikes
    def walk(self):
        print(f"{self.likes} is fav")
    def sleep(self):
        print(f"{self.dislikes} is not fav")
m=Devi('chess','outsidegames')
m.walk()
m.sleep()