#  real world==>> example

# 1...avoiding a crash(most important use)
user_data = {}
if 'age' in  user_data and user_data["age"] >18:
    print("user is adult")
else:
    print("age info missing")



#2... login system
username = ""
if username and check_password_in_database(username):
    print("login successful")
else:
    print("please enter a username")


#3.... checking list before using it

dataset = []
if len(dataset) > 0 and dataset[0] =='valid' :
    print('processing a first record')
else:
    print('dataset is empty')




# 4....
def slow_check():
    print("This ran!")
    return True

data = []
if len(data) > 0 and slow_check():
    print("Processing")
else:
    print("Skipped - no data")

###########..............

def check_username_exists(username):
    print(f"checking database for username: {username}")
    database = {"amit123" : "hashed_password_here"}
    return username in database
def check_password_correct(username , password):
    print(f"verifying password for :{username}")
    return True
username = "ishaa"
password = "12455"

if check_username_exists(username) and check_password_correct(username , password):
    print('login successful')
else:
    print('login failed')