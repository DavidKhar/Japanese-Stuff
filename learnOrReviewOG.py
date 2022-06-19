from googletrans import Translator
import time
import random
translator = Translator()
class Japanese():
    def driver(self):
        x = True
        review = False
        learn = False
        while x:
            choice = input("Would you like to learn new words or review old words? ")
            if choice == "review":
                review = True
                x = False
            elif choice == "learn":
                learn = True
                x = False
            else:
                print("Please respond with either \"learn\" or \"review\"!")
        num = int(self.getNum(choice))
        if review:
            self.review(num)
        elif learn:
            self.learnEKB(num)


    def getNum(self, choice):
        # choice = "review" or "learn"***
        num = input("How many words would you like to " + choice + "? ")
        return(num)

    def learnEKB(self, num):
        # executes the learn function from learning.py and if you get it correct it is added to the learned learned.txt file
        score = 0
        jToE = {}
        with open('new.txt') as f:
            contents = f.readlines()
            f.close()
        if len(contents)<num:
            print("you cannot learn", num, "new words! There are only", len(contents), "words left to learn! (" + contents + ")")
            exit()
        nums = self.numNums(num, 0, len(contents)-1)
        for i in nums:
            eWord = contents[i]
            jWord = translator.translate(contents[i], dest="japanese").text
            jToE[jWord] = eWord
            print(jWord, "=", eWord)
            time.sleep(4)
        for i in jToE:
            jWord = i
            eWord = jToE[i]
            userAnswer = input("translate " + jWord + " word into English: ")
            if str(translator.translate(userAnswer, dest="japanese").text) == jWord:
                print("You are correct! The answer was " + eWord)
                score+=1

                with open('new.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                
                with open('new.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                with open("learned.txt", "a") as f:
                    f.writelines(eWord)
                    f.close()
                with open("new.txt") as f:
                    contents = f.readlines()
                    f.close()

            else:
                print("You were incorrect. The correct answer was " + eWord)
                print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")
                
        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

    def reviewEKB(self, num):
        # executes the JKBFalseQuiz from JQuiz but engcore100.txt is replaced with learned.txt and if you get one wrong it is moved to new.txt
        score = 0
        jToE = {}
        with open('learned.txt') as f:
            contents = f.readlines()
            f.close()
        if len(contents)<num:
            print("you cannot review", num, "words! You have only learned", len(contents), "words! (" + contents + ")")
            exit()
        nums = self.numNums(num, 0, len(contents)-1)
        print(nums)
        for i in nums:
            eWord = contents[i]
            jWord = translator.translate(contents[i], dest="japanese").text
            jToE[jWord] = eWord
        for i in jToE:
            jWord = i
            eWord = jToE[i]
            userAnswer = input("translate " + jWord + " word into English: ")
            if str(translator.translate(userAnswer, dest="japanese").text) == jWord:
                print("You are correct! The answer was " + eWord)
                score+=1
                    
            else:
                print("You were incorrect. The correct answer was " + eWord)
                print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")
                with open('learned.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                with open("new.txt", "a") as f:
                    f.writelines(eWord)
                    f.close()
                with open("learned.txt") as f:
                    contents = f.readlines()
                    f.close()

        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

        

    def scoreMessage(self, score):
        if score <= 50:
            return("Better luck next time!")
        elif score <= 65:
            return("Nice try!")
        elif score <= 80:
            return("Great job!")
        elif score <=90:
            return("Almost perfect!")
        elif score <=100:
            return("Perfect!")

    def numNums(self, num, bottom, top):
        nums = set()
        while len(nums) < num:
            nums.add(random.randint(bottom, top))
        return nums

    def getChoices(self, correctAnswer, max, contents):
        pass





japanese = Japanese()
japanese.driver()