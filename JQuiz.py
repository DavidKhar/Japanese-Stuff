from googletrans import Translator
import random
##
translator = Translator()
class Quiz():
    def JKBFalseQuiz(self, num, bottom, top):
        score = 0
        jToE = {}
        with open('engcore1000.txt') as f:
            contents = f.readlines()
            f.close()
        nums = self.numNums(num, bottom, top)

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

        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

    def JKBTrueQuiz(self, num, bottom, top):
        count = 0
        score = 0
        jToE = {}
        eToJ = {}
        with open('engcore1000.txt') as f:
            contents = f.readlines()
            f.close()
        nums = self.numNums(num, bottom, top)

        for i in nums:
            eWord = contents[i]
            jWord = translator.translate(contents[i], dest="japanese").text
            jToE[jWord] = eWord
            eToJ[eWord] = jWord

        for i in jToE:
            jWord = i
            eWord = jToE[i]
            if count % 2 == 0:
                userAnswer = input("translate " + jWord + " into English: ")
                if str(translator.translate(userAnswer, dest="japanese").text) == jWord:
                    print("You are correct! The answer was " + eWord)
                    score+=1
                        
                else:
                    print("You were incorrect. The correct answer was " + eWord)
                    print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")
            else:
                userAnswer = input("translate " + eWord + " into Japanese: ")
                if str(translator.translate(userAnswer).text) == eWord or translator.translate(userAnswer).text == translator.translate(jWord).text or translator.translate(userAnswer).text == translator.translate(eWord).text:
                    print("You are correct! The answer was " + jWord)
                    score+=1
                        
                else:
                    print("You were incorrect. The correct answer was " + jWord)
                    print("Your answer meant", translator.translate(userAnswer).text, "in English.")
            count+=1

        print(self.scoreMessage(score * 100/num), "You scored a", score/num * 100, "percent!") 

    def numNums(self, num, bottom, top):
        nums = set()
        while len(nums) < num:
            nums.add(random.randint(bottom, top))
        return nums

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
quiz = Quiz()
bottom = 0
top = 10
questions = 10
quiz.JKBFalseQuiz(questions, bottom, top)