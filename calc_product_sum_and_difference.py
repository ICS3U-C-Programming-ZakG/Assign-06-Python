#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 27, 2023
# This program calculates the product, sum, and difference using a list of numbers from the user.


# define function to calculate product
def calc_product(list_of_num):
    # initialize product
    product = 1

    # get product of numbers
    for a_num in list_of_num:
        product = product * a_num

    # return product of numbers
    return product


# define function to calculate sum
def calc_sum(list_of_num):
    # initialize sum
    sum = 0

    # get sum of numbers
    for a_num in list_of_num:
        sum = sum + a_num

    # return sum of numbers
    return sum


# define function to calculate difference
def calc_difference(list_of_num):
    # initialize variables
    difference = 0

    # calculate difference with first two numbers
    difference = list_of_num[0] - list_of_num[1]

    # check if strictly only two numbers
    if len(list_of_num) == 2:
        # return difference
        return difference

    else:
        # for...each loop subtracting all numbers in list from previously calculated difference
        for a_num in list_of_num:
            difference = difference - a_num

        # counteract the double subtraction of first two numbers by adding
        difference = difference + list_of_num[0] + list_of_num[1]

        # return difference of numbers
        return difference


def main():
    # introduce program user
    print(
        "Hello, this program is going to take a list of numbers and calculate the product, sum and the difference."
    )
    print()

    # declare list
    num_list = []

    # loop asking for a number
    while True:
        user_num = input("Please enter a number (type 'EXIT' to exit): ")

        # check if valid input
        try:
            # cast input to float
            user_num_float = float(user_num)

            # append number to list
            num_list.append(user_num_float)

        # catch invalid inputs
        except Exception:
            # exit from loop when user enters "EXIT"
            if user_num == "EXIT":
                # break out of loop
                break

            # tell user invalid input
            print("Please enter a number. {} is not valid.".format(user_num))

    # check if at least two numbers inputted
    if len(num_list) >= 2:
        # call function to calculate product
        calculated_product = calc_product(num_list)

        # call function to calculate product
        calculated_sum = calc_sum(num_list)

        # call function to calculate product
        calculated_difference = calc_difference(num_list)

        # display all user numbers
        print()
        for counter in range(len(num_list)):
            print("Your numbers are: {:.2f}".format(num_list[counter]))

        # display product
        print()
        print("The product is: {:.2f}.".format(calculated_product))

        # display sum
        print()
        print("The sum is: {:.2f}.".format(calculated_sum))

        # display difference
        print()
        print("The difference is: {:.2f}.".format(calculated_difference))

    # tell user not enough numbers
    else:
        print("You do not have at least two numbers to preform any calculations.")


if __name__ == "__main__":
    main()
