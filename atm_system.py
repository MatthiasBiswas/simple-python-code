print("Bank of Robber's ATM")
restart = 'Y'
chances = 3
balance = 36500.00
while chances >= 0:
    pin = int(input('Enter 6 digit pin to confirm: '))
    if pin == 134679:
        print('\nWelcome to Bank of Robbers ATM')
        while restart not in ('n', 'NO', 'N', 'no', 'No'):
            print('\nPress 1 to check your balance')
            print('Press 2 to make a withdrawl')
            print('Press 3 to deposite')
            print('Press 4 to quit and return card')
            option = int(input('Please press to confirm one of the following statements\n'))            
            
            if option == 1:
                print(f'Your balance is tk {balance}')
                restart = input('Would you like to continue?')
                if restart in ('n', 'NO', 'N', 'no', 'No'):
                    print("Thank You for using Robber's ATM")
                    break
            
            elif option == 2:
                option2 = 'y'
                print('\n500, 1000, 2000, 5000, 10000, 20000')
                withdrawl = float(input('How much would you like to withdraw?'))
                if withdrawl in [500, 1000, 2000, 5000, 10000, 20000]:
                    balance -= withdrawl
                    print(f'Your balance is now tk {balance}')
                    restart = input('Would you like to continue?')
                    if restart in ('n', 'NO', 'N', 'no', 'No'):
                        print("Thank You for using Robber's ATM")
                        break
                elif withdrawl not in [500, 1000, 2000, 5000, 10000, 20000]:
                    print('Invalid Amount! \nPlease try again.')
                    restart = 'y'
                elif withdrawl == 1 :
                    withdrawl = float(input("Please Enter Desired amount."))
            
            elif option == 3:
                deposite = float(input("How much would you like to deposite?"))
                balance += deposite
                print(f'Your balance is now tk {balance}')
                restart = input('Would you like to continue?')
                if restart in ('n', 'NO', 'N', 'no', 'No'):
                    print("Thank You for using Robber's ATM")
                    break
            
            elif option == 4:
                print('Please wait while your card is being returned.')
                print("Thank You for using Robber's ATM")
                break
            
            else:
                print('Please enter a valid number.')
                restart = 'y'
        
    elif pin != 134679:
        print('Incorrect Password')
        chances -= 1
        if chances == 0:
            print('Please try later.')
            break



            
