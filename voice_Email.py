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




#  say function is used convert text-to-speech.


def say(text):
    engine.say(text)
    engine.runAndWait()


say("hello i am your email assistant , what can i do for you?")


#assistant_listener is first used to store our voice and then convert it into text.


def assistant_listener():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language="en-in").lower()
            return info

    except:
        return "no"


def send_email(rec, subject, message):
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


# contact = {
#     "vaibhav": chauhanvaibhav1105"@gamil.com",
#     "youtube": "xesaja6786@itwbuy.com"
# }


def Main():

    listen_me = assistant_listener()
    if "assistant" in listen_me:
        if "write mail" in listen_me:
            say("To whom you want to send mail?")
            try:
                user = assistant_listener()
                # email = contact[user]
                email = user + "@gmail.com"
            except:
                say(user+" not found in your contacts!")
                return 0

            say("What you want to be subject?")
            subject = assistant_listener()

            say("what should be the message?")
            message = assistant_listener()

            say("Email Send Successfully")

            send_email(email, subject, message)
            

while True:
    Main()



# import smtplib
# from email.message import EmailMessage
# import speech_recognition as sr
# import pyttsx3


# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server_login_mail = "chauhanvaibhav1105@gmail.com"
# server_login_password = "Vaibhav1105"
# server.login(server_login_mail, server_login_password)


# #  say function is used convert text-to-speech.


# def say(text):
#     engine.say(text)
#     engine.runAndWait()

# say("hello i am your email assistant , what can i do for you?")

# #assistant_listener is first used to store our voice and then convert it into text.

# def assistant_listener():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             voice = listener.listen(source)
#             info = listener.recognize_google(voice, language="en-in").lower()
#             return info
#     except:
#         return "no"


# def send_email(rec, subject, message):
#     email = EmailMessage()
#     email['From'] = server_login_mail
#     email['To'] = rec
#     email['Subject'] = subject
#     email.set_content(message)
#     server.send_message(email)


# # contact = {
# #     "vaibhav": chauhanvaibhav1105"@gamil.com",
# #     "youtube": "xesaja6786@itwbuy.com"
# # }


# def whattodo():
#     listen_me = assistant_listener()
#     if "assistant" in listen_me:
#         if "write mail" in listen_me:
#             say("To whom you want to send mail?")
#             try:
#                 user = assistant_listener()
#                 email = user + "@gmail.com"
                
#             except:
#                 say(user+" not found in your contacts!")
#                 return 0
#             say("What you want to be subject?")
#             subject = assistant_listener()
#             say("what should be the message?")
#             message = assistant_listener()
#             send_email(email, subject, message)
#             say("Email Send Successfully")

# while True:
#     whattodo()