from googletrans import Translator
import time
import random
translator = Translator()
class Japanese():
    def driver(self):
        x = True
        review = False
        learn = False
        mistakes = False
        while x:
            choice = input("Would you like to learn new words, correct past mistakes, or review old words? ")
            if choice == "review":
                review = True
                x = False
            elif choice == "learn":
                learn = True
                x = False
            elif choice == "correct":
                mistakes = True
                x = False
            else:
                print("Please respond with either \"learn\" or \"review\" or \"correct\"!")

        num = int(self.getNum(choice))
        if review:
            self.reviewEKB(num)
        elif learn:
            self.learnEKB(num)
        elif mistakes:
            self.mistakes(num)


    def getNum(self, choice):
        # RL = "review" or "learn"***
        num = input("How many words would you like to " + choice + "? ")
        return(num)

    def mistakes(self, num):
        score = 0
        jToE = {}
        with open('mistakes.txt') as f:
            contents = f.readlines()
            f.close()
        if len(contents)<num:
            print("you cannot correct", num, "mistakes! You only have", len(contents), "mistakes left to correct!")
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

                with open('mistakes.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                

                with open("learned.txt", "a") as f:
                    f.writelines(eWord)
                    f.close()

                with open("mistakes.txt") as f:
                    contents = f.readlines()
                    f.close()

            else:
                print("You were incorrect. The correct answer was " + eWord)
                print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")
                
        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

    def learnEKB(self, num):
        # executes the learn function from learning.py and if you get it correct it is added to the learned learned.txt file
        score = 0
        jToE = {}
        with open('unseen.txt') as f:
            contents = f.readlines()
            f.close()
        if len(contents)<num:
            print("you cannot learn", num, "new words! There are only", len(contents), "words left to learn!")
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

                with open('unseen.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                
                with open("learned.txt", "a") as f:
                    f.writelines(eWord)
                    f.close()
                with open("unseen.txt") as f:
                    contents = f.readlines()
                    f.close()

            else:
                print("You were incorrect. The correct answer was " + eWord)
                print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")
                with open('unseen.txt', 'w') as f:
                    for i in contents:
                        if i != str(eWord):
                            f.writelines(i)
                    f.close()
                with open("mistakes.txt", "a") as f:
                    f.writelines(eWord)
                    f.close()
                with open("unseen.txt") as f:
                    contents = f.readlines()
                    f.close()
                
                
        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

    def reviewEKB(self, num):
        # executes the JKBFalseQuiz from JQuiz but engcore100.txt is replaced with learned.txt and if you get one wrong it is moved to mistakes.txt
        score = 0
        jToE = {}
        with open('learned.txt') as f:
            contents = f.readlines()
            f.close()
        if len(contents)<num:
            print("you cannot review", num, "words! You have only learned", len(contents), "words!")
            exit()
        nums = self.numNums(num, 0, len(contents)-1)
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
                with open("mistakes.txt", "a") as f:
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


japanese = Japanese()
japanese.driver()