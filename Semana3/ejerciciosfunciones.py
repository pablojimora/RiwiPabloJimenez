def greating(name:str)->str:
    print(f"Hello {name}")

def sum(num1:int,num2:int)->int:
    suma=num1+num2
    print(suma)

def circle_area(radio:float)->float:
    area=3.1415*(radio^2)
    print(area)

def pair_number(number:int):
    if number%2==0:
        print("The number is even")
    else:
        print("THe number is odd")

def greater_number(num1:float,num2:float,num3:float):
    numbers=[]
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)
    print(f"The greater number is {max(numbers)}")

def vocal_count(word:str)->int:
    account=0
    vowels="aeiouAEIOU"
    for i in word:
        if i in vowels:
            account+=1
    print(f"This word has {account} vocals")

def palindrome(word:str):
    inversedWord=word[::-1]
    if word == inversedWord:
        print("This word is palindrome")
    else:
        print("This word isnt palindrome")

def fibonacci_sequence(number:int):
    iterator=0
    iterator1=0
    iterator2=1
    sum:int=0
    while iterator<number:
        sum=iterator1+iterator2
        iterator1=sum
        iterator=iterator+1
        iterator2+=1
    print("")    
    print(sum)

def convert_temperature(degrees:float):
    convertion=(degrees*9/5)+32
    print(convertion)

def main():
    greating("Pablo")
    sum(10,10)
    circle_area(5)
    pair_number(2)
    greater_number(15.14,16.25,20)
    vocal_count("Pablo")
    palindrome("reconocer")
    fibonacci_sequence(3)
    convert_temperature(24)

main()