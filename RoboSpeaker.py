import pyttsx3

Robo = pyttsx3.init()
print("Welcome to Robospeaker 1.1 Created by alok singh gusain")

while True:

  user_input = input("Enter what you want to speak(0 to exit) : ")

  if user_input == "0":
    break
  else:
    print(user_input)
    Robo.say(user_input)
    Robo.runAndWait()