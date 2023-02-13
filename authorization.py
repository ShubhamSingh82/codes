# decorator to check if a user has authorization to access a specific resource. 
def authorised(func):
        def inner(x, y):
            if y == "Admin":
                func(x, y)
            elif y == "user":
                print(f"{x} is an user and he can view only limited user")
            else:
                print(f"{x} is not authorized")
        return inner
@authorised          
def access(user_name,user_type):
    print(f"{user_name} is {user_type} and he has authorization to access the resources")
access("shubham","Admin")
access("rishi","user")