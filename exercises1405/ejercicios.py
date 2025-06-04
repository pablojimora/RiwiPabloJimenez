#1. Library Book Tracker

library={}

def add_book(title,author,pages):
    information=[]
    information.append(author)
    information.append(pages)
    information=tuple(information)
    library[title]=information

def find_book(title):
    if title in library.keys():
        print(library[title])
    else: 
        return "Book not found."
def show_books():
    print(library.keys())

# 2. Student Grade Manager

grades={}
def add_student(name:str):
    grades[name]=[]
    
def add_grade(name:str,grade:float):
    grades[name].append(grade)
    

def get_average(name:str):
    average= sum(grades[name])/len(grades[name])
    return (average)

# 3. Restaurant Menu Editor
menu={}
def add_dish(name:str,price:float,available:bool):
    information=[]
    information.append(price)
    information.append(available)
    menu[name]=information


def change_availability(name:str,available:bool):
    menu[name][1]=available

def total_available_price():
    total=0
    for i in menu.values():
        if i[1] == True:
            total=i[0]+total
    return total


# 4. Warehouse Box Counter
warehouse={}
def add_box(name:str,quantity:int):
    warehouse[name]=[]
    warehouse[name].append(quantity)

def update_quantity(name:str,quantity:int):
    warehouse[name]=[quantity]

def has_enough(name:str,quantity:int):
    if warehouse[name][0] <= quantity:
        return True
    else:
        return False 

# 5. Movie Rating System
movies={}
def add_movie(title):
    movies[title]=[]

def rate_movie(title,grade):
    movies[title].append(grade)

def average_rating(title):
    average= sum(movies[title])/len(movies[title])
    return(average)


# 6. Online Course Tracker
courses={}
def add_course(title,time,suscribers):
    course=[]
    course.append(time)
    course.append(suscribers)
    courses[title]=course
def update_enrollment(title,suscribers):
    courses[title][1]=suscribers

def filter_by_hours(time):
    filtered=[]
    for curso, valor in courses.items():
        if valor[0]>=time:
            filtered.append(curso)
    return(filtered)
# 7. To-Do List Organizer
todos={}
def add_task(name,priority):
    task=[]
    task.append(priority)
    todos[name]=task

def complete_task(name):
    todos[name].append("completed")

def filter_tasks(priority,status):
    filtered=[]
    for name,task in todos.items():
        if task[0]==priority and task[1]==status:
            filtered.append(name)
    return filtered


# 8. Digital Wallet
wallet={}
def add_expense(category,expense):
    if category not in wallet.keys():
        wallet[category]=[expense]
    else:
        wallet[category].append(expense)
def total_spent():
    return sum(map(lambda x: sum(x[1]), wallet.items()))
def expense_percentages():
    newwallet={}
    for category, expense in wallet.items():
        newwallet[category]=(sum(expense)/total_spent())*100
    return newwallet
        


# 9. Pet Adoption Center
pets=[{'name':'Ponta','specie':'Perro','age':14},{'name':'Levi','specie':'Gato','age':3}]
def add_pet(name,specie,age):
    pets.append({'name':name, 'specie':specie,'age':age})

def find_by_species(specie):
    petsnew=[]
    for i in pets:
        if i['specie']==specie:
            petsnew.append(i)
    return petsnew

def older_than(age):
    oldnew=[]
    for i in pets:
        if i['age']>=age:
            oldnew.append(i)
    return(oldnew)


# 10. Gym Membership System
members={}
def register_member(name,plan,statuspay):
    data=[]
    data.append(plan)
    data.append(statuspay)
    members[name]=data
def change_plan(name,plan):
    members[name][0]=plan
def unpaid_members(): 
    latemembers=[]
    for name,status in members.items():
        if status[1] == 'late':
            latemembers.append(name)
    return(latemembers)
