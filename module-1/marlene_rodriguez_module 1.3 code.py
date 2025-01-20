####Marlene Rodriguez
####Module 1.3

##Asks user to input numbers of bottles on the wall
Beer_Bottles = int(input("How many bottles of beer on the wall?: "))


##sets while loop to countdown until bottles zero out
while Beer_Bottles > 0:

    Beer_Bottles -=1

##if condition to print specific lyrics as long as bottles are greater than one
    if Beer_Bottles > 1:
        Total_Bottles = Beer_Bottles - 1
        print(Beer_Bottles, 'bottles of beer on the wall,',Beer_Bottles,'bottles of beer.'
              'Take one down and pass it around,', Total_Bottles, 'bottles of beer on the wall.')

##else if condition to change lyrics to singular mode and tell user to buy more beer
    elif Beer_Bottles <= 1:
        A_Total_Bottles = Beer_Bottles -1
        print(Beer_Bottles, 'bottle of beer on the wall,',Beer_Bottles,'bottle of beer.'
             'Take one down and pass it around,', A_Total_Bottles, 'bottles of beer on the wall.'
              'Time to buy more beer.')

        break

