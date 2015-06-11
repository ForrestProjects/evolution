__author__ = 'dion the amazing'
import time
import random

class guesser:
    def __init__(self, name):
        self.name = name
        self.guesses = 1


    def guess(self):
            self.guessed = attempt()
            t = correct(self.guessed, self.name, self.guesses)
            self.guesses = self.guesses + 1
            time.sleep(0.2)
            if t == True:
                return True
            else:
                return False

def attempt():
    y = random.randint(1,100)
    return y

def correct(y, name, guesses):
    x = 88
    if y == x:
        print("Correct" , name, "guessed 88 in", guesses, "attempts")
        return True
    else:
        print(name, "Guessed", y)
        return False

def main():
    g1 = guesser("Dion")
    g2 = guesser("Bob")
    x = False
    people = [g1,g2]
    while(x == False):
        for i in range(0,len(people)):
            x = people[i].guess()
            if x == True:
                break;

if __name__ == '__main__':
    main()