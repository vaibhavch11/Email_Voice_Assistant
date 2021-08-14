import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server_login_mail = "chauhanvaibhav1105@gmail.com"
server_login_password = "Vaibhav1105"

server.login(server_login_mail,server_login_password)




def say(text):
    engine.say(text)
    engine.runAndWait()
    


def assistant_listener():
    try:
        with sr.Microphone() as source:
            
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=2)
           
            info = listener.recognize_google(voice, language="en-in").lower()
            return info

    except:
        return "no"    




def input_mailid():
    say("whom do you want to send mail to")
    print("whom do you want to send mail to?")
    user = assistant_listener()
    
    email = user + "@gmail.com"
    email = email.replace(" ","")
    print(email)
    return email

    

def message_input():
    say("whats the message")
    print("whats the message?")
    message = assistant_listener()
    
    print(message)
    return message              


def subject_input():
    say("whats the subject")
    print("whats the subject")
    subject = assistant_listener()
    
    print(subject)
    return subject
                     









email = EmailMessage()


user_input_mail = input_mailid()
subject = subject_input()
message = message_input()


email['From'] = server_login_mail

email['To'] = user_input_mail
email['Subject'] = subject
email.set_content(message)
server.send_message(email)

print("mail send successfully.")
say("mail send successfully")




