from googletrans import Translator
import time
import random
##
translator = Translator()
class Teach():
    def numNums(self, num, bottom, top):
        nums = set()
        while len(nums) < num:
            nums.add(random.randint(bottom, top))
        return nums
            
    def learn(self, num, bottom, top):
        score = 0
        jToE = {}
        with open('engcore1000.txt') as f:
            contents = f.readlines()
            f.close()
        nums = self.numNums(num, bottom, top)

        for i in nums:
            eWord = contents[i]
            jWord = translator.translate(contents[i], dest="japanese").text
            print(jWord, "=", eWord)
            jToE[jWord] = eWord
            time.sleep(4)
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

        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!")
    def scoreMessage(self, score):
        print(score)
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
        
teach = Teach()
teach.learn(10, 900, 998)
        


