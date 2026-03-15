#This list holds the dict of every employee
employees=[]
print("---welcome to our employee's management system---")

while True:

    
#Choices that are given to the Users
    print("1.Display the employee's detail")
    print("2.Creating and Adding the employee's detail")
    print("3.Searching the employee's detail")
    print("4.Updating the employee's detail")
    print("5.Deleting the employee's detail")
    print("6.Exit from the employee's management system \n")
    

    choice=int(input("Enter your Choice: "))

    print()

#We use match case
    
    match choice:
#Here we need to check whether the current record is present or not to display
        
        case 1:
            
            if len(employees)==0:
                    print("No current Record in the Database!!!")

                    
            
#Displaying all the employees details              

            else:
                for emp in employees:
                    print("Details of the Employee: ")
                    print()
                    
                    print(f"Name of the Employee:  {emp["name"]}")
                    print(f"ID of the Employee:  {emp["id"]}")
                    print(f"Salary of the Employee:  {emp["salary"]}\n")

                
#Getting adhar and pan_no from the nested dictionary              
                    print(f"Documents of the Employee: ")
                    print(f"     => Adhaar of the Employee:  {emp["documents"]["adhar"]}")
                    print(f"     => Pan_number of the Employee:  {emp["documents"]["pan_no"]}\n")
                    print(f"Role of the Employee:  {emp["role"]}")
                
                    count=0
#Extracting skills from the skills list
                    print("Skills that employee has: ")
                    for skill in emp["skills"]:
                        count+=1
                        print(f"    {count} . {skill}")
                print()
                        
                print("-------------------------------------------------------")
                
                                 
                
#Adding the details into the employees list in the form of dictionary
        case 2:

            emp_keys=["name","id","salary","documents","role","skills"]
            emp=dict.fromkeys(emp_keys)
        
            emp["name"]=input("Enter employees name: ")
            emp["id"]=int(input("Enter employee's id: "))
            emp["salary"]=float(input("Enter employee's salary: "))
            print()

#Creating the documents

            print("Enter the Employee's document: ")
            doc_keys=["adhar", "pan_no"]
            doc=dict.fromkeys(doc_keys)

            doc["adhar"]=int(input("Enter Adhar number: "))
            doc["pan_no"]=input("Enter PAN number: ")
            
#Here we're updating documents key with the adhar and pan numbers
            emp["documents"]=doc

            emp["role"]=input("Enter employee's role: ")
            
#Skills need to be updated from the list
            skill_no=int(input("Enter your skill number: "))
            emp["skills"]=[input(f"{i} . ") for i in range(1,skill_no+1)]

            employees.append(emp)
            print()

            print("--------------------------------------------------------------")

            
#Searching the Employee's details using ID        
        case 3:
            
            search_id=int(input("Which ID you want to search?: "))
            for emp in employees:
#If required ID is present in list then print it
                if emp["id"]==search_id:
                    print("Yes we have this ID number in our record ")
                    print()
                    print(f"Name of the Employee: {emp["name"]}")
                    print(f"ID of the Employee: {emp["id"]}")
                    print(f"Salary of the Employee: {emp["salary"]}\n")

                    print(f"Documents of the Employee: ")
                    print(f"    Adhaar of the Employee: {emp["documents"]["adhar"]}")
                    print(f"    Pan_number of the Employee: {emp["documents"]["pan_no"]}\n")
                    print(f"Role of the Employee {emp["role"]}\n")

                    print("Skills that employee has: ")
                    for skill in emp["skills"]:
                        print(f" *  {skill}")
                        break
 #We have to use for else block here                       
                        
            else:
                print(f"There is no ID named {search_id} in our record")

            print()
            print("--------------------------------------------------------------")
            
            
#Updating the values
        case 4:
            print("Updating the Employees Detail:")
            
            

            search_id=int(input("Which ID you want to search?: "))
            for emp in employees:
                if search_id==emp["id"]:
#Continously ask the user until they exit by themselves
                    while True:
                        
                        print(f"Enter 1 if you want to change Name\n Your current Name is: {emp['name']}")
                        print()
                        print(f"Enter 2 if you want to change Salary\n current salary is: {emp["salary"]}")
                        print()
                        print(f"Enter 3 if you want to change Adhaar\n current adhaar number is: {emp["documents"]["adhar"]}")
                        print()
                        print(f"Enter 4 if you want to change Pan_number\n current pan_no is: {emp["documents"]["pan_no"]}")
                        print()
                        print(f"Enter 5 if you want to change Role of the Employee \n current role is: {emp["role"]}")
                        print()
                        print(f"Enter 6 if you want to change Skills")
                        print()
                        print(f"Enter 7 if you want to Exit from updation\n")
                        
                    
                    
                        update=int(input("Enter your Choice: "))
                    
                        match update:

                            #updating name with new name
                            case 1:
                                emp["name"]=input("Enter your new Name: ") or emp["name"]
                            #updating with new salary
                    
                            case 2:
                                salary = input("Enter new Salary: ")
                                emp["salary"] = float(salary) if salary else emp["salary"]
                            
                            #empty str * int gives error so we need to use ternary operator to resolve this
                            case 3:
                                adh=input("Enter your new adhar number: ")
                                emp["documents"]["adhar"]=int(adh) if adh else emp["documents"]["adhar"]

                                
                            #Updating with new pan number
                            case 4:
                                emp["documents"]["pan_no"]=input("Enter your new Pan number") or emp["documents"]["pan_no"]

                            #Updating with new role    
                            case 5:
                                emp["role"]=input("Enter your new role: ") or emp["role"]

                            #Iterate through the employees list ask the user whether to add or delete the skill 
                            case 6:
                                print("Current Skills are :")
                                for skill in emp["skills"]:
                                    print(f"    --> {skill}\n")
                                
                                print("Enter 1 to ADD the skill/s")
                                print("Enter 2 to DELETE the skill/s\n")
                                

                                choice_skill=int(input("Enter your choice: "))
                                n=int(input("How many skills you want to add/delete??"))
                                match choice_skill:
                                    #Adding new skills
                                    case 1:
                                        for i in range(n):
                                            new_skill=input("Enter new Skill/s")
                                            emp["skills"].append(new_skill)
                                        print("Added successfully!!!")

                                        
                                        
                                    #deleting the existing skills    
                                    case 2:
                                        for i in range(n):
                                            delete_skill=input("Enter the skill/s you want to delete: ")
                                            if delete_skill in emp["skills"]:
                                                emp["skills"].remove(delete_skill)

                                            else:
                                                print("Requested skill is not found in the Employee's database")
                    
                                    case _:
                                        print("Invalid choice")
                                
                                
                            case 7:
                                print("Employee's new data is Updated")
                                break

                            case _:
                                print("Invalid Choice!! Choose correct option to update")
                                

            
#To delete complete data from the database using the employee's Id
        case 5:
            delete_id=int(input("Enter the ID you want to delete: "))
            for emp in employees:
                if emp["id"]==delete_id:
                    employees.remove(emp)
                    print("Employee's data deleted")
                    break
                else:
                    print("Employees data not found")
            
#Choosing 6 to exit from the management system
        case 6:
            print("Existing from the Employee's Management System")
            break
            
#default case
        case _:
            print("Invalid Choice")
        
        
              





 


