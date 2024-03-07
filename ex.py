import random
from datetime import date, datetime


class Ex:

    def call():
        list = ['I', 'kk']
        for w in list:
            print(w.title())

    def revArr():
        arr = []
        for num in range(10):
            arr.append(random.randint(1, 100))
        print('Random unsorted nums: ', arr)
        arr.sort()
        print('Sorted nums:          ', arr)
        arr.sort(reverse=True)
        print('Reverse sorted nums:  ', arr)

    def newPass():
        password = '!@#$%^&*)1234567890qwertyuiopasdfghjklzxcv'
        len_pass = int(input("length: "))
        a = "".join(random.sample(password, len_pass))
        print(f"password {a}")

    def sumOfNums():
        num = str(input("enter the number:"))
        sum = 0
        for n in num:
            sum += int(n)
        print(sum)
        
    def replaceCharAndUpperToWord_laptop():
        print(('laptop'.replace('l', 'k')).upper())

    def firstCharCapLetter():
        cities = ['kiyv', 'jerusalem', 'kfar saba']
        for city in cities:
            print(city.title())

    def countCapLetters():
        line = str(input("enter the line with caps & low letters:"))
        count = 0
        for word in line:
            for char in word:
                if char.isupper():
                    count += 1
        print(count)

    def currentDateTime():
        print("Today's date:", date.today())
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        print("The time is:", dt_string)

# Ex.currentDateTime()
# Ex.countCapLetters()
# Ex.newPass()
# Ex.firstCharCapLetter()
Ex.revArr()
# Ex.replaceCharAndUpperToWord_laptop()
# Ex.call()

