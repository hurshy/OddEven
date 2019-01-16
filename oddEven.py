#Odds and Evens
#Tyler Hegewald
numbers = [23,43,56,86,45,91,62,87,102,22,66,92,34,55,101]
odds = []
even = []
numOdds = 0
numEven = 0
#For Loop
for i in numbers:
    if i % 2 == 1:
        odds.append(i)
        numOdds = numOdds + 1
print("Here's the number of odds:",numOdds)

for i in numbers:
    if i % 2 == 0:
        even.append(i)
        numEven = numEven + 1
print("Here's the number of evens:",numEven)
