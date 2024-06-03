class Messages:

    @staticmethod
    def welcomeMessage():
        return print(" \033[1;34m Bem-vindo ao sistema Blue Carbon Track \033[0m")
    
    @staticmethod
    def applicationDivisor():
        return print("****************************************************************************************************")
    
    @staticmethod
    def spaceDivisor(spaceMin):
        for _ in range(int(spaceMin)):
                print("")  # Adiciona algumas linhas vazias para separar visualmente a saída
        return
    


    @staticmethod
    def optionMessage(message):
        return print(message)
    

    @staticmethod
    def errorMessages(error):
        if(error == "option"): return print("\033[91m Opção inválida\033[0m")
        if(error == "input"): return print("\033[91m O dado informado está incorreto!\033[0m")
        
    @staticmethod
    def successMessage(success):
        print(f"\033[1;34m {success} \033[0m")
            
     