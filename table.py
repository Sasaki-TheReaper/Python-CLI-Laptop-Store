from tabulate import tabulate
print("\t\t\t WELCOME TO PRAJWAL DON STORESSSSSSS:\n \t\t\tletssss rent something new in my store. \n \t\t\tYou can rent following items from this below table.")
def table_():
    try:
        file=open("data.txt","r")
        data=[line.strip().split(',') for line in file]
        table=tabulate(data,headers='firstrow',tablefmt='grid')
        print(table)
    except:
        print("Error")
table_() 