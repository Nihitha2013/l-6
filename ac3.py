import random
class friutclass:
    def __init__(self):
        self.fruits={'watermelon':'green',
                     'apple':'yellow',
                     'grapes' : 'black',
                     'pineapple' : 'yellow',
                     'mango' : 'yellow'
                     }
        
    def quiz(self):
        while True:
            fr, col=random.choice(list(self.fruits.items()))

            print("What is the color of",fr)
            u_a=input()

            if(u_a.lower() == col):
                print("Correct answer")
            else:
                print("Wrong answer")

            option=int(input("Write 0 to add new otherwise write 1:"))
            if (option):
                break

print("Welcome to friut quiz")
obj=friutclass()
obj.quiz()
        
