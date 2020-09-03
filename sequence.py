n = int(input("Enter the length of the sequence: ")) # Do not change this line
number_a = 1
number_b = 2
number_c = 3
number_sum = 0


for number in range(1, n+1):
    if number == 1:
        print(number_a)
    elif number == 2:
        print(number_b)
    elif number == 3:
        print(number_c)
    else:
        number_sum = number_a + number_b + number_c
        number_a = number_b
        number_b = number_c
        number_c = number_sum
        print(number_sum)
