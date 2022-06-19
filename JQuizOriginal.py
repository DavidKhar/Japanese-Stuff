from googletrans import Translator
import random
##
translator = Translator()
class Quiz():
    def japaneseQuiz(self, bottom, top, questions, JKB):
        score = 0
        with open('engcore1000.txt') as f:
            contents = f.readlines()
            f.close()

            if JKB:
                for i in range(questions):
                    eWord = contents[random.randint(bottom, top)]
                    jWord = translator.translate(eWord, dest="japanese").text
                    if i % 2 == 0:
                        userAnswer = input("translate " + eWord + " into Japanese: ")
                        
                        if translator.translate(userAnswer).text == translator.translate(jWord).text:
                            print("You are correct!")
                            score+=1

                        else:
                            print("You were incorrect. The correct answer was " + jWord)
                            
                    else:
                        userAnswer = input("translate " + jWord + " word into English: ")

                        if translator.translate(userAnswer, dest="japanese").text == translator.translate(eWord, dest="japanese").text:
                            print("You are correct!")
                            score+=1

                        else:
                            print("You were incorrect. The correct answer was " + eWord)
                
        # the error is that it thinks that the translated version and the user inputted version which are equal are not equal (line 44) and always goes to the else statement [FIXED I THINK?]
            else:       
                for i in range(questions):            
                    eWord = contents[random.randint(bottom, top)]
                    jWord = translator.translate(eWord, dest="japanese").text
                    userAnswer = input("translate " + jWord + " word into English: ")
                        
                    if str(translator.translate(userAnswer, dest="japanese").text) == jWord:
                        print("You are correct! The answer was " + eWord)
                        score+=1
                            
                    else:
                        print("You were incorrect. The correct answer was " + eWord)
                        print("Your answer meant", translator.translate(userAnswer, dest="japanese").text, "in Japanese.")

        print(self.scoreMessage(score * 100/questions), "You scored a", score/questions * 100, "percent!")
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
questions = 5
quiz.japaneseQuiz(bottom, top, questions, True)