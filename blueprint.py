from googletrans import Translator
##
translator = Translator()

translated_text = translator.translate('こんにちは')
print(translated_text.text)

translated_text = translator.translate('こんにちは', dest='french')
print(translated_text.text)


translated_text = translator.translate('hello', dest='japanese')
print(translated_text.text)

translated_text = translator.translate('veritas lux mea', src='latin')
print(translated_text.text)

print("Welcome to today's Quiz, David!")
#Create a dictionary
val = input