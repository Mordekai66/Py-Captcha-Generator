import pyttsx3
digits_char = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[1].id)
for i in digits_char:
    engine.save_to_file(i, rf"path\to\voice\dir\{i}.wav")
engine.runAndWait()
