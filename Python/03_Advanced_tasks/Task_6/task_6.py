import time

class Employee_Database:
    def __init__(self):
        self.employees={}
    
    def new_employee(self,name,job,salary,id):
        if id in self.employees:
            print(f"Employee with ID {id} already exists")
        else:
            self.employees[id]={'name':name,'job':job,'salary':salary}
            print(f"employee added successfuly, ID = {id}")
    
    def remove_employee(self,id):
        if id in self.employees:
            del self.employees[id]
            print(f"employee with ID {id} removed successfuly")
        else:
            print(f"employee with ID {id} not found")
    
    def print_employee(self,id):
        if id in self.employees:
            print(f"ID: {id}")
            print(f"Name: {self.employees[id]['name']}")
            print(f"Job: {self.employees[id]['job']}")
            print(f"Salary: {self.employees[id]['salary']}")
        else:
            print(f"employee with ID {id} not found")
    
    def update_employee(self,id,name=None,job=None,salary=None):
        if id in self.employees:
            if name:
                self.employees[id]['name']=name
            if job:
                self.employees[id]['job']=name
            if salary:
                self.employees[id]['salary']=name
            print(f"employee with ID {id} updated succesfuly")
        else:
            print(f"employee with ID {id} not found")
            
def main():
    db = Employee_Database()
    
    while True:
        print("Employee Database System")
        print(" 1. Add new employee")
        print(" 2. Remove employee")
        print(" 3. Print employee data")
        print(" 4. Update employee")
        print(" 5. Exit")
                    
        choice=int(input("select option : "))
    
        if choice == 1:
            id = input("Enter employee ID : ")
            name = input("Enter employee name : ")
            salary = input("Enter employee salary : ")            
            job = input("Enter employee job : ")
            db.new_employee(name,job,salary,id)
            
        elif choice == 2:
            id = input("Enter employee ID : ")
            db.remove_employee(id)
    
        elif choice == 3:
            id = input("Enter employee ID : ")
            db.print_employee(id)
        
        elif choice == 4:
            id = input("Enter employee ID : ")
            name = input("Enter new name (or leave blank to keep current): ")
            job = input("Enter new job (or leave blank to keep current): ")
            salary = input("Enter new salary (or leave blank to keep current): ") 
            db.update_employee(id,name,job,salary)
            
        elif choice == 5:
            print("Exiting system...")
            
        else:
            print("Invalid choice")
        
        time.sleep(1.5)
            
if __name__ == "__main__":
    main()
