########## login successful after 3 attempts

users ={
 "amit": "12345",
 "riya": "54321",
 "sid": "98765"
}

username = input("Enter Username : ")
password = input("Enter Password : ")

if username in users and users[username] == password:
    print("Login Succssful")
else:
    print('Invalid Username or Password')






############  shopping cart total

prices = []
while True:
    price = input("Enter price (or 'done' to finish): ")
    if price == "done":
        break
    prices.append(float(price))

total = sum(prices)
#total = 0
#for price in prices:
#   total += price
print(f"Total amount: {total}")