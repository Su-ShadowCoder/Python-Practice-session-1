
# Practice session 1:

# task 1:
# user_input = int(input("Enter a number and it will put that number into a multiplication table: "))
# for number in range(0, 11):
#     answer = user_input * number
#     print(f"{user_input} x {number} = {answer}")

# Task 2:
# evens = []
# odds = []
# for number in range(0, 10):
#     if number % 2 != 0:
#         odds.append(number)
#     else:
#         evens.append(number)
# print(f"evens: {evens}\nodds: {odds}")

# Task 3:
# def lst_splitter_into_even_odd_counter_function(lst):
#     evens = 0
#     odds = 0
#     for number in (lst):
#         if number % 2 != 0:
#             odds += 1
#         else:
#             evens += 1
#     return evens, odds

# # lst_one = sorted[11, 2, 24, 61, 48, 33, 3]
# user_input = input(f"please input a list: ")
# user_input_lst = [int(x.strip()) for x in user_input.split(",")]

# print(f"This is the list you have entered: {sorted(user_input_lst)}")
# answer_1, answer_2 = lst_splitter_into_even_odd_counter_function(user_input_lst)
# print(f"The number of even numbers : {answer_1}\nThe number of odd numbers : {answer_2}")


# Task 4:

# for number in range(10):
#     pir = number * str(number)
#     print(pir)

# Task 5:
# def sum_of_range(x, y):
#     sum_result = 0
#     for number in range(x, y + 1):
#         sum_result += number
#     return sum_result
# answer = sum_of_range(1, 74)
# print(answer)

# Task 6:
days_in_months = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31]
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sts = [1, 21, 31]
nds = [2, 22]
rds = [3, 23]
current_day = 0

for month, n_days in zip(months, days_in_months):
    for day in range(1, n_days + 1):
        if day in sts:
            day_addition = "st"
        elif day in nds:
            day_addition = "nd"
        elif day in rds:
            day_addition = "rd"
        else:
            day_addition = "th"
        print(f"{weekdays[current_day]}, {month} {day}{day_addition}")
        current_day = (current_day + 1) % len(weekdays)

# # learn how to zip and module interaction