

def login():
 print("Hello,Welcome")
 x=input("Username:")
 z=len(x)
 if z<=11:
    print("Please enter the password")
    p=input()
    print("Welcome:",x)
    list_input()
    
 else:
    print("Check the username")
    login()
    
def list_input():
    grocery=[]
    print("How many items you want to enter")
    first_add=int(input())
    print("Please enter",first_add)
    for i in range(first_add):
        ask=input()
        grocery.append(ask)
        print("The entered value is:",grocery)
        i=i+1
        if i ==first_add:
          print("Want to add more items**1 for Yes** 2 for viewing saved items")
          add=int(input())
          #Program if the user selects to add more items
          if add==1:
            grocery_list2=[] #Second grocery list
            second_add=int(input("How many new items you want to enter"))
            for j in range(second_add):
                ask2=input("Please enter the new items")
                grocery_list2.append(ask2)
                print("The entered item is:",ask2)
                print("The new entered items are:",grocery_list2)
                final_grocery=grocery+grocery_list2
                print("The updated final list saved is:",final_grocery)
                print("Do you wish to edit the list ***1 for yes 2 for viewving the final list")#If the user wants ti edit the second list
                ask1=int(input())
                if ask1==1:
                    print("Please enter the item to be replaced")
                    replace_item1=input()
                    replace_find1=final_grocery.index(replace_item1)#Finding the index of the item to be replaced
                    print("Please enter new item")
                    new_item=input()
                    print("The new item entered is:",new_item)
                    final_grocery[replace_find1]=new_item #inserting the new item
                    print("The final list saved is:",final_grocery)#Printing the final list
                    
                    # If the user opts to just view the list without editing
                elif ask1==2:
                    print("The final list saved is:",final_grocery)
                    
                    #If the user dosent wish to add more items but to edit the first list
                    
          elif add==2:
            print("Final items saved are:",grocery) #The first list without user asking to add new items
            print("Do you want to replace any of the items")
            print("1 for Replace***2 for viewing final list")
            ask2=int(input())
            if ask2==1:
                print("Please enter the item")
                replace_item=input()
                replace_find=grocery.index(replace_item)
                print("The index of the item to be replace is:",replace_find)
                replace_item2=input("Please enter the new item")
                print("The new item entered is:",replace_item2)
                grocery[replace_find]=replace_item2
                print("The final list saved is:",grocery)
            else:
                print("The final list is:",grocery)
                
               
    
    
    
login()
    











    
    

        
        
        
    
    
     
    
    



