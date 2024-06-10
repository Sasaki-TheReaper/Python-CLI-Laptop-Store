print("WELCOME TO PRAJWAL DON STORESSSSSSS:\n lestssss rent something new in my store. \n You can rent following items from this below table.")
def cloth_to_dictionary():
    file=open("data.txt", "r")
    cloth_dictionary={}
    cloth_id=1
    for line in file:
        line=line.replace("\n","")
        cloth_dictionary.update({cloth_id:line.split(",")})
        cloth_id=cloth_id+1
    file.close()
    print(cloth_dictionary[2][3])
    print(cloth_dictionary)
    
    return cloth_dictionary
cloth_to_dictionary()