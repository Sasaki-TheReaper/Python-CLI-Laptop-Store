# @ author: Anjan Khadka
# @ version: 3.11.2


import laptop
import order
import sell

# function of main that starts the program and used to call other functions
def main():
    print("""
        +====================================================================================================+
        -----------------------------------------------------------------------------------------------------
         *            ++++++++++++  WELCOME TO PRAJWAL RENTAL SHOP   ++++++++++++++++       $$        * 
        -----------------------------------------------------------------------------------------------------
                                    -----  Urlabari-7 , Morang -----
        +====================================================================================================+
    """)

    # starting the program with while
    while True:
        customer_name = input ("Enter your name here ----> ") # name of user
        password = input ("Enter the password  ----> ") # password of user (write anything you want)
        if not customer_name.isalpha(): # validation for name only letters can be used
            print(""" 
              _____________________________________________________
              |                     Invalid Input                 |               
              |___________________________________________________|
              |        Only alphabets can be used in              |
              |                  User name                        |
              |___________________________________________________|
             """)
            continue
        elif len(customer_name or password) < 3: # validation for lenght of username and password
            print("""
                ┌──────────────────────────────────────────────────────────┐
                │                       Invalid Input                      │
                ├──────────────────────────────────────────────────────────┤
                │       More than 2 letters should be used for name        |
                |        and more than 2 numbers password                  │
                └──────────────────────────────────────────────────────────┘
            """)
            continue
        else:
            print(f"""
                ┌──────────────────────────────────────────────────────────┐
                │                   Hello {User_name}                      │
                ├──────────────────────────────────────────────────────────┤
                │               Logged in successfully                     |              
                └──────────────────────────────────────────────────────────┘
            """)

        break
    
       # this section contains the choice between different functions 
    while True:         
        print("""                  
            +--------+--------------------------------+           
            | Choice |          Description           |
            +--------+--------------------------------+
            | 1      | Display all Laptops            |
            | 2      | Order Laptop                   |
            | 3      | Sell Laptop                    |
            | 4      | Exit                           |
            +--------+--------------------------------+
        """)
        
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("""  
              _____________________________________________________
              |              Invalid Choice                       |               
              |___________________________________________________|
              |       Enter proper interger value only            |
              |___________________________________________________|
            """) 
            continue
        if choice == 1:  
            laptop.show_laptops()
        elif choice == 2 :
            order.order_laptops(User_name)
        elif choice == 3 :
            sell.sell_laptops()
        elif choice == 4:
            print("""
              _____________________________________________________
              |               Thank you for your visit            |               
              |___________________________________________________|
              |        Remember us in case of more trade          |
              |              or queries about laptos              |
              |___________________________________________________|
            """)        
        else:
            print("""
              _____________________________________________________
              |                     Invalid Input                 |               
              |___________________________________________________|
              |           Enter the choices given above           |
              |                   (1,2,3,4)                       |
              |___________________________________________________|
                  """)

if __name__ == "__main__":
    main()
    
           

        
           