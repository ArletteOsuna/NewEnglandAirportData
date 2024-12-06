"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """

APPLES = .50
BREAD = 1.50
CHEESE = 2.25

numApples = 3
numBread = 10
numCheese = 6

prcApples = numApples * APPLES
prcBread = numBread* BREAD
prcCheese = numCheese * CHEESE
strApples = 'Apples'
strBread = 'Rye Bread'
strCheese = 'Cheese'
total = prcBread + prcCheese + prcApples

print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples:10s}{numApples:10d}\t${prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}\t${prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}\t${prcCheese:>5.2f}')
print(f'{"Total:":>20s}\t${total:>5.2f}')

