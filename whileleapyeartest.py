year = int(input())
# counter variables
leap_cnt = 0 
common_cnt = 0

current_year = 2024
# while loop sol'n
while year <= current_year : # while year < current_year +1:
    if year % 4 == 0:
        leap_cnt += 1 
    else:
        common_cnt += 1 
    year += 1 
    
print(f"{leap_cnt} leap years and {common_cnt} common years\ from {year} to {current_year}.")