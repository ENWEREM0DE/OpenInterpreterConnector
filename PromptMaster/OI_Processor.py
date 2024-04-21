from groq import Groq
from interpreter import interpreter


def initializeGroqClient():
    apiKey = ""
    groqClient = Groq(api_key=apiKey)
    return groqClient

def initializeOpenAIClient():
    apikey = ""
def determineResult(resultString):
    print(resultString)
    resultString = resultString.lower()
    if "no" in resultString:
        return True
    return False


class PromptController:
    PromptExpressingDeterminer = "You are an Insurance question detector, all you do is say yes or no if a question concerns insurance"

    def __init__(self, prompt):
        self.prompt = prompt
        self.groqClient = initializeGroqClient()

    def isOI(self):
        queryReturn = self.groqClient.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.PromptExpressingDeterminer
                },
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            model="mixtral-8x7b-32768"
        )
        return determineResult(queryReturn.choices[0].message.content)


class OIProcessor:
    def __init__(self):
        interpreter.llm.api_key = "putKeyhere"
        interpreter.verbose = False
        interpreter.conversation_history = True
        interpreter.auto_run = True

    def performWorkFlow(self, prompt):
        lowerPrompt = prompt.lower()
        if 'email' in lowerPrompt or 'email.' in lowerPrompt or 'email!' in lowerPrompt:
            lowerPrompt = self.emailWorkflow()
        elif 'message' in lowerPrompt or 'message!' in lowerPrompt or 'message.' in lowerPrompt:
            lowerPrompt = self.textMessageWorkflow()
        elif 'setup text' in lowerPrompt:
            lowerPrompt = self.setUpMessagingWorkflow()
        else:
            pass
        fullMessage = lowerPrompt + ". do this with the assumption that I use a macbook I give you consent to control my system's applications."
        print(self.communicateWithOpenInterpreter(fullMessage))
    def emailWorkflow(self):
        emailAddress = input("Please enter your email address: ")
        emailSubject = input("Please enter the subject of the email: ")
        emailMessage = input("Please enter your")
        return (f"send an email to {emailAddress} with subject {emailSubject} and body {emailMessage}")

    def textMessageWorkflow(self):
        personToSendTo = input("who do you want to send the message to: ")
        messageToSend = input("What message do you want to send: ")
        return (f"find the contacts.json file in my current directory, convert it to a dictionary, find the value for the key {personToSendTo} use this as a phone number and send them the message {messageToSend}")

    def setUpMessagingWorkflow(self):
        personName = input("What is the person's name")
        personNumber = input("What is the person's phone number")
        return(f"in the contacts.json file in my current directory, convert it to a dictionary, add the key {personName} and give it value the key {personNumber}, and save this as the new contacts.json file")
    def communicateWithOpenInterpreter(self, fullprompt):
        interpreter.chat(fullprompt)
        condition = str(interpreter.messages[1].get("content"))
        if 'proceed' in condition.lower() or 'now' in condition.lower() or "let's" in condition.lower():
            interpreter.chat('proceed')
        return condition

    #workflow for play, asks for medium, then goes to google, spotify or apple music


if __name__ == "__main__":
    prompt = input("Enter your prompt: \n")
    promptController = PromptController(prompt)
    isOI = promptController.isOI()
    print(isOI)
    if isOI == True:
        oiProcessor = OIProcessor()
        oiProcessor.performWorkFlow(prompt)

