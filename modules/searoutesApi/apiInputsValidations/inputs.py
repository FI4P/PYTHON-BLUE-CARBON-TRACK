from modules.applicationMessages import applicationMessages;

messages = applicationMessages.Messages()


class ApiInputs:
    def inputValue(messageInput):
        option = input(messageInput) 
        return option
        
        