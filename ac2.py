class flashcard:
    def __init__(self,w,m):
        self.w=w 
        self.m=m
    def __str__(self):
        return self.w + "-" + self.m
    
f=[]
while True:
    w=input("Enter the word in a flashcard:")
    m=input("Enter its meaning in a flashcard:")
    f.append(flashcard(w,m))
    op=int(input("Write 0 to add new ,else write 1:"))
    if op:
        break

print("Your flashcards:")
for i in f:
    print("->",i)