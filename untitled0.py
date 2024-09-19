print("""
                                        ______          ______   ______            ______     _______  ______ 
                              |      | |       |       |        |      | |\    /| |              |    |      |
                              |      | |       |       |        |      | | \  / | |              |    |      |
                              |      | |______ |       |        |      | |  \/  | |______        |    |      |
                              |  /\  | |       |       |        |      | |      | |              |    |      |
                              | /  \ | |       |       |        |      | |      | |              |    |      |
                              |/    \| |______ |______ |______  |______| |      | |______        |    |______|

                   ______   ______                                  ______                                    
                  |      | |      | \     /    /\      |           |             /\      |            /\      \    / \     /
                  |      | |      |  \   /    /  \     |           |            /  \     |           /  \      \  /   \   / 
                  |______| |      |   \ /    /____\    |           |   ____    /____\    |          /____\      \/     \ /  
                  |   \    |      |    |    /      \   |           |      |   /      \   |         /      \     /\      |   
                  |    \   |      |    |   /        \  |           |      |  /        \  |        /        \   /  \     |   
                  |     \  |______|    |  /          \ |______     |______| /          \ |______ /          \ /    \    |   

""")      
import pandas as pd
import matplotlib.pyplot as plt
import random
import sys

GT=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Guest.csv")
GBT=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Guest booking.csv")
pd.set_option('display.expand_frame_repr',False)
pd.set_option('display.max_columns',None)
ST=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv")
pd.set_option('display.max_columns',None)
MT=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Menu.csv")

#ADMIN LOGIN
def admin_login():
    UID = input("ENTER THE USER ID = ")
    if UID == 'RGH_AD00001':
        while True:
            PWD = input("ENTER THE PASSWORD = ")
            if PWD == 'royalgalaxy':
                break
            else:
                print("!!! INVALID PASSWORD !!!") 
        print()    
    else:
        print("!!! INVALID USER ID !!!") 
        admin_login()

#1. VIEWING STAFF TABLE
def staff_info():
        print()
        print("""
                        ____   ____         ____  ____     ____   ____  ____  ____   ____   ___    ____
                       |        |    /\    |     |        |    | |     |     |    | |    | |   \  |    
                       |____    |   /__\   |____ |____    |____| |____ |     |    | |____| |    | |____
                            |   |  /    \  |     |        |  \   |     |     |    | |  \   |    |      |
                        ____|   | /      \ |     |        |   \  |____ |____ |____| |   \  |___/   ____|


                    """)     
        print()
        print(ST)        

#2. ADDING A NEW STAFF
def update_staff():
    print()
    print("""
          
                                                                        STAFF TABLE UPDATION
                                 ____________________________                                           ______________________________________
                                |                            |                                         |                                     |
                                |     a. ADD A NEW STAFF     |                                         |     b. DELETE AN EXISTING STAFF     |
                                |____________________________|                                         |_____________________________________|
          """)
    u = input("ENTER YOUR CHOICE = ")
    if u == "A" or u == "a":
        ST=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv")
        a = int(input("ENTER THE STAFF ID = "))
        b = input("ENTER THE NAME OF THE EMPLOYEE = ")
        c = int(input("ENTER DEPARTMENT NUMBER = "))
        d = int(input("ENTER THE SALARY OF THE EMPLOYEE = "))
        e = input("ENTER THE JOB OF THE EMPLOYEE = ")
        f = input("ENTER THE HIRE DATE OF THE EMPLOYEE (YYYY/MM/DD) = ")
        g = input("ENTER THE VACCINATION DETAILS (Yes/No) = ")
        ST.loc[a]=[a,b,c,d,e,f,g]
        ST.to_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv", index = False)
        print("*"*95, '\n')
        print(" "*35, "YOU HAVE SUCCESSFULLY ADDED A STAFF \n")
        print("*"*95)
    elif u == "B" or u == "b":
        ST=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv")
        xyz = int(input("ENTER THE STAFF ID = "))
        ST=ST.drop(ST.index[ST["Staff_ID"]==xyz])
        print()
        ST.to_csv("E:\\IP\\Project\\Staff.csv",index=False) 
        print("*"*95, '\n')
        print(" "*35, "YOU HAVE SUCCESSFULLY DELETED A STAFF \n")
        print("*"*95)
    else:
        print("!!!INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE WITH UPDATION? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        update_staff()

#REVISE STAFF TABLE
def revise_staff():
    print()
    print(""" 
          
                                                                                     REVISING STAFF TABLE
                                 _________________________________________                                           ______________________________________
                                |                                         |                                         |                                     |
                                |     a. UPDATE COVID VACCINE DETAILS     |                                         |        b.UPDATE EMPLOYEE JOB        |
                                |_________________________________________|                                         |_____________________________________|
          """)
    r = input("ENTER YOUR CHOICE = ")
    if r == "A" or r == "a":
        sid = int(input("ENTER THE STAFF ID = "))
        for i in ST.Staff_ID:
            if i == sid:
                found = True
                covid = input("ENTER THE UPDATED VACCINATED DETAILS = ")
                ST.loc[ST.Staff_ID == sid, "Covid_Vaccine"] = covid
                ST.to_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv", index = False)
                print()
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED STAFF DETAILS")
                print("*"*95)
                break
        else:
            print("!!! INVALID ENTRY. STAFF ID DOES NOT EXIST !!!")
    elif r == "B" or r == "b":
        sid = int(input("ENTER THE STAFF ID = "))
        for i in ST.Staff_ID:
            if i == sid:
                found = True
                job = input("ENTER THE NEW JOB TITLE = ")
                ST.loc[ST.Staff_ID == sid, "Job_Title"] = job
                ST.to_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Staff.csv", index = False)
                print()
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED STAFF DETAILS")
                print("*"*95)
                break
            else:
                print("!!! INVALID ENTRY. STAFF ID DOES NOT EXIST !!!")
        else:
            print("!!! INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE UPDATING? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        revise_staff()

#SEARCHING A STAFF
def search_staff():
    print("""
                                                                      SEARCHING FOR AN EMPLOYEE
                               _______________________________                                           ________________________________
                              |                               |                                         |                                |
                              |     a. SEARCH BY STAFF ID     |                                         |     b.SEARCH BY STAFF NAME     |
                              |_______________________________|                                         |________________________________|                      
          
          """)
    s = input("ENTER YOUR CHOICE = ")
    if s == "a" or s == "A":
        stid = int(input("ENTER THE ID OF THE STAFF = "))
        found = False
        for i in ST["Staff_ID"]:
            if stid == i:
                found = True
                print(" EMPLOYEE FOUND ")
                print("""
                      
                      THE STAFF'S  DETAILS ARE
                      
                      """)    
                print()
                print("STAFF ID: ",ST[ST["Staff_ID"]==stid]["Staff_ID"].values)
                print("NAME: ",ST[ST["Staff_ID"]==stid]["Name"].values)
                print("DEPARTMENT: ",ST[ST["Staff_ID"]==stid]["Department"].values)
                print("SALARY: ",ST[ST["Name"]==stid]["Salary"].values)
                print("JOB TITLE: ",ST[ST["Staff_ID"]==stid]["Job_Title"].values)
                print("HIRE DATE: ",ST[ST["Staff_ID"]==stid]["Hire_Date"].values)
                print("COVID VACCINE: ",ST[ST["Staff_ID"]==stid]["Covid_Vaccine"].values) 
                print()
                break
        if found==False:
            print("!!! EMPLOYEE NOT FOUND !!!")     
    elif s == "b" or s == "B":        
        stname = input("ENTER THE NAME OF THE STAFF = ")
        found = False
        for i in ST["Name"]:
            if stname == i:
                found = True
                print(" EMPLOYEE FOUND ")
                print("""
                      
                      THE STAFF'S  DETAILS ARE
                      
                      """)    
                print()
                print("STAFF ID: ",ST[ST["Name"]==stname]["Staff_ID"].values)
                print("NAME: ",ST[ST["Name"]==stname]["Name"].values)
                print("DEPARTMENT: ",ST[ST["Name"]==stname]["Department"].values)
                print("SALARY: ",ST[ST["Name"]==stname]["Salary"].values)
                print("JOB TITLE: ",ST[ST["Name"]==stname]["Job_Title"].values)
                print("HIRE DATE: ",ST[ST["Name"]==stname]["Hire_Date"].values)
                print("COVID VACCINE: ",ST[ST["Name"]==stname]["Covid_Vaccine"].values)
                print()
                break
        if found==False:
            print("!!! EMPLOYEE NOT FOUND !!!")
    else:
        print("!!! INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE SEARCHING? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        search_staff()

#MENU
def menu():
        print()
        print("""
                            ____
                    |\  /| |     |\   | |     |
                    | \/ | |____ | \  | |     |
                    |    | |     |  \ | |     |
                    |    | |____ |   \| |_____|
              """)
        print()
        print(MT)        

#ADDING A NEW ITEM
def additem():
        itemno = int(input("ENTER THE ITEM NUMBER = "))
        for i in range(1,25):
            if i == itemno:
                found = True
                print("!!! RECORD ALREADY EXISTS !!!")
                break
            item = input("ENTER THE ITEM NAME= ")
            if len(item) < 35:
                print()
            else:
                print("!!! ITEM NAME MUST BE WITHIN 35 CHARACTERS !!!")        
            item_type = input("ENTER THE TYPE = ")
            price = int(input("ENTER THE PRICE = "))
            MT.loc[itemno]=[itemno,item,item_type,price]
            MT.to_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Menu.csv",index=False)
            print("*"*95, '\n')
            print(" "*35, "YOU HAVE SUCCESSFULLY ADDED AN ITEM")
            print("*"*95)
            break

#REVISING MENU TABLE
def update_item():
    print()
    print("""
                                                                     REVISING MENU TABLE
                           _____________________________                                           ______________________________
                          |                             |                                         |                              |
                          |     a. UPDATE ITEM NAME     |                                         |     b. UPDATE ITEM PRICE     |
                          |_____________________________|                                         |______________________________|  
          
          """)
    m = input("ENTER YOUR CHOICE = ")
    if m == "A" or "a":
        ino = int(input("ENTER THE ITEM NUMBER = "))
        for i in MT.Item_No:
            if i == ino:
                found = True
                item = input("ENTER THE UPDATED ITEM NAME = ")
                MT.loc[MT.Item_No == ino, "Item"] = item
                print()
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED ITEM DETAILS")
                print("*"*95)
                break
            
        else:
            print("!!! INVALID ENTRY. ITEM NUMBER DOES NOT EXIST !!!")
    elif m == "B" or m == "b":
        ino = int(input("ENTER THE ITEM NUMBER = "))
        for i in MT.Item_No:
            if i == ino:
                found = True
                iprice = input("ENTER THE UPDATED ITEM PRICE = ")
                MT.loc[MT.Item_No == ino, "Price"] = iprice
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED ITEM DETAILS")
                print("*"*95)
                break
            if found == True:
                break
            else:
                print("!!! INVALID ENTRY. ITEM NUMBER DOES NOT EXIST !!!")
    else:
        print("!!! INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE UPDATING? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        update_item()

#SEARCHING FOR AN ITEM
def search_item():
    print()
    print("""
                                                                     SEARCHING FOR AN ITEM
                      __________________________________                                           _______________________________
                     |                                  |                                         |                               |
                     |     a. SEARCH BY ITEM NUMBER     |                                         |     b.SEARCH BY ITEM TYPE     |
                     |__________________________________|                                         |_______________________________| 
          """)
    i = input("ENTER YOUR CHOICE = ")
    if i == "A" or i == "a":
        mtitem = int(input("ENTER THE ITEM NUMBER = "))
        found = False
        for o in MT["Item_No"]:
            if o == mtitem:
                found = True
                print(" ITEM FOUND ")
                print("""
                      
                      THE ITEM  DETAILS ARE
                      
                      """)    
                print()
                print("ITEM NO: ",MT[MT["Item_No"]==mtitem]["Item_No"].values)
                print("ITEM: ",MT[MT["Item_No"]==mtitem]["Item"].values)
                print("TYPE: ",MT[MT["Item_No"]==mtitem]["Type"].values)
                print("PRICE: ",MT[MT["Item_No"]==mtitem]["Price"].values)
                print()
        if found == False:
            print("!!! ITEM NOT FOUND !!!")            
    elif i == "B" or i == "b":
        mtname = input("ENTER THE ITEM NAME = ")
        found = False
        for t in MT["Type"]:
            if mtname == t:
                found = True
                print(" ITEM NAME FOUND ")
                print("""
                      
                      THE ITEM DETAILS ARE
                      
                      """)    
                print()
                print("ITEM NO: ",MT[MT["Item_No"]==mtname]["Item_No"].values)
                print("ITEM: ",MT[MT["Item_No"]==mtname]["Item"].values)
                print("TYPE: ",MT[MT["Item_No"]==mtname]["Type"].values)
                print("PRICE: ",MT[MT["Item_No"]==mtname]["Price"].values)
                print()
                break
        if found==False:
            print("!!! ITEM TYPE NOT FOUND !!!")
    else:
        print("!!! INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE SEARCHING? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        search_item()

#VIEWING GUEST RECORDS
def guestrecord():
        print(GT)

#SALES
def avgsales():
        while True:
            print("""
                  
                                                                                     AVERAGE SALES
                   ________________________________________            ____________________________________________            ___________________________________________
                  |                                        |          |                                            |          |                                           |
                  |     a. AVERAGE SALE ON YEARLY BASIS    |          |     b. AVERAGE SALES ON A MONTHLY BASIS    |          |     c. AVERAGE SALES ON A WEEKLY BASIS    |
                  |________________________________________|          |____________________________________________|          |___________________________________________|
                  
                  """)
            x = input("ENTER YOUR CHOICE = ")
            if x == 'A' or x == 'a':
                print()
                print("AVERAGE SALES ON A YEARLY BASIS")
                print()
                avgy={"YEAR":[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],
                      "AVERAGE SALES":[100000,150000,189000,300000,126000,135000,157000,205000,265000,199800]}
                dfy = pd.DataFrame(avgy)
                dfy.plot(kind="bar",x="YEAR",y="AVERAGE SALES",
                         color=['r','y','g','b','m','c','purple','pink','orange','maroon'])
                plt.ylabel="SALES"
                plt.title("YEARLY AVERAGE SALES")
                plt.show()
            elif x == 'B' or x == 'b':
                print()
                print("AVERAGE SALES ON A MONTHLY BASIS")
                print()
                avgm={"MONTH":['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'],
                      "AVERAGE SALES":[67800,52000,48000,78000,92000,55000,65000,79000,81000,43000,35000,99500]}
                dfy = pd.DataFrame(avgm)
                dfy.plot(kind="bar",x="MONTH",y="AVERAGE SALES",
                         color=['r','y','g','b','m','c','purple','pink','orange','maroon','grey','brown'])
                plt.ylabel="SALES"
                plt.title("MONTHLY AVERAGE SALES")
                plt.show() 
            elif x == 'C' or x == 'c':
                print()
                print("AVERAGE SALES ON A WEEKLY BASIS")
                print()
                avgw={"SUN":[12100,11000,16700,8600],
                      "MON":[10000,15000,18600,9800],
                      "TUE":[16000,17900,10500,9800],
                      "WED":[12000,13000,17600,12800],
                      "THU":[13700,13300,15000,19900],
                      "FRI":[20000,25000,18000,19800],
                      "SAT":[23000,20000,17700,19550]}
                dfy = pd.DataFrame(avgw)
                dfy.plot(kind="bar")
                plt.xticks(range(4),labels=["WEEK1","WEEK2","WEEK3","WEEK4"])
                legend_properties={"weight":"bold","size":7.5}
                plt.legend(loc="upper right",prop=legend_properties)
                plt.title("WEEKLY AVERAGE SALES")
                plt.show()    
            else:
                print("!!! INVALID ENTRY. PLEASE ENTER A, B, C !!!")
            con = input("DO YOU WANT TO CONTINUE WITH SALES? (YES/NO) = ")
            if con == "NO" or con == "no":
                break

#Guest login
def guest_login():
    foundid = False
    foundpw = False
    while True:
        GID = input("ENTER YOUR USER ID = ").upper()
        for i in GT.Guest_ID:
            if i == GID:
                foundid = True
                break
        if foundid == True:
            break
        else:
            print("!!! INVALID ENTRY. YOUR ACCOUNT ID IS INCORRECT !!!")
    while True:        
        GPW = input("ENTER YOUR PASSWORD = ")
        b = GT[GT["Guest_ID"]==GID]["Guest_Password"].values
        for i in GT["Guest_Password"]:
            if i == GPW and GPW == b:
                foundpw = True
                break
        if foundpw == True:
            break
        else:
            print(" !!! INVALID ENTRY. THE PASSWORD YOU HAVE ENTERED IS INCORRECT !!! ")

            guest_login()
    print("*"*135,'\n')
    print(" "*50, " YOU HAVE SUCCESSFULLY LOGGED IN \n")
    print("*"*135)

# GUEST ACCOUNT CREATION
def create_account():
    ID = input("\nENTER YOUR ID = ")
    pw = input("\nENTER YOUR PASSWORD = ")    
    nm = input("\nENTER YOUR NAME = ")
    GT.loc[ID]=[ID,pw,nm]
    GT.to_csv("E:\\IP\\Project\\Guest.csv", index = False)

# ROOM DETAILS
def roomtype():
    while True:
        print("""            
                                                                                                        TYPES OF ROOMS
                                                                                    
                                                                                    _____________________________________________________
                                                                                   |                                                     |
                                                                                   |          a. 1 KING BED                              |
                                                                                   |                                                     |
                                                                                   |          b. 2 TWIN BEDS                             |
                                                                                   |                                                     |
                                                                                   |          c. 1 KING BED HIGH FLOOR                   |
                                                                                   |                                                     |
                                                                                   |          d. 2 TWIN BEDS HIGH FLOOR                  |
                                                                                   |                                                     |
                                                                                   |          e. 1 KING BED WITH CLUB ACCESS             | 
                                                                                   |                                                     |
                                                                                   |          f. 2 TWIN BEDS WITH CLUB ACCESS            |
                                                                                   |                                                     |
                                                                                   |          g. ROYAL SUITE WITH 1 KING BED             |
                                                                                   |                                                     |
                                                                                   |          h. ROYAL SUITE WITH 2 TWIN BEDS            | 
                                                                                   |_____________________________________________________|
          
          """)
        ch = input("ENTER YOUR CHOICE = ")
        if ch == "A" or ch == "a":
            print("\n\n\t\t\t\t\t1. 1 KING BED\n")
            print("--> ROOM DETAILS - 35-sqm, Work area, 43-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Mini bar\n")
            print("--> PAYMENT - 7000\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "B" or ch == "b":
            print("\n\n\t\t\t\t\t2. 2 TWIN BEDS\n")
            print("--> ROOM DETAILS - 35-sqm, Work area, View of the city, 43-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Mini bar\n")
            print("--> PAYMENT - 7500\n\n")
        elif ch == "C" or ch == "c":
            print("\n\n\t\t\t\t\t3. 1 KING BED HIGH FLOOR\n")
            print("--> ROOM DETAILS - 35-sqm on higher floors of hotel, Work area, 50-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Mini bar\n")
            print("--> PAYMENT - 8000\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "D" or ch == "d":
            print("\n\n\t\t\t\t\t4. 2 TWIN BEDS HIGH FLOOR\n")
            print("--> ROOM DETAILS - 35-sqm on higher floors of hotel, Work area, View of the city, 50-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Mini bar\n")
            print("--> PAYMENT - 8500\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "E" or ch == "e":
            print("\n\n\t\t\t\t\t5. 1 KING BED WITH CLUB ACCESS\n")
            print("--> ROOM DETAILS - Deluxe 35-sqm, Work area, Glass atrium, 55-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Royal club lounge\n")
            print("--> PAYMENT - 9000\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "F" or ch == "f":
            print("\n\n\t\t\t\t\t6. 2 TWIN BED WITH CLUB ACCESS\n")
            print("--> ROOM DETAILS - Deluxe 35-sqm on higher floors of hotel, Work area, View of the city, 55-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Walk-in rain shower, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board\n")
            print("--> CLUBS - Royal club lounge\n")
            print("--> PAYMENT - 9500\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "G" or ch == "g":
            print("\n\n\t\t\t\t\t7. ROYAL SUITE WITH 1 KING BED\n")
            print("--> ROOM DETAILS - 75-sqm, Living/Dining area, Standard suite, Two 65-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Bathroom with walk-in shower, Bathtub, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board, Fridge\n")
            print("--> CLUBS - Private Royal club lounge\n")
            print("--> PAYMENT - 10000\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break
        elif ch == "H" or ch == "h":
            print("\n\n\t\t\t\t\t8. ROYAL SUITE WITH 2 TWIN BEDS\n")
            print("--> ROOM DETAILS - 110-sqm, Living and dining area, Premium suite, Two 75-inch LCD, Nespresso coffeemaker\n")
            print("--> BATHROOM ACCESSORIES - Luxurious bathroom with walk-in shower, Bathtub, Bathrobe, Slippers, Hairdryer\n")
            print("--> IN-ROOM ACCESSORIES - IP phones, In-room safe, Iron, Ironing board, Fridge\n")
            print("--> CLUBS - Private Royal club lounge\n")
            print("--> PAYMENT - 15000\n\n")
            con = input("DO YOU WANT TO CONTINUE? (YES/NO) = ")
            if con == "NO" or con == "no":
                break

# ROOM BOOKING
def room_booking():
   GB=pd.read_csv("E:\\IP\\Project\\Guest booking.csv")
   Gid = input("\nENTER YOUR ACCOUNT ID = ")
   gpw = input("\nENTER YOUR PASSWORD = ")
   name = input("\nENTER YOUR NAME = ")
   cid = input("\nENTER THE CHECK-IN DATE (DD/MM/YYYY) = ")
   cod = input("\nENTER THE CHECK-OUT DATE (DD/MM/YYYY) = ")
   sb = input("\nENTER THE SOURCE OF BOOKING = ")
   nd = int(input("\nENTER THE NUMBER OF DAYS = "))
   print("""            
                                                                                                   TYPES OF ROOMS
                                                                               
                                                                               _____________________________________________________
                                                                              |                                                     |
                                                                              |          a. 1 KING BED                              |
                                                                              |                                                     |
                                                                              |          b. 2 TWIN BEDS                             |
                                                                              |                                                     |
                                                                              |          c. 1 KING BED HIGH FLOOR                   |
                                                                              |                                                     |
                                                                              |          d. 2 TWIN BEDS HIGH FLOOR                  |
                                                                              |                                                     |
                                                                              |          e. 1 KING BED WITH CLUB ACCESS             | 
                                                                              |                                                     |
                                                                              |          f. 2 TWIN BEDS WITH CLUB ACCESS            |
                                                                              |                                                     |
                                                                              |          g. ROYAL SUITE WITH 1 KING BED             |
                                                                              |                                                     |
                                                                              |          h. ROYAL SUITE WITH 2 TWIN BEDS            | 
                                                                              |_____________________________________________________|
     
     """)
   py = input("\nENTER THE ROOM OF YOUR CHOICE (A/B/C/D/E/F/G/H) = ")
   if py == "a" or py == "A":
       s = 7000*nd
   elif py == "B" or py == "b":
       s = 7500*nd
   elif py == "c" or py == "C":
       s = 8000*nd
   elif py == "d" or py == "D":
       s = 8500*nd   
   elif py == "e" or py == "E":
       s = 9000*nd 
   elif py == "f" or py == "F":
       s = 9500*nd
   elif py == "g" or py == "G":
       s = 10000*nd
   elif py == "h" or py == "H":
       s = 15000*nd
   rm = input("ENTER THE NAME OF ROOM YOU HAVE SELECTED = ")
   x = random.randint(11,95)
   print("\nYOUR ROOM NUMBER IS",x)
   print("THE NET PAYEMENT IS",s)
   GB.loc[Gid] = [Gid,gpw,name,rm,nd,cid,cod,x,sb,s]
   GB.to_csv("E:\\IP\\Project\\Guest booking.csv", index = False)
   print("*"*95, '\n')
   print(" "*35, "YOU HAVE SUCCESSFULLY BOOKED A ROOM \n")
   print("*"*95)

#VIEW ACCOUNT
def view_acc():
    GBT=pd.read_csv("E:\\IP\\Project\\Guest booking.csv")
    gid = input("ENTER YOUR ACCOUNT ID = ").upper()
    for i in GT["Guest_ID"]:
        if gid == i:
            found = True
            print("*"*95,'\n')
            print(" "*30, "YOUR ACCOUNT DETAILS ARE AS FOLLOWS \n")
            print("*"*95)
            print("ID: ",GT[GT["Guest_ID"]==gid]["Guest_ID"].values)
            print("\nPASSWORD: ",GT[GT["Guest_ID"]==gid]["Guest_Password"].values)
            print("\nNAME: ",GT[GT["Guest_ID"]==gid]["Name_Of_Guest"].values)
            print("\nROOM TYPE: ",GBT[GBT["Guest_ID"]==gid]["Type_Of_Room"].values)
            print("\nNUMBER OF DAYS: ",GBT[GBT["Guest_ID"]==gid]["No_Of_Days"].values)
            print("\nCHECK-IN DATE: ",GBT[GBT["Guest_ID"]==gid]["Check_In_Date"].values)
            print("\nCHECK-OUT DATE: ",GBT[GBT["Guest_ID"]==gid]["Check_Out_Date"].values)
            print("\nROOM NUMBER: ",GBT[GBT["Guest_ID"]==gid]["Room_No"].values)
            print("\nSOURCE OF BOOKING: ",GBT[GBT["Guest_ID"]==gid]["Source_Of_Booking"].values)
            print("\nPAYMENT: ",GBT[GBT["Guest_ID"]==gid]["Net_Payment"].values)
            break
    if found == False:
        print("!!! INVALID ENTRY. PLEASE RETRY AGAIN !!!")
        view_acc()

#UPDATE ACCOUNT
def update_details():
    print()
    print("""
                                                                    REVISING GUEST DETAILS
                           _____________________________                                           ______________________________
                          |                             |                                         |                              |
                          |   a. UPDATE YOUR PASSWORD   |                                         |    b. UPDATE CHECK-IN DATE   |
                          |_____________________________|                                         |______________________________|  
          
          """)
    n = input("ENTER YOUR CHOICE = ")
    if n == "A" or n == "a":
        g_id = input("ENTER YOUR ACCOUNT ID = ")
        for i in GT.Guest_ID:
            if i == g_id:
                found = True
                pass_wd = input("ENTER THE UPDATED PASSWORD = ")
                GT.loc[GT.Guest_ID == g_id, "Guest_Password"] = pass_wd
                print()
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED YOUR DETAILS \n")
                print("*"*95)
                break  
        else:
            print("!!! INVALID ENTRY. ACCOUNT ID DOES NOT EXIST !!!")
            
    elif n == "B" or n == "b":
        GB=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Guest booking.csv")
        g_id = input("ENTER YOUR ACCOUNT ID = ")
        for i in GB.Guest_ID:
            if i == g_id:
                found = True
                cidate = input("ENTER THE NEW CHECK-IN DATE (DD/MM/YYYY) = ")
                GB.loc[GB.Guest_ID == g_id, "Check_In_Date"] = cidate
                print()
                print("*"*95, '\n')
                print(" "*35, "YOU HAVE SUCCESSFULLY UPDATED YOUR DETAILS \n")
                print("*"*95)
                break  
        else:
            print("!!! INVALID ENTRY. ACCOUNT ID DOES NOT EXIST !!!")
            
    else:
        print("!!! INVALID ENTRY. PLEASE ENTER A OR B !!!")
    con = input("DO YOU WANT TO CONTINUE UPDATING? (YES/NO) = ")
    if con == "NO" or con == "no":
        exit_AD()
    elif con == "YES" or con == "yes":
        update_details()

# FEED BACK
def feedback():
    print()
    print("""
                                                                           FEEDBACK
                           _____________________________                                           ______________________________
                          |                             |                                         |                              |
                          |     a. POSITIVE FEEDBACK    |                                         |     b. NEGATIVE FEEDBACK     |
                          |_____________________________|                                         |______________________________|  
          
          """)
    fb = input("\n ENTER YOUR CHOICE = ")
    if fb == "A" or fb == "a":
        pfb = input("\n PLEASE ENTER YOUR COMMENTS = ")
        print()
        print("THANK YOU FOR THE FEEDBACK. PLEASE DO VISIT US AGAIN :D ")
        
    elif fb == "B" or fb == "b":
        nfb = input("\n PLEASE ENTER YOUR COMMENTS = ")
        print()
        print("""THANK YOU FOR THE FEEDBACK.
              WE ARE SORRY THAT WE COULD NOT MEET YOUR EXPECTION.
              WE WILL IMPROVE OUR SERVICE IN THE FUTURE
                    PLEASE DO VISIT US AGAIN """)
                    
#DELETING ACCOUNT
def delGT():
    GT=pd.read_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Guest.csv")
    dg = input("ENTER YOUR ACCOUNT ID = ")
    GT=GT.drop(GT.index[GT["Guest_ID"]==dg])
    print()
    GT.to_csv("C:\\Users\\chris\\Desktop\\Christina\\IP\\Project\\Guest.csv",index=False) 
    print("*"*95, '\n')
    print(" "*35, "YOU HAVE SUCCESSFULLY DELETED YOUR ACCOUNT \n")
    print("*"*95)  
    
#RATING
def rating():
    print("""
                                          ____________________       ____________________       ____________________
                                         |                    |     |                    |     |                    |
                                         |    a. * * * * *    |     |     b. * * * *     |     |      c. * * *      |
                                         |____________________|     |____________________|     |____________________|
              
                                                        ____________________        ____________________
                                                       |                    |      |                    |
                                                       |       d. * *       |      |        e. *        |
                                                       |____________________|      |____________________|
                            
              """)
    rt = input("\nENTER YOUR CHOICE = ")
    if rt == "A" or rt == "a":
        print("""
              
                                                       THANK YOU FOR RATING US 5 STARS
                                                          PLEASE DO VISIT US AGAIN
                  
                  """)
    if rt == "B" or rt == "b":
        print("""
              
                                                       THANK YOU FOR RATING US 4 STARS
                                                          PLEASE DO VISIT US AGAIN
                  
                  """)
    if rt == "C" or rt == "C":
        print("""
                  
                                                       THANK YOU FOR RATING US 3 STARS
                                                          PLEASE DO VISIT US AGAIN
                  
                  """)
    if rt == "D" or rt == "d":
        print("""
                  
                                                       THANK YOU FOR RATING US 2 STARS
                                                WE PROMISE TO IMPROVE OUR SERVICE IN THE FUTURE
                                                          PLEASE DO VISIT US AGAIN
                  
                  """)
    if rt == "E" or rt == "e":
        print("""
                  
                                                       THANK YOU FOR RATING US 1 STAR
                                                WE PROMISE TO IMPROVE OUR SERVICE IN THE FUTURE
                                                          PLEASE DO VISIT US AGAIN
                  
                  """)
                  
#Exiting Admin
def exit_AD():
     ES=input("DO YOU WANT TO CONTINUE? (Y/N) = ")
     if ES=="n" or ES=="N":
            print("""
                                                             ___________                                                     ______                    
                                                                 |       |       |      /\      |\     | |  /      \     /  /      \   |        |     
                                                                 |       |       |     /  \     | \    | | /        \   /  |        |  |        |     
                                                                 |       |_______|    /____\    |  \   | |/          \ /   |        |  |        |     
                                                                 |       |       |   /      \   |   \  | |\           |    |        |  |        |     
                                                                 |       |       |  /        \  |    \ | | \          |    |        |  |        |     
                                                                 |       |       | /          \ |     \| |  \         |     \______/    \______/      
                                                      
                        
                  """)

#EXITING GUEST
def exit_GT():
    ES=input("\nDO YOU WANT TO CONTINUE IN GUEST SECTION? (Y/N) = ")
    if ES=="n" or ES=="N":
            print("""
                                                             ___________                                                     ______                    
                                                                 |       |       |      /\      |\     | |  /      \     /  /      \   |        |     
                                                                 |       |       |     /  \     | \    | | /        \   /  |        |  |        |     
                                                                 |       |_______|    /____\    |  \   | |/          \ /   |        |  |        |     
                                                                 |       |       |   /      \   |   \  | |\           |    |        |  |        |     
                                                                 |       |       |  /        \  |    \ | | \          |    |        |  |        |     
                                                                 |       |       | /          \ |     \| |  \         |     \______/    \______/                         
                  """)
                  
#EXITING ABOUT US
def exit_AU():
    ES=input("\nDO YOU WANT TO EXIT THE SOFTWARE? (Y/N) = ")
    if ES=="Y" or ES=="y":
            print("""
                                                             ___________                                                     ______                    
                                                                 |       |       |      /\      |\     | |  /      \     /  /      \   |        |     
                                                                 |       |       |     /  \     | \    | | /        \   /  |        |  |        |     
                                                                 |       |_______|    /____\    |  \   | |/          \ /   |        |  |        |     
                                                                 |       |       |   /      \   |   \  | |\           |    |        |  |        |     
                                                                 |       |       |  /        \  |    \ | | \          |    |        |  |        |     
                                                                 |       |       | /          \ |     \| |  \         |     \______/    \______/      
                                                      
                                                   ______   ______    ______                      ______    __________             ______                  ______
                                                  |        /      \  |      |     \          / | |        |     |      | |\     | |            |        | |
                                                  |       |        | |      |      \        /  | |        |     |      | | \    | |            |        | |
                                                  |______ |        | |______|       \      /   | |_____   |     |      | |  \   | |   ____     |        | |_____ 
                                                  |       |        | |   \           \    /    |       |  |     |      | |   \  | |      |     |        |       |
                                                  |       |        | |    \           \  /     |       |  |     |      | |    \ | |      |     |        |       |
                                                  |        \______/  |     \           \/      | ______|  |     |      | |     \| |______|      \______/  ______|
                  """)
            sys.exit()
                  
while True:
    print("""                                         
                                                                                ____________________________
                                                                               |                            |
                                                                               |           SELECT           |
                                                                               |____________________________|
          """) 
    print("""
                                                       _________________            ____________________            ____________________
                                                      |                 |          |                    |          |                    |
                                                      |     a.ADMIN     |          |      b.GUEST       |          |     c.ABOUT US     |
                                                      |_________________|          |____________________|          |____________________|
          
         """)
    ch = input("ENTER YOUR CHOICE = ")
    #ADMIN
    if ch == 'a' or ch == "A":  
        admin_login()
        while True:
        
            print()
            print("""
                                                                                WELCOME TO THE ADMINISTRATION SECTION
                                                                                ____________________________________
                                                                               |                                    |
                                                                               |     a. VIEW STAFF TABLE            |
                                                                               |                                    |
                                                                               |     b. UPDATE STAFF TABLE          |
                                                                               |                                    |
                                                                               |     c. REVISE EMPLOYEE DETAILS     |
                                                                               |                                    |
                                                                               |     d. SEARCH FOR AN EMPLOYEE      |
                                                                               |                                    |
                                                                               |     e. VIEW MENU                   |
                                                                               |                                    |
                                                                               |     f. UPDATE MENU TABLE           |
                                                                               |                                    |
                                                                               |     g. REVISE MENU TABLE           |
                                                                               |                                    |
                                                                               |     h. SEARCH FOR AN ITEM          |
                                                                               |                                    |
                                                                               |     i. VIEW CUSTOMER RECORDS       |
                                                                               |                                    | 
                                                                               |     j. VIEW SALES                  |
                                                                               |                                    |
                                                                               |     k. EXIT                        |
                                                                               |____________________________________|
                          
                          """)
            x = (input("ENTER YOUR CHOICE = "))
            
            if x == "a" or x == "A": # view staff
                staff_info()
                exit_AD()
                
            elif x == "b" or x == "B": # update (add and delete)
                update_staff()
                exit_AD()
                
            elif x == "c" or x == "C": # update (covid and job)
                revise_staff()
                exit_AD()
                
            elif x == "d" or x == "D": # search (id and name)
                search_staff()
                exit_AD()   
                
            elif x == "e" or x == "E": # menu
                menu()
                exit_AD()
                
            elif x == "f" or x == "F": # add item
                print("""
                  
                                                                                      MENU TABLE UPDATION
                                                                                 ____________________________                                          
                                                                                |                            |
                                                                                |      ADD A NEW ITEM        |                                       
                                                                                |____________________________|                                         
                  """)
                additem()
                exit_AD()
            elif x == "g" or x == "G": # update(item name and item price)
                update_item()
                exit_AD()
                
            elif x == "h" or x == "H": # search item (type and name)
                search_item()
                exit_AD()
                
            elif x == "i" or x == "i": # guest record
                guestrecord()
                exit_AD()
                
            elif x == "j" or x == "J": # view sales
                avgsales()
                exit_AD()

            else:
                break
    
    #GUEST
    elif ch== "b" or ch == "B":
        while True:
            print()
            print("""
                                                                                WELCOME TO THE GUEST SECTION
                                                                            ____________________________________
                                                                           |                                    |
                                                                           |     a. CREATE ACCOUNT              |
                                                                           |                                    |
                                                                           |     b. LOG IN                      |
                                                                           |____________________________________|
                                                                       
                      """)              
            g = (input("ENTER YOUR CHOICE = "))
           
            if g == "A" or g == "a":
                create_account()
                exit_AD()
           
            elif g == "B" or g == "b":
                guest_login()
                exit_AD()
                
                while True:
                    print()
                    print("""
                                                                           _____________________________________
                                                                          |                                    |
                                                                          |     a. VIEW ROOM DETAILS           |
                                                                          |                                    |
                                                                          |     b. BOOK A ROOM                 |
                                                                          |                                    |
                                                                          |     c. VIEW ACCOUNT DETAILS        |
                                                                          |                                    |
                                                                          |     d. UPDATE ACCOUNT DETAILS      |
                                                                          |                                    |
                                                                          |     e. FEEDBACK                    |
                                                                          |                                    |
                                                                          |     f. DELETE ACCOUNT              |
                                                                          |                                    |
                                                                          |     g. RATE US                     |
                                                                          |                                    |
                                                                          |     h. EXIT                        |
                                                                          |____________________________________|                                      
                             """)
                    g = input("ENTER YOUR CHOICE = ")
                
                    if g == "A" or g == "a":
                        roomtype()
                        exit_AD()    
                    
                    elif g == "B" or g == "b":
                        room_booking()
                        exit_AD()
            
                    elif g == "C" or g == "c":
                        view_acc()
                        exit_AD()
                    
                    elif g == "D" or g == "d":
                        update_details()
                        exit_AD()
            
                    elif g == "E" or g == "e":
                        feedback()
                        exit_AD()
            
                    elif g == "F" or g == "f":
                        delGT()
                        exit_AD()
            
                    elif g == "G" or g == "g":
                        rating()
                        exit_AD()
                
                    elif g == "H" or g == "h":
                        exit = input("\nDO YOU WANT TO LOG OUT OF YOUR ACCOUNT? (Y/N) = ")
                        if exit == "Y" or exit == "y":
                            print("*"*135,'\n')
                            print(" "*50, " YOU HAVE SUCCESSFULLY LOGGED OUT \n")
                            print("*"*135)
                            break
                exit = input("\nDO YOU WANT TO EXIT GUEST SECTION? (Y/N) = ")
                if exit == "Y" or exit == "y":
                    break
    
    #ABOUT US
    elif ch == "C" or ch == "c":
        print("""
                              ROYAL GALAXY, Doha, is an intimate and stylish urban retreat located in the centre of Msheireb Downtown Doha, 
                              the new lifestyle and cultural heart of the city. 
                              The hotel blends chic and contemporary design with touches of Qatari heritage, 
                              bringing new levels of luxury to Qatar. 
                              Designed by the world-renowned David Collins Studio, 
                              the hotel's rooms, 
                              suites and serviced apartments blend an elegant, 
                              contemporary design with subtle elements 
                              of traditional Qatari heritage. 
                              Royal Galaxy, Doha continues to exceed guest expectations with its legendary service excellence, 
                              which has been recognised and awarded the honorary distinction of the Forbes Five-Star rating in 2022.
              """)
        pass
    exit = input("\nDO YOU WANT TO CONTINUE? (Y/N) = ")
    if exit == "N" or exit == "n":
        exit_AU()
