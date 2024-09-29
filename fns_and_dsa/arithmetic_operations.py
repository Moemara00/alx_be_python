
def perform_operation(num1,num2,operation): 
    match operation:
        case "add":
             num1 + num2
            
        case "subtract":
            return  num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0 :
                raise ValueError("Sorry we can't divide")
            else:
              return  num1//num2
        case _ :
            return ("Invalid")
        
